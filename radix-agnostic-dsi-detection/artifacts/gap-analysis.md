# Gap Analysis — QNFO.UMP.008

**Date:** 2026-08-12

## What QNFO already covers

- QNFO.UMP.007 (cmb-higher-n-point-functions, 10.5281/zenodo.21900192): radix-LOCKED p-adic bispectrum search, ε_p<2.5 null. Establishes the empirical channel.
- CAL-03 (10.5281/zenodo.21534747): radix-locked CMB log-periodogram (e/π/Efimov), global p=0.38 null.
- P5 analysis: p-adic ln2/ln3/ln5 two-point, global p=0.38 null.
- Methodological notes (`_26224105000.md`, `_26224105300.md`): survey + radix-agnostic protocol.
- Tool: `dsi-radix-detector.py` (research skill, committed).

## What external literature covers (verified this session)

- Sornette lineage: LPPL calibration, log-periodic DSI in complex systems (finance, physics).
- Lomb-Scargle spectral estimation (astronomy).
- p-adic/ultrametric theory (Schikhof, Avetisov, Robert).
- Causal/dependency, DFA/multifractal, symbolic regression (survey breadth).

## The gap (novelty space)

**No published work fuses spectral estimation + log-periodic DSI detection +
p-adic theory into a single CERTIFIED radix-agnostic detector with:**

1. Three-stage separation (detrend → spectral peak → bounded sinusoid) —
   empirically shown to be REQUIRED (joint LPPL collapses, D3).
2. Max-statistic bootstrap certification (already multiplicity-corrected —
   the Sidak double-counting error is a trap others would hit).
3. Integrity gates (resolvability, amplitude SNR, radix precision) enforced
   by default in the tool.
4. G4 model-subtraction protocol for non-power-law data.
5. A definitive, certification-backed null on real Planck 2018 data at full
   continuous radix coverage (not just 4 locked primes).

**Is the proposed research genuinely novel?** YES within the bounded claim:
the *methodology + certification + tool* is novel; the empirical null
reinforces (does not contradict) prior radix-locked analyses. The novelty is
in the measurement instrument, not in claiming new physics.

## Vectorize Confirmation-Bias Disclosure

All 10 Vectorize hits for the core query were QNFO-internal.
**[CONFIRMATION-BIAS-RISK]** — mitigated by the 15 externally-verified DOIs
(OpenAlex title-match) that anchor the external landscape. The gap is
therefore assessed against real external literature, not only the internal
corpus.
