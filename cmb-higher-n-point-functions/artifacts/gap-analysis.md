# Gap Analysis — QNFO.UMP.007 (CMB Higher n-Point Functions)

**Date:** 2026-08-12 · **Phase:** P1 (Gap Analysis)

---

## 1. What is already covered (do not re-do)

| Coverage | Where | Evidence |
|:---------|:------|:---------|
| p-adic log-periodic prediction, 2-point form | `log-periodic-oscillations-in-the-cmb` (proposal, 2026-04) | DOI 10.5281/zenodo.19555030 |
| 2-point test against Planck 2018 (null / constrained) | `cmb-ultrametric-signatures` (2026-07-05) + CAL-03 + RQ-002 registry | DOI 10.5281/zenodo.21205104; A_LPO < 0.003 (95% CL); log Bayes −5.14..−6.54 |
| Search protocol design (log-resample, Lomb-Scargle, significance) | proposal §3 | DOI 10.5281/zenodo.19555030 |
| D=4 ultrametric special case / CMB scale mapping | `cmb-ultrametric-signatures` §1 | DOI 10.5281/zenodo.21205104 |
| External p-adic cosmology program | Djordjević et al. 2002; Dragović 2022 | 10.1016/s0920-5632(01)01613-9; 10.3390/sym14010073 |

## 2. What prior work to build on (foundations)

1. **The 2-point null** (A_LPO < 0.003, 95% CL) — the established constraint; RQ-013 extends to higher-n.
2. **OSF pre-registration `2ndsz`** — the methodological anchor; this project operationalizes it.
3. **Resonant-features template library** (Leblond–Pajer 2011) — the degeneracy-control toolbox; build the shape-orthogonality argument against it.
4. **Ultrametric tree structure in cosmology** (Harlow–Shenker–Stanford 2012) — structural precedent.
5. **p-adic CFT / bulk dual** (Ebert et al. 2019) — theoretical complement for interpretation.

## 3. Is the proposed research genuinely novel? — Assessment

**The specific claim is novel and falsifiable:** no external publication tests p-adic
log-periodic signatures in CMB *higher-order* correlators (verified: OpenAlex 0 direct,
Zenodo 0, EuropePMC 0, arXiv conjunction 0). The RQ-013 question is open.

**The novelty is bounded by degeneracy risk:** the *observable* (log-periodic modulation
of the bispectrum) overlaps the resonant-features inflation literature. The novelty
claim must therefore be framed as: "the first *p-adic-cosmology-derived* template for
higher-n CMB statistics, with an explicit orthogonality argument against standard
resonant shapes" — not "the first log-periodic bispectrum template" (that is Leblond–Pajer).

## 4. Gap matrix

| Gap | Status | Action |
|:----|:-------|:-------|
| G-1 p-adic bispectrum/trispectrum shape derivation | OPEN | P4: derive the p-adic log-periodic non-Gaussian template; closed form where possible |
| G-2 Orthogonality vs resonant features | OPEN (critical) | P4: shape-overlap computation vs Leblond–Pajer / Barnaby–Cline templates; BP-3 density control |
| G-3 Planck 2018 higher-n data access | PARTIAL | P4: public COM_CompMap / Planck legacy products; bispectrum estimator results from Planck 2018 NG papers |
| G-4 Quantitative amplitude prediction | OPEN (was CAL-03 blocker) | P4: derive ε_p amplitude from the ultrametric framework (the CAL-03 "not falsifiable without amplitude" gap) |
| G-5 Synthetic-signal injection pipeline | OPEN | P4: inject p-adic template into simulations, recover with estimator, quantify sensitivity |
| G-6 Internal detection-claim hygiene | OPEN | P5: publish the null-vs-detection framing per §1.3 of due-diligence.md; never propagate v0.1.1 3σ claim as established |

## 5. Consilience-domain selection (feeds KIF-29 gate)

Evidence from Phase 1 selects these domains (dynamic selection per research v2.46):
1. **Cosmology / CMB statistics** — the observable channel (Planck 2018, bispectrum estimators).
2. **Number theory (p-adic / ultrametric analysis)** — the formalism (Ostrowski, valuations, log-periodic modulation).
3. **Inflationary phenomenology / features** — the degeneracy channel (resonant shapes).
4. **Signal processing / spectral analysis** — the method (log-resample, Lomb–Scargle, higher-n estimators).
5. **Information theory** (D=4 ultrametric embedding, hierarchical structure) — the interpretive frame.
