# Phase 1 Due Diligence — QNFO.UMP.013 (pattern-particle-unification)

**Date:** 2026-08-19 · **Gate:** DUE-DILIGENCE-DEPTH-1 · **Status:** COMPLETE

## 1. Corpus statistics (gate step 1)

`query_graph({endpoint:"stats"})` 2026-08-19: **8,303 nodes / 8,462 edges** — Paper 1,642, Note 5,616, Project 153. Evidence: tool result this session.

## 2. Full-corpus sweep (gate step 2: >=3 formulations per topic, limit>=16)

12 query formulations across 4 topics, qnfo-memory-mcp search_papers limit=16 each (VECTORIZE-TOP-K-50-1: limit<=16 reliable). 192 result rows screened.

| Topic | Formulations | Key hits (slug) |
|---|---|---|
| T1 SM statistics/particle table | 3 | spin-statistics-distinction (RES.009), exchange-phase-logical-scalar, configuration-space-topology (RES.011), thermodynamic-genesis-of-the-standard-model, standard-model-critique, higgs-particle-never-existed, geometric-unification-framework, reentrant-distinctions |
| T2 Quasiparticles | 3 | odr-thesis, compton-ontology-bt-coordinates, frequency-valuation-theory, superconductivity-quadrangle, signal-worker-boundary-confinement (INM.001), structural-mediation-of-planckian-dissipation, operationalizing-generalized-symmetries |
| T3 Anyons | 3 | adelic-synthesis-pattern-particle, p-adic-anyon-fusion-braiding, p-adic-braid-groups-bruhat-tits, ultrametric-relaxation-dynamics-in-topological-quantum-memory, beyond-the-qubit, ultrametric-quantum-computation-langlands, zbw-majorana-tqc-p4-zbw-anyon-braiding |
| T4 BT tree / adelic geometry | 3 | adelic-cross-domain-program v5.0, compton-cross-ratios-v2 (v2.3), non-anthropocentric-natural-units-v2, fine-structure-constant-cross-ratio, ballistic-transport-on-the-bruhat-tits-tree, spectral-dynamics-on-bruhat-tits-trees, adelic-core-synthesis, adelic-constraints-on-quantum-field-theory-phase-1, harmonic-ostrowski-re-evaluation |

Adjacent WBS domains covered (gate step 4): **UMP** (primary), **RES** (RES.009 spin-statistics, RES.011 configuration-space-topology), **INM** (INM.001 signal-worker-boundary), **ODR** (odr-thesis), **SLB** (exchange-phase-logical-scalar — re-entrant calculus), **ADL** (adelic-cross-domain lineage). Requirement >=2: satisfied (5 adjacent).

KG walk: query_graph nodes Paper "anyon" → 4 nodes incl. adelic-synthesis-pattern-particle, p-adic-anyon-fusion-braiding, zbw-majorana-tqc-p4, zenodo-18199397 (external: operationalizing-generalized-symmetries). "quasiparticle" KG → 0 nodes (data-quality finding DQ6 below).

## 3. Cross-system ID validation (gate step 3)

`resolve_paper_id` per key hit — slug → Vectorize ID → KG ID → DOI:

| Slug | D1 doi | zenodo_doi | KG node | Status |
|---|---|---|---|---|
| spin-statistics-distinction | 10.5281/zenodo.21964598 | 10.5281/zenodo.21962904 | — | ⚠ DQ1 |
| adelic-synthesis-pattern-particle | 10.5281/zenodo.21208568 | = | ✓ published | ✓ |
| p-adic-anyon-fusion-braiding | 10.5281/zenodo.21208491 | = | ✓ published | ✓ |
| p-adic-braid-groups-bruhat-tits | 10.5281/zenodo.21208366 | = | — | ✓ |
| quasiparticles-as-rational-functions | 10.5281/zenodo.21768757 | 10.5281/zenodo.21778335 | ✗ none | ⚠ DQ2 |
| compton-ontology-bt-coordinates | 10.5281/zenodo.21758752 | null | — | ⚠ DQ3 |
| compton-cross-ratios-v2 | 10.5281/zenodo.21485556 | = | — | ✓ |
| adelic-cross-domain-program | 10.5281/zenodo.21965332 | 10.5281/zenodo.21698355 | — | ✓ |
| exchange-phase-logical-scalar | 10.5281/zenodo.21964104 | 10.5281/zenodo.21964359 | — | ✓ (concept 21941184 in body) |
| configuration-space-topology | 10.5281/zenodo.21962450 | 10.5281/zenodo.21957291 | ✓ RES.011 complete | ✓ |
| thermodynamic-genesis-of-the-standard-model | null | null | — | ⚠ DQ4 |
| signal-worker-boundary-confinement | 10.5281/zenodo.21974194 | = | — | ⚠ DQ5 |

**Data-quality findings (not footnotes):**
- **DQ1** spin-statistics-distinction: D1 doi (21964598, v1.6) vs zenodo_doi (21962904, v1.x). Multi-version record; cite concept DOI in UMP.013.
- **DQ2** quasiparticles-as-rational-functions: D1 doi 21768757 is a v1 record; **verified live**: v2.0 = 10.5281/zenodo.21784490, concept = 10.5281/zenodo.21768756 (evidence: artifacts/external-search/zenodo_qp_21784490.json). UMP.013 cites the CONCEPT DOI 21768756.
- **DQ3** compton-ontology-bt-coordinates: r2_key `releases/2026/08/...` — WRONG-BUCKET-SELECTION-1 class (canonical bucket is qnfo-releases). Historical; not ours; log-only.
- **DQ4** thermodynamic-genesis-of-the-standard-model: no DOI in D1; r2_key uses deprecated `qnfo/releases` bucket.
- **DQ5** signal-worker-boundary-confinement: identifier field holds a DIFFERENT version's DOI (21931224 vs record 21974194).
- **DQ6** quasiparticles-as-rational-functions has NO KG node and is NOT Vectorize-indexed (memory mem-mB650REOZPAA: body-no-slug exclusion). Corpus-internal discovery requires D1 fallback — this is why the paper was found via D1 lookup, not semantic search.

## 4. External independent verification (gate step 5)

Evidence files in `artifacts/external-search/`. Every claim below cites its file.

| Claim (ingredient) | Source | Verification | Evidence file |
|---|---|---|---|
| Spin-statistics derivation from Lorentz invariance (Weinberg) | Phys. Rev. 133, B1318 (1964) | Crossref: 10.1103/physrev.133.b1318, Weinberg, 1964 ✓ | crossref_weinberg.json |
| BCS theory of superconductivity | Phys. Rev. 108, 1175 (1957) | Crossref: 10.1103/physrev.108.1175, Bardeen, 1957 ✓ | crossref_bcs.json |
| Fractional QHE, Laughlin incompressible fluid | PRL 50, 1395 (1983) | Crossref: 10.1103/physrevlett.50.1395, Laughlin, 1983 ✓ | crossref_laughlin.json |
| p-adic analysis and mathematical physics (BT trees in physics) | Vladimirov–Volovich–Zelenov 1994 | Crossref: 10.1142/1581, 1994 ✓ | crossref_vladimirov.json |
| Non-abelian (Pfaffian/Moore–Read) statistics | Nucl. Phys. B 360, 362 (1991); arXiv hep-th/9202001 | arXiv live ✓ — matrix-valued statistics exist | (arXiv MCP result, session log) |
| External BT-building physics | Gubser et al., "Holographic Codes on Bruhat–Tits buildings…" (2018) | OpenAlex: 10.48550/arxiv.1801.09623 ✓ | openalex_padic_anyons.json |
| External novelty sweep "p-adic anyons Bruhat-Tits" | — | Top hits are QNFO Zenodo records (21208366/70); no external unification competitor | openalex_padic_anyons.json |
| External novelty sweep "ultrametric condensed matter unification" | — | No direct competitor found | openalex_ultrametric_cm.json |
| QP v2.0 version chain | Zenodo | 21784490 = v2.0, concept 21768756 ✓ | zenodo_qp_21784490.json |

archive.org CDX + Google Patents: NOT applicable this phase — the core claim makes no web-date or "patented" claims (conditional N/A documented per gate).

## 5. Confirmation-bias disclosure (KIF-17 / Vectorize disclosure)

`[CONFIRMATION-BIAS-RISK]` — the corpus sweep is overwhelmingly QNFO-internal (the QNFO program IS the main producer of p-adic/BT-tree physics). External corroboration exists only at the INGREDIENT level (Weinberg, BCS, Laughlin, Moore–Read, Gubser, Vladimirov) — each imported premise is externally anchored, but the UNIFICATION claim itself has no external prior. Novelty is therefore real but untested: no external framework proposes the two-catalog pattern table.

## 6. Gap analysis — what is covered vs what is new

**Covered by prior QNFO work (import, do not re-derive):**
- Statistics scalar R = e^{2πis}, boson/fermion as 3D shadow — RES.009 (21964598 concept lineage) + exchange-phase-logical-scalar (21964104): R = (e^{iπ})^{2s}, the half-turn reading. [This is premise 3.]
- Anyons as p-adic braid phases / quantum groups at roots of unity — adelic-synthesis-pattern-particle (21208568), p-adic-anyon-fusion-braiding (21208491), p-adic-braid-groups-bruhat-tits (21208366). [Premise 5.]
- Quasiparticles as rational functions N_C*(α) — QP v2.0 (concept 21768756). [Premise 4.]
- Compton count ontology on BT tree — ODR (21780909) + compton-ontology-bt-coordinates (21758752). [Premise 1.]
- SM mass spectrum on BT trees — adelic-cross-domain-program v5.0 (21965332), compton-cross-ratios-v2 (21485556). [Premise 2's empirical anchor.]

**Genuinely new in UMP.013:**
1. The unified PATTERN TABLE: both catalogs (SM fermions + bosons; quasiparticles + anyons) assembled as labeled tree patterns in ONE table with a uniform address scheme (place, branch, node class, N_C*, statistics phase).
2. The REGIME DICTIONARY: which tree structure (unramified vs ramified, place choice, composition depth) corresponds to which physical regime, with per-entry conditions.
3. Falsifiability conditions F1–F4 spanning BOTH catalogs (prior work's falsifiability conditions are per-paper, single-regime).

**Records that COMPLICATE or CONTRADICT (mandatory surfacing):**
- **C1 (from UIA A3):** BCS gap Δ ~ exp(−1/N(0)V) (10.1103/physrev.108.1175) is non-analytic, and heavy-fermion quasiparticle masses m* ∝ 1/T_K with T_K ~ exp(−1/Jρ) are EXPONENTIAL in coupling — the "rational function" premise (QP v2.0) must be scoped: it holds for weakly-interacting/band composites; strongly-correlated exponential scales are outside it. UMP.013 will scope the premise accordingly, NOT absorb the counterexample.
- **C2 (from UIA A4, externally verified):** Moore–Read non-abelian statistics (hep-th/9202001) are MATRIX-valued, not phase-valued — "root of unity" covers ABELIAN anyons only. UMP.013 scopes the anyon clause to abelian anyons and records the non-abelian extension as an open question (fusion multiplicities, UMTC), not as solved.
- **C3 (from UIA A5):** Weinberg (10.1103/physrev.133.b1318) makes ±1 FORCED in 3+1D by Lorentz invariance + microcausality — the tree reading of boson/fermion is explanatory, not predictive, in 3+1D. The paper must state what the tree adds beyond the forced result (the unified two-catalog table + the 2D interpolation), and must not claim to "derive" spin-statistics.

**Novelty bound:** the paper is a structural synthesis with three novel deliverables (table, dictionary, cross-catalog falsifiability); it claims NO new dynamics. Value ceiling per UIA A6: consilient/classification-grade until a measurement that REQUIRES the tree is found — the abstract must not overclaim.

## 7. SO-WHAT and premise-depth

Covered by PROJECT-PLAN.md §"Why a reader should care" and §"Premise-depth disclosure" (committed at Phase 0). Gap analysis confirms: premises end at the five named imports; derived content is the table + dictionary + falsifiability conditions.

## 8. Evidence discipline

Every count and DOI above cites an evidence file in artifacts/external-search/ or a same-session tool result. No count without evidence.
