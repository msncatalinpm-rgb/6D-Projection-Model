# Toy Model 5G Public Baseline - Read Me First

**Version:** V4.2 post-release data-protocol baseline  
**Package date:** 2026.05.28  
**Status:** Full-SPARC diagnostic run complete; not physical validation.

## What this is

Toy Model 5G is the first real-data diagnostic track after the V4.2 GitHub publication baseline. It tests whether the 6D Projection Framework's relational-organization idea can be expressed as a reproducible rotation-curve protocol using public SPARC radial baryonic data.

The correct category is:

> A reproducible falsification and metric-reconstruction protocol inside a speculative integrated geometric research architecture.

It is **not** a completed physical theory, not a dark-matter replacement claim, and not proof of physical 3T.

## Why this package exists

The earlier V4.2 publication taught a direct lesson: public-facing material must explain the model category and purpose before listing files or equations. This package therefore leads with the frame:

**Relationship -> Organization -> Observable Order**

For 5G, the observable order is the galaxy rotation curve. The tested hidden object is not a dark halo. It is an empirical relational metric distortion field:

`chi(R) = ln[g_obs(R) / g_bar(R)]`

## Full-SPARC result in one paragraph

Toy Model 5G-M ran on **175 SPARC galaxies** and **3391 radial points** from `Rotmod_LTG.zip`. In frozen-four mode, the four-galaxy 5G-L coefficients were applied to the full archive: `R2 chi = 0.4613`, RMS improved from `58.57 km/s` Newtonian baryonic baseline to `36.46 km/s`, with `139 / 175` galaxies improved. In group-holdout mode using the same frozen feature set, `R2 chi = 0.5669`, RMS improved to `24.69 km/s`, with `155 / 175` galaxies improved.

This is a strong diagnostic improvement. It is not physical validation.

## Reproducibility Quick Check

To reproduce the headline 5G-M diagnostic run locally, use the committed validation script and SPARC archive:

```bash
cd code/5G
pip install -r requirements.txt
python run_5G_M_full_sparc_validation.py
```

The run should process:

```text
175 galaxies
3391 radial points
```

The headline outputs expected from the current committed baseline are:

```text
Mode 1: frozen_four
R2 for chi:                 0.4613
Newtonian baryonic RMS:     58.57 km/s
5G-M RMS:                   36.46 km/s
Improved galaxies:          139 / 175

Mode 2: train_groupkfold
R2 for chi:                 0.5669
Newtonian baryonic RMS:     58.57 km/s
5G-M RMS:                   24.69 km/s
Improved galaxies:          155 / 175
```

If these values change after future edits, the change should be documented in the results folder and in the release notes. The current 5G-M package should not be described as a validation claim; it is a reproducible diagnostic baseline.

## What to read first

1. `docs/public_baseline/Toy_Model_5G_Public_Baseline_Close_Out_and_5G_N_Roadmap.pdf`
2. `docs/public_baseline/Toy_Model_5G-M_Full_SPARC_Run_Results.pdf`
3. `docs/roadmap/5G_N_Relational_Metric_Generation_Law_Roadmap.md`
4. `docs/reproducibility/DATA_PROVENANCE_AND_REPRODUCIBILITY.md`
5. `docs/STRICT_NON_CLAIMS.md`

## Main guardrail

The result supports the next mathematical phase: **5G-N - Relational Metric Generation Law**.

It does not authorize claims that V4.2 has solved dark matter, replaced Lambda-CDM, disproven particle dark matter, or proven a hidden 3T sector.
