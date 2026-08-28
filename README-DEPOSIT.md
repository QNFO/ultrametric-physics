# README-DEPOSIT.md

## The Distinction-Based Ultrametric

A Hierarchy Distance Without Primes, and the Statistical Test of Arithmetic Structure in Physical Spectra

**Author:** Rowan Brad Quni-Gudzinas
**Date:** 2026-08-28
**License:** CC BY 4.0 (deposit license; see LICENSE-CC-BY-4.0.txt)

## How to cite

Cite all versions via the concept DOI (always resolves to the latest version):

> Quni-Gudzinas, Rowan Brad. (2026). *The Distinction-Based Ultrametric: A Hierarchy Distance Without Primes, and the Statistical Test of Arithmetic Structure in Physical Spectra*. Zenodo. 10.5281/zenodo.22150471

## Reproduce

Every quantitative statement in the paper is reproduced by a deposited, deterministic
script (seed 20260828, Python 3.12, NumPy 2.4.4, SciPy 1.17.1):

```bash
python scripts/sim-distinction-ultrametric-verification.py   # formula: LCA-depth + realization independence (6/6)
python scripts/sim-statistical-signatures-smoke.py           # Bost-Connes + log-periodic detector (7/7)
python scripts/sim-statistical-signatures-full.py            # synthetic three-way suite (8/8)
python scripts/sim-riemann-zeros-fast.py                     # Montgomery-Odlyzko law, N=3000 zeros (4/4)
python scripts/sim-benchmark-real.py                         # real-data benchmark with null models
```

Outputs are in `artifacts/verification/` (`*-output.json` + `*-run.txt`). The reference
list is rendered from `references.bib` (28 entries, every one cited in-body).

## Pre-registration

The disconfirmation criterion for the empirical claim is pre-registered at
https://osf.io/ba8ns/ (H-DIST-3, the five observables and their null models).

## Provenance

Source of record: https://github.com/QNFO/ultrametric-physics/tree/ump/paper/distinction-based-ultrametric
