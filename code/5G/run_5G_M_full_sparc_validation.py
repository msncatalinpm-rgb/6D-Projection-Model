#!/usr/bin/env python3
"""
Toy Model 5G-M - Frozen 5G-L Full-SPARC Validation Harness

Purpose:
  Expand 5G-L from the four-galaxy diagnostic set to the full SPARC Rotmod_LTG sample
  without changing the mathematical object.

Modes:
  1) frozen_four: apply coefficients learned from the 5G-L four-galaxy run to all available SPARC files.
  2) train_test: train the same 5G-L formulation on a declared training subset and test the holdout.

Strict guardrail:
  This script is not allowed to add dark halos, per-galaxy tuning, new features after inspection,
  or galaxy-specific correction parameters.
"""
from pathlib import Path
import argparse, json, zipfile, urllib.request, math, sys
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GroupKFold
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

ZENODO_ROTMOD_URL = 'https://zenodo.org/records/16284118/files/Rotmod_LTG.zip?download=1'
OFFICIAL_SPARC_URL = 'https://astroweb.case.edu/SPARC/'

G = 4.30091e-6
YDISK = 0.5
YBULGE = 0.7
GREF_INTERNAL = 1000.0
MREF = 1e10
SIGREF = 1e8
FEATURES = ['log_gbar','log_Meff','log_Mtotal','log_R','log_Sigma_eff','slope_g_bar_internal','slope_Meff_Msun']
FROZEN_COEFS = {
  'intercept': 1.141241587420997,
  'log_gbar': -0.08869693624996525,
  'log_Meff': 0.017767341530992263,
  'log_Mtotal': -0.03404761659935218,
  'log_R': 0.11785596832115343,
  'log_Sigma_eff': -0.0886969362499652,
  'slope_g_bar_internal': -0.036990659605920316,
  'slope_Meff_Msun': -0.03699065960592011,
}

def download_if_needed(data_dir: Path):
    data_dir.mkdir(parents=True, exist_ok=True)
    if list(data_dir.glob('*_rotmod.dat')):
        print(f'Found existing rotmod files in {data_dir}')
        return
    zip_path = data_dir.parent/'Rotmod_LTG.zip'
    if not zip_path.exists():
        print(f'Downloading SPARC Rotmod_LTG.zip from Zenodo: {ZENODO_ROTMOD_URL}')
        urllib.request.urlretrieve(ZENODO_ROTMOD_URL, zip_path)
    with zipfile.ZipFile(zip_path,'r') as z:
        z.extractall(data_dir)
    # If zip contains nested folder, move files up
    for f in list(data_dir.rglob('*_rotmod.dat')):
        if f.parent != data_dir:
            target = data_dir/f.name
            if not target.exists(): f.rename(target)
    print(f'Prepared {len(list(data_dir.glob("*_rotmod.dat")))} rotmod files in {data_dir}')

def read_rotmod(path: Path):
    rows=[]
    with open(path,'r',errors='ignore') as f:
        for line in f:
            s=line.strip()
            if not s or s.startswith('#') or s.startswith(';'):
                continue
            parts=s.split()
            if len(parts)<6: continue
            try:
                vals=[float(x) for x in parts[:6]]
            except ValueError:
                continue
            rows.append(vals)
    if not rows: return None
    df=pd.DataFrame(rows, columns=['R_kpc','Vobs_kms','eVobs_kms','Vgas_kms','Vdisk_kms','Vbulge_kms'])
    name=path.name.replace('_rotmod.dat','').replace('.dat','')
    df['galaxy']=name
    return df

def prepare(df):
    df=df.copy()
    df=df[(df['R_kpc']>0)&(df['Vobs_kms']>0)].copy()
    df['Vbar2_kms2']=df['Vgas_kms']**2+YDISK*df['Vdisk_kms']**2+YBULGE*df['Vbulge_kms']**2
    df=df[df['Vbar2_kms2']>0].copy()
    df['Vbar_kms']=np.sqrt(df['Vbar2_kms2'])
    df['g_bar_internal']=df['Vbar2_kms2']/df['R_kpc']
    df['g_obs_internal']=df['Vobs_kms']**2/df['R_kpc']
    df['metric_chi_obs']=np.log(df['g_obs_internal']/df['g_bar_internal'])
    df['g_rel_internal']=df['g_obs_internal']-df['g_bar_internal']
    df['Meff_Msun']=df['R_kpc']*df['Vbar2_kms2']/G
    mtot=df.groupby('galaxy')['Meff_Msun'].max().to_dict()
    df['Mtotal_proxy_Msun']=df['galaxy'].map(mtot)
    df['Sigma_eff_Msun_kpc2']=df['Meff_Msun']/(np.pi*df['R_kpc']**2)
    for col in ['g_bar_internal','Meff_Msun']:
        df['slope_'+col]=np.nan
    for gal, sub in df.groupby('galaxy'):
        idx=sub.index
        lr=np.log(sub['R_kpc'].values)
        for col in ['g_bar_internal','Meff_Msun']:
            yy=np.log(np.maximum(sub[col].values,1e-30))
            sl=np.gradient(yy,lr) if len(yy)>=2 else np.zeros_like(yy)
            df.loc[idx,'slope_'+col]=sl
    df['log_gbar']=np.log(np.maximum(df['g_bar_internal'],1e-30)/GREF_INTERNAL)
    df['log_Meff']=np.log(np.maximum(df['Meff_Msun'],1e-30)/MREF)
    df['log_Mtotal']=np.log(np.maximum(df['Mtotal_proxy_Msun'],1e-30)/MREF)
    df['log_R']=np.log(df['R_kpc']/10.0)
    df['log_Sigma_eff']=np.log(np.maximum(df['Sigma_eff_Msun_kpc2'],1e-30)/SIGREF)
    return df

def predict_frozen(df):
    chi=np.full(len(df), FROZEN_COEFS['intercept'], dtype=float)
    for f in FEATURES:
        chi += FROZEN_COEFS[f]*df[f].values
    return chi

def add_predictions(df, chi_col='metric_chi_pred'):
    df['metric_factor_pred']=np.exp(df[chi_col])
    df['g_model_internal']=df['g_bar_internal']*df['metric_factor_pred']
    df['Vmodel_kms']=np.sqrt(np.maximum(df['R_kpc']*df['g_model_internal'],0))
    df['Vnewton_kms']=df['Vbar_kms']
    df['residual_kms']=df['Vobs_kms']-df['Vmodel_kms']
    df['residual_newton_kms']=df['Vobs_kms']-df['Vnewton_kms']
    return df

def summarize(df):
    rows=[]
    for gal,sub in df.groupby('galaxy'):
        rows.append({'galaxy':gal,'n_points':len(sub),
            'RMS_5G_M_km_s':float(np.sqrt(np.mean(sub['residual_kms']**2))),
            'RMS_Newtonian_km_s':float(np.sqrt(np.mean(sub['residual_newton_kms']**2))),
            'mean_chi_obs':float(sub['metric_chi_obs'].mean()),
            'mean_chi_pred':float(sub['metric_chi_pred'].mean()),
            'negative_g_rel_points':int((sub['g_rel_internal']<0).sum()),
            'Mtotal_proxy_Msun':float(sub['Mtotal_proxy_Msun'].iloc[0])})
    return pd.DataFrame(rows).sort_values('RMS_5G_M_km_s')

def make_plots(df, summary, out_dir):
    fig_dir=out_dir/'figures'; fig_dir.mkdir(parents=True, exist_ok=True)
    pdf_path=fig_dir/'5G_M_Full_SPARC_Validation_Plots.pdf'
    with PdfPages(pdf_path) as pdf:
        fig,ax=plt.subplots(figsize=(8,6))
        ax.scatter(df['metric_chi_obs'],df['metric_chi_pred'],s=8,alpha=.5)
        mn=min(df['metric_chi_obs'].min(),df['metric_chi_pred'].min()); mx=max(df['metric_chi_obs'].max(),df['metric_chi_pred'].max())
        ax.plot([mn,mx],[mn,mx],'--')
        ax.set_xlabel('Observed chi = ln(g_obs/g_bar)')
        ax.set_ylabel('Predicted chi')
        ax.set_title('5G-M full-sample metric reconstruction check')
        ax.grid(alpha=.3); fig.tight_layout(); pdf.savefig(fig); plt.close(fig)
        # worst 12 plots
        for gal in summary.sort_values('RMS_5G_M_km_s',ascending=False).head(12)['galaxy']:
            sub=df[df['galaxy']==gal]
            fig,ax=plt.subplots(figsize=(8,5))
            ax.errorbar(sub['R_kpc'],sub['Vobs_kms'],yerr=sub['eVobs_kms'],fmt='o',label='V_obs',ms=3)
            ax.plot(sub['R_kpc'],sub['Vbar_kms'],label='V_bar')
            ax.plot(sub['R_kpc'],sub['Vmodel_kms'],label='5G-M prediction')
            ax.set_xlabel('R (kpc)'); ax.set_ylabel('Velocity (km/s)')
            ax.set_title(f'Worst-case check: {gal}')
            ax.legend(fontsize=8); ax.grid(alpha=.3); fig.tight_layout(); pdf.savefig(fig); plt.close(fig)
    return pdf_path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--data-dir', default='data/5G/raw/Rotmod_LTG')
    ap.add_argument('--out-dir', default='results/5G_M_full_sparc')
    ap.add_argument('--download', action='store_true')
    ap.add_argument('--mode', choices=['frozen_four','train_groupkfold'], default='frozen_four')
    args=ap.parse_args()
    data_dir=Path(args.data_dir); out_dir=Path(args.out_dir); out_dir.mkdir(parents=True, exist_ok=True)
    if args.download: download_if_needed(data_dir)
    files=sorted(data_dir.glob('*_rotmod.dat'))
    if not files:
        raise SystemExit(f'No *_rotmod.dat files found in {data_dir}. Run with --download or place Rotmod_LTG files there.')
    dfs=[]
    for f in files:
        d=read_rotmod(f)
        if d is not None and len(d)>=4: dfs.append(d)
    raw=pd.concat(dfs,ignore_index=True)
    df=prepare(raw)
    if args.mode=='frozen_four':
        df['metric_chi_pred']=predict_frozen(df)
        mode_note='Frozen coefficients from the 5G-L four-galaxy baseline applied to all available galaxies.'
    else:
        X=df[FEATURES].values; y=df['metric_chi_obs'].values; groups=df['galaxy'].values
        preds=np.zeros_like(y)
        gkf=GroupKFold(n_splits=min(5,len(set(groups))))
        for tr,te in gkf.split(X,y,groups):
            mod=make_pipeline(StandardScaler(), Ridge(alpha=100.0))
            mod.fit(X[tr],y[tr]); preds[te]=mod.predict(X[te])
        df['metric_chi_pred']=preds
        mode_note='Five-fold group holdout by galaxy using the frozen 5G-L feature set and ridge alpha=100.'
    df=add_predictions(df)
    summary=summarize(df)
    summary.to_csv(out_dir/'5G_M_Per_Galaxy_Summary.csv',index=False)
    df.to_csv(out_dir/'5G_M_Point_Diagnostics_Combined.csv',index=False)
    stats={'mode':args.mode,'note':mode_note,'n_galaxies':int(df['galaxy'].nunique()),'n_points':int(len(df)),
           'R2_metric_chi':float(r2_score(df['metric_chi_obs'],df['metric_chi_pred'])),
           'RMSE_metric_chi':float(mean_squared_error(df['metric_chi_obs'],df['metric_chi_pred'])**0.5),
           'global_RMS_5G_M_km_s':float(np.sqrt(np.mean(df['residual_kms']**2))),
           'global_RMS_Newtonian_km_s':float(np.sqrt(np.mean(df['residual_newton_kms']**2))),
           'negative_g_rel_points':int((df['g_rel_internal']<0).sum())}
    (out_dir/'5G_M_Run_Summary.json').write_text(json.dumps(stats,indent=2))
    make_plots(df,summary,out_dir)
    print(json.dumps(stats,indent=2))

if __name__=='__main__': main()
