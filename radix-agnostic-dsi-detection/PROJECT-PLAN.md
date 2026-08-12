# WBS: QNFO.UMP.008

# Radix-Agnostic Detection of Discrete Scale Invariance

**Charter:** A methodology paper establishing a certified, radix-agnostic detector for discrete scale invariance (DSI) — log-periodic structure whose scaling radix is unknown and must not be assumed — with a definitive null application to the Planck 2018 CMB temperature spectrum.

**Author:** Rowan Brad Quni-Gudzinas | **Date:** 2026-08-12 | **Status:** Phase 0 init

---

## 1. Core Claims (locked 2026-08-12 — see docs/core-claim.md)

- **C1:** In log-coordinate $u=\ln x$, DSI under $x\to\lambda x$ becomes periodicity with $\omega_0 = 2\pi/\ln\lambda$. The radix is the inverse logarithm of a measured log-frequency.
- **C2:** A three-stage protocol — (1) detrend + spectral peak (FFT or Lomb-Scargle), (2) bounded sinusoid refinement on residuals, (3) candidate-radix hypothesis test — recovers a **non-prime** radix $\lambda=1.62$ to $\le 0.02\%$ error on synthetic data (verified seeds 42/12345/7).
- **C3:** Certification is mandatory: bootstrap null (max-statistic p, already multiplicity-corrected) + ΔBIC likelihood ratio + integrity gates (G1 resolvability $\omega\ge 2\pi/u_{\rm span}$, G2 amplitude SNR ≥ 1, G3 $\sigma_\lambda/\lambda<10\%$). A DSI claim is certified only if bootstrap p<0.05 AND ΔBIC>10 AND gates_pass==3.
- **D1:** Application to the Planck 2018 unbinned TT spectrum (ℓ≥30) yields **no certified DSI at any resolvable radix** — including the p-adic radices λ∈{2,3,5,7} (probed at 0.078 rad resolution, power_frac 0.0002–0.0005) — consistent with the radix-locked nulls (CAL-03 global p=0.38; P5 p-adic p=0.38).
- **D2:** The G4 model-subtraction protocol (scan $\log y - \log y_{\rm model}$ residuals, not raw spectra) is mandatory for non-power-law data: raw-spectrum scanning produces a self-refuting low-frequency artifact (λ≈10⁴–10⁵, σ_λ/λ=985%, SNR=0.15) that the integrity gates correctly reject.
- **D3:** The full joint LPPL fit is unreliable for radix discovery — it collapses even when initialized at the true FFT peak (λ→10⁹); stage separation (detrend → peak → bounded refinement) is required.

## 2. Phases with WBS

| Phase | WBS | Deliverable | Gate |
|---|---|---|---|
| P0 Init | QNFO.UMP.008.P0 | Branch, PROJECT-PLAN, core-claim lock, README, commit/tag/push | HARD |
| P1 Due Diligence | QNFO.UMP.008.P1 | KG+Vectorize+D1 cross-ref, 8-source external search, gap analysis, KIF-29 consilience + KIF-60 | HARD |
| P2 Literature | QNFO.UMP.008.P2 | 8-source triage, KIF-18 Mandatory Symmetry | HARD |
| P3 Citations | QNFO.UMP.008.P3 | BibTeX live-verified (P3.AUTHOR-GATE) | HARD |
| P4 Research | QNFO.UMP.008.P4 | Full derivation + synthetic verification matrix + real-data application + red-team | HARD |
| P5 Publication | QNFO.UMP.008.P5 | `<slug>.md` + CDP PDF + Publication Language Gate + Zenodo DOI | HARD |
| P6 Deployment | QNFO.UMP.008.P6 | D1 living-paper, papers-server, KG node, Vectorize index | HARD |
| P7 Dissemination | QNFO.UMP.008.P7 | Buffer social, Internet Archive, SEO (NO journal submission — user directive) | SOFT |
| P8 Distribution | QNFO.UMP.008.P8 | GitHub tag, Zenodo newversion, R2 archive, Consolidated Closeout | HARD |

## 3. Milestones with Gate Criteria

| Milestone | Criterion |
|---|---|
| M1 Phase 0 committed | Branch pushed, tag v0.1-phase0-ump008, `git ls-remote` verified |
| M2 Phase 1 complete | `artifacts/consilience-gate.md` + `artifacts/bayesian-evidential-weight.md` present |
| M3 Phase 4 complete | `artifacts/fit-verify.txt` + synthetic matrix + real-data evidence files |
| M4 Published | DOI resolves, P5.FRESH ok, D1+KG+Vectorize verified |

## 4. Deliverable Registry

| # | Deliverable | Location | Status |
|---|---|---|---|
| 1 | PROJECT-PLAN.md | `radix-agnostic-dsi-detection/PROJECT-PLAN.md` | DONE (P0) |
| 2 | docs/core-claim.md | `docs/core-claim.md` | DONE (P0) |
| 3 | README.md | `README.md` | DONE (P0) |
| 4 | Detector script (source) | research skill `dsi-radix-detector.py` (committed a9db635→ca6a965, QNFO/qnfo-skills) | EXISTING |
| 5 | Methodology notes | Obsidian `_26224105000.md`, `_26224105300.md` | EXISTING |
| 6 | consilience-gate.md | `artifacts/` | PENDING (P1b) |
| 7 | bayesian-evidential-weight.md | `artifacts/` | PENDING (P1b) |
| 8 | fit-verify.txt | `artifacts/` | PENDING (P4) |
| 9 | `<slug>.md/.pdf/.html` | `releases/` | PENDING (P5) |

## 5. Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| arXiv rate-limit / no endorsement | HIGH | Medium | OpenAlex PRIMARY (verified 2026-08-12) |
| Reviewer subagent truncation | HIGH | Low | Mandate 3 direct-audit fallback |
| Concurrent SKILL.md writes | MED | Low | CONCURRENT-SKILL-WRITE-1 protocol |
| Records-API metadata drops | MED | Med | Deposit-API shape (ZENODO-RECORDS-API-DROPS-METADATA-1) |

## 6. Success Criteria

1. Certified radix-agnostic DSI detection methodology published with reproducibility evidence.
2. Definitive null on Planck 2018 (D1) — strengthens the p-adic program's honest-negative record.
3. Tool hardened: `dsi-radix-detector.py --data in.csv --model modelcol` enforces certification by default.
