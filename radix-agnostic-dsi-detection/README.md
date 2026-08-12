# Radix-Agnostic Detection of Discrete Scale Invariance (QNFO.UMP.008)

A certified, radix-agnostic detector for discrete scale invariance (DSI) —
log-periodic structure whose scaling radix is unknown and must not be assumed.

## Core result

DSI under $x \to \lambda x$ becomes periodicity in $u=\ln x$ with
$\omega_0 = 2\pi/\ln\lambda$. Three-stage protocol (detrend → spectral peak →
bounded sinusoid refinement) recovers a **non-prime** radix λ=1.62 to ≤0.02%
error; bootstrap-null + ΔBIC + integrity-gate certification is mandatory.

## Planck 2018 application (honest null)

No certified DSI at any resolvable radix in the CMB temperature spectrum —
including p-adic radices λ∈{2,3,5,7} — consistent with the radix-locked nulls
(CAL-03 p=0.38; P5 p=0.38). G4 model-subtraction is required for non-power-law
data; raw-spectrum scanning produces a self-refuting artifact the gates reject.

## Artifacts

- `docs/core-claim.md` — locked core claims C1-C3, D1-D3 (P6)
- `artifacts/` — consilience gate, evidential-weight, fit-verify (P1/P4)
- `notebooks/` — synthetic + real-data verification
- `releases/` — published `<slug>.md/.pdf/.html` (P5)

## Tool

The detector lives in the research skill (git-tracked):
`research/scripts/dsi-radix-detector.py` — `--data in.csv` (scale,value),
`--model modelcol` for G4 residual mode. Committed QNFO/qnfo-skills
(a9db635 → 50cb510 → ca6a965).
