# Due Diligence Report — QNFO.UMP.007 (CMB Higher n-Point Functions)

**Date:** 2026-08-12 · **Phase:** P1 (Due Diligence — QNFO Cross-Reference)

---

## 1. QNFO Cross-Reference: Found N related papers

### 1.1 Ecosystem state (query_graph stats)
- 8,257 nodes / 8,394 edges; 1,611 Paper nodes; 144 Project nodes; 15 Program nodes; 49 ResearchQuestions.

### 1.2 Directly related QNFO publications

| Slug | Title | DOI | Status | Relevance |
|:-----|:------|:----|:-------|:----------|
| `log-periodic-oscillations-in-the-cmb` | Log-Periodic Oscillations in the CMB (proposal) | 10.5281/zenodo.19555030 | published (2026-04-13) | The original prediction: `C_l(l+1) = A(l/l0)^{1-ns}[1 + B cos(2π/ln q · ln(l/l0) + φ)]`; 3-step search protocol; falsification criterion. |
| `cmb-ultrametric-signatures-an-empirical-probe-of-hierarchical-cosmology` | CMB Ultrametric Signatures: An Empirical Probe of Hierarchical Cosmology | 10.5281/zenodo.21205104 | published (2026-07-05) | The 2-point null analysis (v0.1.1). **CRITICAL TENSION:** v0.1.1 claims 3σ p=2 detection; later calibration (CAL-03) + Disconfirming Registry + RQ-002 registry refine this to a NULL (see §1.3). |

### 1.3 The 2-point null — state reconciliation (IMPORTANT)

The project builds on the **null**, not on the v0.1.1 3σ claim. Verified sources:

| Source | Statement | Evidence |
|:-------|:----------|:---------|
| RQ-002 KG registry | "CMB Planck 2018: No Log-Periodic Oscillations"; `A_LPO < 0.003` at 95% CL for all p; "Higher-order n-point functions not yet tested" | KG node `rq-002-cmb-log-periodic` |
| Disconfirming Registry (memory) | "CMB Planck 2018: no log-periodic oscillations at >0.3% amplitude" | mem-heuristic-1784264832913 |
| CAL-03 calibration | log-periodogram INCONCLUSIVE — best-fit λ=2.05, p=0.43 not significant; Planck 2018 limits \|A\| < 0.02–0.03 at 2σ; **needs quantitative amplitude prediction before falsifiable** | mem-task_outcome-1785011027802 |
| CAL-03B | log Bayes factors −5.14 to −6.54 for the 2-point LPO model | mem-project_fact-1784561726488 |

**Consequence for QNFO.UMP.007:** the paper MUST (a) cite the 2-point null as the established constraint; (b) NOT propagate the v0.1.1 3σ detection claim as established; (c) state the higher-n search as a genuinely open channel (RQ-013), consistent with the RQ-002 registry note.

### 1.4 Existing pre-registration (STRONG asset)

**OSF Pre-registration `2ndsz`** — "CMB Higher n-Point p-Adic Signature Search" (RQ-013), submitted 2026-07-20, subject taxonomy Physical Sciences → Astrophysics → Cosmology, 16+ schema fields populated. OpenAlex-indexed: DOI 10.17605/osf.io/2ndsz. Related populated drafts: R2-LSS DSI, R3-GW DSI.

### 1.5 QNFO program context
- Research WBS Master v1.0: R11 = CMB research tier (T3 medium-term after T1/T2 critical path).
- Post-Grand-Synthesis priorities: "RQ-002 CMB oscillations" listed in T3 (prove/withdraw) — this project directly serves that item by extending to higher-n.
- Related program papers: `measure-theoretic-artifacts-archimedean-place` (Adelic Restructuring), `unity-of-ultrametric-physics`, `syntactic-token-calculus-research-plan` (STC, source of the original LPO prediction), `conditional-state-distances-pw-clocks` (ultrametric emergence).

### 1.6 Vectorize search results
- `search_papers("CMB higher-order correlation functions bispectrum trispectrum p-adic...")` → top hits: `scale-invariant-physics`, `log-periodic-oscillations-in-the-cmb`, `syntactic-token-calculus-research-plan`, `computational-toolkit-for-p-adic-spacetime`, `non-archimedean-syntactic-paradigm-for-physics`.
- **`[CONFIRMATION-BIAS-RISK]` flag:** ALL top hits are QNFO-internal. External corroboration must come from Phase 1b (OpenAlex/Crossref/arXiv) — which it does (§2). The internal corpus alone would be a confirmation-bias trap; this report therefore weights external sources for novelty claims.

---

## 2. External Literature (Phase 1b evidence — files in `artifacts/external-search/`)

| Source | Query | Count | Evidence file |
|:-------|:------|:------|:--------------|
| OpenAlex | `"p-adic" AND (CMB) AND (bispectrum OR trispectrum OR non-Gaussianity)` | 15 | openalex_padic_cmb.json |
| OpenAlex | `ultrametric p-adic cosmology` | 15 | openalex_ultrametric_cosmology.json |
| Crossref | `p-adic CMB bispectrum ultrametric` | 10 | crossref_padic_cmb.json |
| Zenodo | `"p-adic" AND "bispectrum"` | 0 | zenodo_padic_bispectrum.json |
| Europe PMC | `"p-adic" AND CMB AND bispectrum` | 0 | europepmc_padic_cmb.json |
| arXiv | `all:"p-adic" AND all:"CMB" AND (bispectrum OR non-Gaussianity)` | 0 | arxiv_padic_cmb.xml |
| arXiv | `all:"log-periodic" AND all:"CMB"` | 1 | arxiv_logperiodic_cmb.xml |
| QNFO Vectorize | internal cross-ref | 8 | (this report §1.6) |
| QNFO KG | internal cross-ref | 4 Paper nodes | (this report §1.2) |

### 2.1 Key external papers (degeneracy channel — KIF-18 constraining evidence)

| Paper | Year | DOI | Relevance |
|:------|:-----|:----|:----------|
| Barnaby & Cline, *Large non-Gaussianity from non-local inflation* | 2007 | 10.1088/1475-7516/2007/07/017 | Non-local (non-Archimedean-flavored) inflation produces large NG; shape overlap with p-adic predictions must be quantified. |
| Barnaby & Cline, *Predictions for non-Gaussianity from non-local inflation* | 2008 | 10.1088/1475-7516/2008/06/030 | Concrete f_NL predictions for non-local inflation. |
| Barnaby, *Features and non-Gaussianity from inflationary particle production* | 2010 | 10.1103/physrevd.82.106009 | Particle-production features generate oscillatory bispectrum signatures. |
| **Leblond & Pajer, *Resonant trispectrum and a dozen more primordial N-point functions*** | 2011 | 10.1088/1475-7516/2011/01/035 | **THE degenerate template library** — resonant (log-periodic-like) N-point functions already derived in standard inflation features. Direct overlap risk with p-adic log-periodic trispectrum. |
| Koshelev, Kumar, Mazumdar, *Non-Gaussianities... non-local R2-like inflation* | 2020 | 10.1007/jhep06(2020)152 | Modern non-local inflation NG predictions. |
| Harlow, Shenker, Stanford, *Tree-like structure of eternal inflation* | 2012 | 10.1103/physrevd.85.063516 | Ultrametric tree structure in eternal inflation — closest external structural analogue. |
| Djordjević, Dragović, Nešić, *p-Adic quantum cosmology* | 2002 | 10.1016/s0920-5632(01)01613-9 | External p-adic cosmology program. |
| Dragović, *A p-Adic Matter in a Closed Universe* | 2022 | 10.3390/sym14010073 | External p-adic matter cosmology. |
| Ebert, Sun, Zhang, *Probing holography in p-adic CFT* | 2019 | 10.48550/arxiv.1911.06313 | p-adic CFT (bulk dual) — theoretical complement. |
| *One Feature, Three Clocks* (arXiv log-periodic CMB hit) | 2026 | — | Phase-locked GW/PBH/NG from a feature — external log-periodic-NG connection. |

### 2.2 Honest assessment (P3.SOURCE-DISCIPLINE / thin-results honesty)
- **Direct overlap search is genuinely empty:** no external paper directly tests "p-adic log-periodic signatures in CMB bispectrum/trispectrum." The RQ-013 channel is open in the literature.
- **BUT the degenerate channel is crowded:** standard inflationary feature/resonance models (Leblond–Pajer, Barnaby–Cline) already predict log-periodic-like non-Gaussian shapes. A p-adic bispectrum detection would be **degenerate** with resonant-features models unless a shape-orthogonality argument is provided. This is the paper's central methodological challenge and its main falsifiability risk.
- Zenodo/EuropePMC/arXiv-direct returned 0/0/0 — consistent with a genuinely uncovered niche, not with an indexing failure (OpenAlex found 15 works on the same query; the arXiv query with 0 hits was narrowed by the p-adic+CMB+NG conjunction).

---

## 3. Sources-received / sources-cited (three-count audit)

- Queries sent: 9 (2 OpenAlex, Crossref, Zenodo, EuropePMC, 2 arXiv, Vectorize, KG)
- Sources received: 8 sources returned ≥1 hit; 2 returned 0 (Zenodo, EuropePMC)
- Sources cited in this report: all 8 (6 external with evidence files + Vectorize + KG)
- **cited ≤ received: TRUE** — no fabrication risk.
