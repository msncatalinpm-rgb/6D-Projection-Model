# Roadmap: Toy Model 5G

## Target

Minimal Real-Galaxy Rotation-Curve Fitting Protocol.

## Why 5G Comes After Publication

The current V4.2 foundation is theoretical and structurally coherent.  
5G moves into real data and must be handled as a falsification protocol, not as a foundation claim.

## 5G Must Define Before Running

```text
dataset
sample selection
allowed parameters
global fixed parameters
per-galaxy parameters, if any
success criteria
failure criteria
residual metrics
plotting conventions
data provenance
reproducibility rules
```

## Recommended Dataset

Use a public galaxy rotation-curve dataset, likely SPARC-style data.

Do not include proprietary or unclear-source data.

## Anti-Cheating Rule

No hidden parameters should be introduced after looking at failed fits.

If a fit fails, record the failure.

## Expected Iterations

```text
Step 1: protocol design
Step 2: data ingestion script
Step 3: single-galaxy dry run
Step 4: small-sample run
Step 5: guardrail audit
Step 6: publish results, including failures
```

## Estimated Effort

5G is likely a separate heavy session, not a quick README edit.
