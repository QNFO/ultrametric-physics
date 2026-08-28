# OSF Pre-Registration — QNFO.UMP.014 H-DIST-3 Disconfirmation Criterion

- **OSF node:** https://osf.io/ba8ns/
- **GUID:** `ba8ns` (child of the Pre-Registration Hub `jtrh7`)
- **Created:** 2026-08-28 (token-verified, user `6hyj8` = Rowan Brad Quni-Gudzinas)
- **Paper:** `distinction-based-ultrametric.md` (commit `a0a0734`)
- **GitHub:** QNFO/ultrametric-physics, branch `ump/paper/distinction-based-ultrametric`

## Pre-registered content

**Claim (H1 of the Ultrametric Program, 10.5281/zenodo.22076816).** Physical spectra may
carry arithmetic information beyond universal random-matrix statistics.

**Observables (five, each with a null model).**
1. Pair correlation R2(s) after unfolding — GUE bulk 1 − (sin πs/πs)² plus
   Bogomolny–Keating arithmetic corrections.
2. Spectral form factor K(τ) — ramp versus plateau.
3. Number variance Σ²(L) and rigidity Δ₃(L) — GUE (1/π²) log L versus Poisson L.
4. Bost–Connes partition thermodynamics Z(β) = ζ(β), phase transition at β = 1.
5. Subleading log-periodic corrections f(x) = x^α (1 + ε cos(2π log x / log λ)).

**Null models.** Pure GUE (random-matrix theory) and Poisson.

**Disconfirmation criterion.** Pure GUE statistics with no arithmetic corrections in
N ≥ 10³ systems falsifies the program at the statistical-distribution level, feeding
the 2028 decision point of RES.023.

**Multiple comparisons.** Corrected p-values via Bonferroni–Holm over the five
observables; empirical p-values from a Monte Carlo null (Poisson and GUE/GOE at
n = 2000 through the same smoothed-staircase unfolding).

## Pre-commitment anchor

The criterion was locked in git **before** the confirmatory analysis:

- `PROJECT-PLAN.md` §4 (H-DIST-3) — revision 3, commit `e5a673d`
- `BENCHMARK-DESIGN-UMP014.md` — commit `e5a673d`

Executed results are recorded in `artifacts/verification/` (commits `39381f6`, `f9593b0`,
`a0a0734`). The OSF node is therefore a dated public anchor pointing at a
pre-committed criterion, not a post-hoc one.

## Executed results (transparency)

- Riemann zeros: pair correlation matches GUE (mean |Δ| = 0.061, N = 3000) — the
  Montgomery–Odlyzko law, computationally confirmed.
- NaH Rivlin (3,339 levels): rejects both nulls (p = 0.000 vs Poisson and vs GUE).
- H2O POKAZATEL (200,000 states): Poisson-like (p = 1.000 vs Poisson, p = 0.000 vs GUE).
- Null-machinery calibration controls pass (3-control medians).
