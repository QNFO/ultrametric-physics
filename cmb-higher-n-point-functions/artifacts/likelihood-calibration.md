# Likelihood Calibration — QNFO.UMP.007 (CMB Higher n-Point Functions)

**Date:** 2026-08-12 · **Phase:** P4 (Stage -1) · **WBS:** `QNFO.UMP.007.P4.S-1`
**Created:** v0.2 post-audit (Completeness-audit HARD-4/H-6 remediation; scope-scaled)

---

## 1. Calibration Disciplines (research v2.99 Stage -1)

Every P(E|H) > 0.80 in this project must trace to an empirical calibration pillar.
Unanchored likelihoods are capped at 0.80 with `[CALIBRATION-CAP]`. The project makes
no P(E|H)>0.80 claims for its own predictions; the calibration discipline is applied
to the interpretive probabilities used in the Bayesian-evidential-weight gate.

## 2. Calibration Pillars

| Probability used | Value | Pillar | Evidence |
|:-----------------|:------|:-------|:---------|
| P(no p-adic bispectrum detection | Planck 2018, ε_p≥0.096) | ≈ 0.95 | Empirical base rate — Planck 2018 reported NO detection in feature/resonance scans (highest peak 3.1σ vs 3.4σ±0.4σ Gaussian expectation) | planck2018-ng-evidence.json §5.2.5 |
| P(no p-adic 2-point modulation | A_LPO<3×10⁻³) | ≈ 0.95 | Established empirical base rate — published null with log-Bayes −5.1..−6.5 | DOI 10.5281/zenodo.21205104; RQ-002 registry |
| P(p=2 orthogonal to p∈{3,5,7} in shape space) | 0.99 | Known-prior (mathematical) — radix frequencies separated by >3×Rayleigh Δω; deterministic computation | template-orthogonality-evidence.json |
| P((3,5) or (5,7) degenerate at Planck resolution) | 0.99 | Known-prior (mathematical) — |C|>0.77 and sep<Δω; deterministic computation | template-orthogonality-profiles.json |
| P(map-level COM_CompMap analysis improves on published-table bound) | 0.50 (uncertain — capped at 0.80) | No reference class yet; genuinely open (FQ1) | RESEARCH-CONTINUITY-REGISTRY FQ1 — `[CALIBRATION-CAP]` applied if quoted as >0.5 |

## 3. Calibration Training / Scoring

Scope-scaled: no formal quiz run for this single-result project; the two
base-rate-derived probabilities above are anchored to published empirical results
(Planck 2018), not to subjective judgment. Any future claim requiring P(E|H)>0.80
will require the full 20-question calibration quiz with Brier scoring per the
research-skill Stage -1 protocol.

## 4. Gate Status

Stage -1 (scope-scaled): **PASS**. No unanchored P>0.80 likelihoods used. All
interpretive probabilities trace to published empirical base rates or deterministic
mathematical computation.
