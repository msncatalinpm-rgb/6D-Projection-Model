# GitHub Submission Instructions - V4.2 Toy Model 5G Public Baseline

## Recommended release

**Release title:** Toy Model 5G Public Baseline - Full SPARC Close-Out and 5G-N Roadmap

**Tag:** `v4.2-5g-public-baseline`

**Branch:** `main`

## Upload strategy

This package is prepared as a repository overlay. Copy its contents into the repository root, preserving the folder structure.

The most important file is the new root `README.md`. This is the GitHub front page. It now starts with the general model category, embedded-observer/accessibility interpretation, and Toy Models 1-5 before introducing 5G.

## Suggested command sequence

```bash
git checkout main
git pull

# Copy the package contents into the repository root, preserving folders.
# Then review locally before committing.

git status

git add README.md README_ROOT_UPDATE.md 00_READ_ME_FIRST.md

git add docs/5G figures/5G results/5G code/5G data/5G release GITHUB_SUBMISSION_INSTRUCTIONS.md MANIFEST.md

git commit -m "Add Toy Model 5G public baseline and full SPARC diagnostic results"

git tag v4.2-5g-public-baseline

git push origin main

git push origin v4.2-5g-public-baseline
```

Then create a GitHub Release from the tag.

## Release notes summary

Use `release/RELEASE_NOTES_FOR_GITHUB.md` as the release body.

## Guardrails

Do not describe this release as physical validation.

Do not say:

- 6D is proven.
- Dark matter is solved.
- Lambda-CDM is replaced.
- Particle dark matter is false.
- Physical 3T is proven.

Use:

- reproducible diagnostic baseline;
- full-SPARC diagnostic run;
- relational metric reconstruction path;
- systematic failures remain;
- 5G-N is the next mathematical step.

## Files to check on GitHub after upload

1. Root `README.md` renders correctly.
2. `docs/5G/00_READ_ME_FIRST.md` is visible.
3. The two main PDFs open:
   - `docs/5G/public_baseline/Toy_Model_5G_Public_Baseline_Close_Out_and_5G_N_Roadmap.pdf`
   - `docs/5G/public_baseline/Toy_Model_5G-M_Full_SPARC_Run_Results.pdf`
4. CSV files display in `results/5G/`.
5. `data/5G/Rotmod_LTG.zip` is present for reproducibility.
6. The release tag is `v4.2-5g-public-baseline`.
