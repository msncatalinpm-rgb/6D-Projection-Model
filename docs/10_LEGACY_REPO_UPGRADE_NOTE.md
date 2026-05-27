# Legacy Repository Upgrade Note

This repository previously contained V4 / V4.1 material.

The current active release is V4.2.

## Recommended handling of older files

If older V4 / V4.1 files are still present in the repository root, move them into:

```text
legacy_v4_v4.1/
```

or keep them only in Git history.

Do not leave older V4.1 materials in positions that make them look like the current active framework.

## Why this matters

Without this note, readers may confuse:

```text
V4 / V4.1 = historical conceptual baseline
V4.2 = current active toy-model framework
```

The V4.2 release should be the front door.

## Do not delete history blindly

Preserving earlier versions is useful, but they should be clearly labelled as historical.
