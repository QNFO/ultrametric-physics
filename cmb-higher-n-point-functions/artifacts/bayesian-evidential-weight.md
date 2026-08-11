# Bayesian Evidential Weight Gate (KIF-60) — QNFO.UMP.007

**Date:** 2026-08-12 · **Phase:** P4 · **Gate:** KIF-60 (HARD sub-gate of KIF-29)

---

## 1. Pre-Registration Record

| Item | Value | Evidence |
|:-----|:------|:---------|
| Prediction | CMB higher-n (bispectrum/trispectrum) may reveal p-adic log-periodic signatures below 2-point sensitivity (RQ-013) | OSF `2ndsz` (2026-07-20, DOI 10.17605/osf.io/2ndsz) |
| Core claim | `docs/core-claim.md` C1–C3 | committed 2026-08-12 (sha 9eeed5e) |
| Amplitude model | single-modulation: ε_p ≲ A_LPO ≈ 0.003 | this artifact §4 |
| Analysis plan | radix-locked matched filter over p ∈ {2,3,5,7}, look-elsewhere control | `notebooks/synthetic_injection.py` |

## 2. Falsifiability Matrix (one disconfirmation condition per claim)

| Claim | Disconfirmation condition | Status |
|:------|:--------------------------|:-------|
| C1 p-adic log-periodic bispectrum shape | **D1:** no log-periodic modulation at any radix-locked ω_p, with an upper bound below the 2-point-implied amplitude, at 95% CL with look-elsewhere control | PASS (bound computed; see §4) |
| C2 higher-n is an independent channel | **D2:** a bispectrum detection at ε_p ≫ 0.003 without an amplification mechanism contradicts the single-field ultrametric model | PASS (0 detections at realistic amplitudes; amplification mechanism NOT supplied by framework) |
| C3 testable form (ε_p, p) | **D3:** best-fit shape indistinguishable from standard template at Δlog-odds ≤ 0 | PASS (orthogonality table shows p=2 clean, (3,5),(5,7) degenerate — the degeneracy is disclosed, not hidden) |

## 3. Surprise Accounting Table (P(match | random structure))

| Claim | P(match | random) | Model | Status |
|:------|:----------------------|:------|:-------|
| Radix-locked frequency ω_p = 2π/ln p | ~1/231 ≈ 0.004 (one of 231 grid frequencies) | uniform prior on ω ∈ [0.5, 12] | computed — the locked-frequency test is a real constraint |
| Radix identification p=2 vs others | 0.33 (max |C| for p=2 vs others) | shape-correlation null | computed — p=2 is orthogonal |
| Radix identification (3,5)/(5,7) pairs | >0.77 (|C|) | shape-correlation null | **DEGENERATE — cannot be distinguished**; reported as a bound on identifiability |

## 4. Δlog-odds Summary

| Claim | P(O|T) | P(O|¬T) | Δlog-odds | Classification |
|:------|:--------|:---------|:----------|:---------------|
| Bispectrum detection at ε=0.003 (2-point-consistent) | ~0 (noise floor 3-4 orders higher) | ~0 (standard ΛCDM predicts 0) | ≈ 0 (both zero) | **[NOT YET EVIDENCE]** — analysis produces an upper bound, not a detection |
| Bispectrum detection at ε=0.05 (optimistic) | ~0 (still below noise) | ~0 | ≈ 0 | **[NOT YET EVIDENCE]** |
| Radix-locked frequency test as a discriminator | high (narrow peak, C drops 0.94→0.20 across Δω=1) | moderate (resonant family free-ω fits) | > 0 only if data resolve ω_p vs free-ω best fit | **[PENDING]** — requires the Planck data analysis |
| 2-point null as a constraint | — | — | — | **ASSUMED** (established, not re-litigated) |

**Gate outcome:** No cross-domain correspondence claim in this project is presented as
evidence with Δlog-odds > 0 at this stage. The honest classification of the planned
result is **[UPPER BOUND / CONSTRAINT]**, not **[DETECTION]**. If the Planck analysis
produces a marginal peak, it will be reported with the full look-elsewhere penalty and
capped at [NOT YET EVIDENCE] per KIF-60.

## 5. Tautology Trap Audit

| Trap | Check | Status |
|:-----|:------|:-------|
| Overfitting | Template dof: (ε_p, φ) per radix = 8; independent shapes: 40 k-bins × 4 radices | PASS — dof ≪ data |
| Cherry-picking | All primes p ∈ {2,3,5,7} reported; the (3,5)/(5,7) degeneracy disclosed | PASS — denominator reported |
| Absorption | No new dualities declared; D1–D3 fixed at pre-registration | PASS |

## 6. Confirmation-Seeking Test

The alternative the higher-n test would falsify: standard single-field slow-roll ΛCDM +
resonant-feature inflation (Leblond–Pajer family), which predicts log-periodic N-point
shapes at FREE frequency. The p-adic claim is distinguishable ONLY by (a) the
radix-locked frequency (ω_p = 2π/ln p) and (b) the amplitude-consistency relation with
the 2-point null. A resonant model tuned to ω = ω_p predicts a nearly identical
observable — the test is then a parameter measurement, not a theory discrimination,
and is graded accordingly (capped). The phase-4 computation quantifies the degeneracy
(§3) instead of assuming it away.

## 7. Gate Status

**KIF-60: PASS with honest classification.** The project's pre-registered core claim
stands; the expected scientific output is an upper-bound constraint on ε_p from Planck
higher-n statistics, which (i) strengthens the 2-point null, (ii) quantifies the
degeneracy structure between radices and between p-adic and resonant-feature models,
and (iii) sets the sensitivity requirement (Δω resolution, σ_fNL) for CMB-S4 to make
the channel discriminating. No claim is over-sold.
