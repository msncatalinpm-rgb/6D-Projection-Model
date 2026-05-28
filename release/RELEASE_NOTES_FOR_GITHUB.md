# Toy Model 5G Public Baseline - Full SPARC Close-Out and 5G-N Roadmap

This release adds the Toy Model 5G public baseline to the V4.2 6D Projection Framework.

Toy Model 5G is the first real-data diagnostic extension of the V4.2 framework. It uses SPARC galaxy rotation-curve data to test whether the dark-sector analogue is better treated as a relational metric / connection reconstruction problem rather than as a direct acceleration correction.

## What this release contains

- A new root README framing the 6D Projection Framework as an integrated geometric research architecture.
- A clear explanation of the Embedded Observer Problem, accessibility limits, and intuitive geometric translation layer.
- Summaries of Toy Models 1-5 and the geometric interpretation each one tested.
- The Toy Model 5G public baseline and close-out document.
- Full-SPARC 5G-M diagnostic results.
- A-to-K failure analysis archive.
- Reproducibility notes, source data archive, validation harness code, selected plots, and CSV result tables.
- Roadmap for Toy Model 5G-N - Relational Metric Generation Law.

## Full-SPARC 5G-M diagnostic result

The full-SPARC 5G-M run processed:

```text
175 galaxies
3391 radial points
```

Mode 1 - frozen_four:

```text
R2 for chi:                 0.4613
Newtonian baryonic RMS:     58.57 km/s
5G-M RMS:                   36.46 km/s
Improved galaxies:          139 / 175
```

Mode 2 - train_groupkfold:

```text
R2 for chi:                 0.5669
Newtonian baryonic RMS:     58.57 km/s
5G-M RMS:                   24.69 km/s
Improved galaxies:          155 / 175
```

## Interpretation

The result does not validate the framework physically.

The result means something narrower:

> The residual structure in SPARC rotation curves appears more naturally handled as a relational metric / connection reconstruction problem than as a direct missing-acceleration patch.

This motivates the next mathematical step: Toy Model 5G-N - Relational Metric Generation Law.

## Strict non-claims

This release does not claim that V4.2 has:

- proven physical 3T;
- derived full quantum mechanics;
- derived Quantum Field Theory;
- derived the Standard Model;
- derived nonlinear General Relativity;
- derived the Einstein-Hilbert action;
- derived physical constants;
- solved dark matter;
- solved dark energy;
- replaced Lambda-CDM;
- disproven particle dark matter;
- achieved physical validation.

## Recommended starting points

- `README.md`
- `docs/5G/00_READ_ME_FIRST.md`
- `docs/5G/public_baseline/Toy_Model_5G_Public_Baseline_Close_Out_and_5G_N_Roadmap.pdf`
- `docs/5G/public_baseline/Toy_Model_5G-M_Full_SPARC_Run_Results.pdf`
- `docs/5G/roadmap/5G_N_Relational_Metric_Generation_Law_Roadmap.md`
