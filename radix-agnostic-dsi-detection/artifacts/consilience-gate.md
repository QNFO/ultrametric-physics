# Consilience Gate — KIF-29 (HARD) — QNFO.UMP.008

**Date:** 2026-08-12 | **Status:** PASS

## Cross-Domain Lexicon (dynamic, evidence-driven)

| Domain | Why chosen (evidence) | Lexicon terms |
|---|---|---|
| Statistical Signal Processing | The methodological home: FFT, Lomb-Scargle spectral estimation (Press & Rybicki 1989; Zechmeister & Kürster 2009) | periodogram, spectral peak, uneven sampling, frequency resolution |
| Complex Systems Science / Econophysics | The DSI phenomenon class: log-periodicity, discrete scale invariance (Sornette lineage; Huang 1997; Filimonov & Sornette 2013) | log-periodic oscillation, LPPL, DSI, critical time, bubble diagnosis |
| Ultrametric / p-adic Analysis | The theory class under test: Ostrowski completions, ultrametric hierarchy (Schikhof 1984; Avetisov 2002) | radix, valuation, ultrametric inequality, Bruhat–Tits, p-adic |
| Cosmology (CMB) | The real-data application: Planck 2018 TT, ΛCDM (CAL-03 anchor 10.5281/zenodo.21534747) | multipole ℓ, power spectrum, acoustic peaks, best-fit ΛCDM |
| Time Series / Econometrics | The null-model discipline: stationarity, spurious regression (Granger–Newbold) | stationarity, ADF/KPSS, differencing, residual |

## Minimum-Viable-Finding (per domain)

1. **Signal Processing → DSI:** The core reduction C1 — DSI under $x\to\lambda x$ becomes periodicity in $u=\ln x$ at $\omega_0=2\pi/\ln\lambda$ — is a non-trivial isomorphism: spectral estimation becomes radix measurement. Verified live (synthetic λ=1.62 recovered).
2. **Econophysics → Methodology gap:** LPPL literature fits ω continuously but treats the joint 6-parameter fit as valid; this project *disproves* that (joint fit collapses at true-peak init — D3) and replaces it with stage separation. Non-trivial corrective finding.
3. **p-adic Analysis → CMB:** The p-adic radix hypothesis (λ∈{2,3,5,7} ⇒ ω∈{9.07,5.72,3.90,3.23} rad) is empirically *testable* at the Planck multipole range (0.078 rad resolution) — the mapping from number theory to observable is concrete, not metaphorical.
4. **Cosmology → Honest null:** The G4 model-subtraction protocol is required for non-power-law spectra; raw scanning produces a self-refuting artifact. A null with correct null-model is informative.
5. **Time Series → Certification:** The bootstrap max-statistic p is already multiplicity-corrected; Sidak double-counts. This is the same look-elsewhere discipline as BP-3.

## Silo Cost Table

| Domain | Structure Name | Earliest | Connected | Silo Cost | Key Paper |
|---|---|---|---|---|---|
| Number Theory | Ostrowski completions / p-adic radix | 1916 | 2026 (QNFO CMB test) | **110 yr** | Ostrowski, Acta Math 1916 |
| Econophysics | Log-periodic power law | 1996 | 2026 (this protocol) | **30 yr** | Sornette et al. 1996 |
| Astronomy | Lomb-Scargle periodogram | 1989 | 2026 (radix-agnostic detector) | **37 yr** | Press & Rybicki 1989 |
| Ultrametric Physics | p-adic hierarchical dynamics | 2002 | 2026 (CMB application) | **24 yr** | Avetisov et al. 2002 |

[SILO-FAILURE: >50yr gap — Ostrowski→CMB test = 110 yr. This synthesis connects number theory to empirical cosmology through a certified detector.]

## Synthesis Consilience

**Meta-principle:** The universal measurement instrument for discrete scale invariance is *log-frequency estimation* — the radix is always the inverse log of a measured frequency, whether the structure is cosmological, financial, or hierarchical.

**Frontier Question (FQ-1):** In which complex systems does a measured DSI radix coincide with prime-rational values (λ∈{2,3,5,7,...}), and what distinguishes those systems from ones with generic λ?

## KIF-60 Bayesian Evidential Weight (sub-gate)

| Claim | Pre-registration | Falsifiability | Surprise accounting | Δlog-odds |
|---|---|---|---|---|
| C1 log-space reduction | Methodological identity (mathematical) | N/A (definition) | N/A | N/A (identity) |
| C2 radix recovery ≤0.02% | Detector calibration, verified in-session | Falsifiable: fresh synthetic λ∈[1.2,3.0] with C=0.3 must recover to ≤2% | Calibration statement (tool accuracy), not a world-claim | Calibration evidence |
| D1 no DSI in Planck | OSF pre-registration 2ndsz (2026-07-20) anchors the p-adic search program | Falsifiable: any resolvable ω in LCDM residuals with p<0.05 + gates=3 | Null — constrains but does not confirm | Negative constraint (honest) |
| D2 G4 mandatory | Discovered during application | Falsifiable: if raw-scan artifact passed gates on a non-power-law dataset, G4 unnecessary | Artifact mechanics understood | Methodological finding |
| D3 LPPL collapse | Reproduced twice (seed 42, 12345) | Falsifiable: if a joint LPPL fit ever recovers λ=1.62 to <3% at true-peak init | — | Corrective negative result |

**Gate verdict:** The p-adic correspondence claims (the program's speculative core) are either pre-registered (OSF 2ndsz) or honestly reported as nulls. No [RETRODICTION] classification needed — the paper's claims are calibration + honest null + methodology. **KIF-29 PASS.**

## Calibration Register

```
[CHECK: 2027] A second real dataset (non-CMB) scanned with dsi-radix-detector.py
--model; report any certified radix.
Strength: [MEDIUM] | Status: [PENDING]
---
[CHECK: 2028] FQ-1 answered for >=3 complex-system classes (cosmological, financial,
biological/geophysical) with a certified radix or certified null each.
Strength: [WEAK] | Status: [PENDING]
---
[CHECK: 2030] >=1 external citation of the radix-agnostic DSI methodology as a
bridging tool between spectral estimation and p-adic structure.
Strength: [WEAK] | Status: [PENDING]
```
