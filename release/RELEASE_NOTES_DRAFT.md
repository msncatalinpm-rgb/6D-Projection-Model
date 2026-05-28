# Release Notes - Toy Model 5G Public Baseline

## Release purpose

This release packages the Toy Model 5G real-data diagnostic track for public GitHub review.

## Core result

The full-SPARC 5G-M run processed 175 galaxies and 3391 radial points.

| Mode | R2 chi | RMS 5G-M | RMS Newtonian | Improved galaxies |
|---|---:|---:|---:|---:|
| frozen_four | 0.4613 | 36.46 km/s | 58.57 km/s | 139 / 175 |
| train_groupkfold | 0.5669 | 24.69 km/s | 58.57 km/s | 155 / 175 |

## Interpretation

This is a strong diagnostic improvement over the Newtonian baryonic baseline. It supports continuing the relational metric reconstruction path.

It is not physical validation.

## Next step

Toy Model 5G-N - Relational Metric Generation Law.
