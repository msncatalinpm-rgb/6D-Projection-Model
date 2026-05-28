# Toy Model 5G-L - Relational Metric Reconstruction Protocol

Status: proposed next mathematical object after 5G A-K failure analysis.

## Purpose

Toy Model 5G-L stops trying to fit the rotation curve directly. It reconstructs the effective operational metric / connection implied by the observed rotation curve, then asks whether that inferred geometry can be generated from baryonic organization by one universal rule.

## Motivation

5G A-G tested scalar thresholds and kernels. 5G-H showed the residual cannot be a simple positive additive field. 5G-I showed typed time-scheduling links are not enough. 5G-J and 5G-K showed simple Laplacian smoothing of acceleration or potential is not the hidden engine.

Therefore the next object must be the geometry/connection itself.

## Inputs

Use the same SPARC radial data:

- R
- V_obs(R)
- error bars
- V_gas(R)
- V_disk(R)
- V_bulge(R), if present
- fixed stellar mass-to-light rule: Upsilon_disk=0.5, Upsilon_bulge=0.7

## Reconstruct observed and baryonic fields

Compute:

V_bar^2(R) = V_gas^2(R) + Upsilon_disk V_disk^2(R) + Upsilon_bulge V_bulge^2(R)

g_obs(R) = V_obs^2(R) / R

g_bar(R) = V_bar^2(R) / R

Then reconstruct potentials by numerical integration:

Phi_obs(R) = integral g_obs(R) dR

Phi_bar(R) = integral g_bar(R) dR

Define the inferred relational geometry residual:

Delta_Phi_rel(R) = Phi_obs(R) - Phi_bar(R)

and/or the connection-like residual:

Delta_Gamma_rel(R) = d/dR [Phi_obs(R) - Phi_bar(R)]

## Core test

Do not fit a new velocity formula first.

First test whether Delta_Phi_rel or Delta_Gamma_rel collapses onto a universal relation with baryonic organization descriptors:

- surface-density proxy
- enclosed effective mass M_eff(R)
- mass-space gradient
- gas fraction
- concentration index
- disk scale proxy
- radial location normalized by baryonic scale radius
- nonlocal graph connectivity descriptors

## Success condition

The protocol succeeds if a small set of universal descriptors maps baryonic organization to the inferred relational metric/connection across galaxies without per-galaxy tuning.

## Failure condition

The protocol fails if each galaxy requires its own metric-generation rule, hidden halo-like parameters, or post-hoc rescue terms.

## Guardrails

- No dark halo fitting.
- No galaxy-specific metric law.
- No galaxy-specific rescue terms.
- All failures must be reported.
- This remains a falsification protocol, not physical validation.
