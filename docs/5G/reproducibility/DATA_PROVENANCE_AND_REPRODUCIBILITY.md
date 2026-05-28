# Data Provenance and Reproducibility

## Dataset

The full-SPARC run used the uploaded archive:

`data/Rotmod_LTG.zip`

This archive contains SPARC-style `*_rotmod.dat` files. The run processed:

- 175 galaxies;
- 3391 radial points.

## Baryonic mass-to-light rules

The pipeline used the fixed stellar mass-to-light rules inherited from the 5G pilot protocol:

- disk mass-to-light factor: 0.5;
- bulge mass-to-light factor: 0.7.

These were not fitted galaxy-by-galaxy.

## Reproducibility command

From the package root:

```bash
pip install -r code/requirements.txt
python code/run_5G_M_full_sparc_validation.py --rotmod-zip data/Rotmod_LTG.zip --out-dir results_rerun
```

## Guardrails

The full-SPARC run did not use dark halo parameters, galaxy-specific tuning, or post-hoc removal of failed galaxies.

## Important caution

This package contains a reproducible diagnostic run. It should not be treated as independent astrophysical validation until reproduced by external reviewers using the official SPARC source files and the frozen code.
