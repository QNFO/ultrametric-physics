# Phase 1 Due Diligence — QNFO.UMP.011 (2026-08-17)

Project: Conditional Truths and the Locale Framework (slug conditional-truths-locale-framework)
Gate: DUE-DILIGENCE-DEPTH-1 (HARD). Evidence: `artifacts/external-search/corpus-sweep-evidence.json` + `external-verification.json`.

## 1. Corpus scale and channels

- KG stats (live 2026-08-17): 8,293 nodes / 8,443 edges / **1,633 Paper** nodes / 152 Project nodes.
- D1 living-paper: **997 papers**, FTS5-indexed (title+abstract).
- Channels used: D1 `papers_fts` (2-step rowid lookup; 16 formulations across 4 topics, LIMIT 20) + KG node search + KG neighbor walks + `search_memories` + `recall_facts` + `resolve_paper_id` + external (Zenodo/Crossref/OpenAlex/arXiv).
- **Channel outage (FIND-1):** Vectorize-backed `search_papers`/`search_papers_enriched` (qnfo-memory-mcp.q08.workers.dev) threw Worker Error 1101 on 7/7 calls this turn — compensated with D1 FTS + KG + memory. Evidence in corpus-sweep-evidence.json.

## 2. Full-corpus sweep results (16 formulations, 4 topics)

| Topic | Formulations | Hits (LIMIT 20) | Verdict |
|:------|:--------------|:----------------|:--------|
| T1 conditional/locale/EFT | conditional(6), locale(0), "effective field theory"(0), applicability(0) | 6 | NOT covered as a doctrine in corpus abstracts |
| T2 Monna/ultrametric/p-adic/perspective | monna(4), ultrametric(20+), "p-adic"(20+), perspective(3) | 47+ | WELL covered (UMP core) |
| T3 structural realism/map-territory/spin/ontology | 1 / 1 / 14 / 20+ | 36+ | Partial |
| T4 Ostrowski/completion/temperature/frequency | 20+ / 12 / 5 / 11 | 48+ | WELL covered (C4 heavily prior-arted) |

Key corpus records (cross-system validated):

| Slug | DOI | Relevance |
|:-----|:----|:----------|
| non-archimedean-projective-perspective (UMP.010) | 10.5281/zenodo.21979032 (v0.3, 2026-08-17; concept 21969603) | DIRECT ancestor — visual Monna-map underdetermination |
| s10-observer | 10.5281/zenodo.21473899 | Observer self-location in ultrametric structure (C3 adjacent) |
| non-anthropocentric-natural-units | 10.5281/zenodo.21480756 | C4 overlap — Bekenstein→Ostrowski unit derivation |
| ostrowski-dimensionless-reformulation | 10.5281/zenodo.21756190 | C4 overlap — Planck-unit compilation |
| consilience-physics-number-theory | 10.5281/zenodo.21590155 | C4 overlap — Ostrowski consilience |
| measure-theoretic-artifacts-archimedean-place (+v2.0) | 10.5281/zenodo.21595214 / 21601112 | C4 overlap — Archimedean-place artifacts |
| universal-ignorance-audit | 10.5281/zenodo.21901984 (canonical v0.3) | map-territory hygiene instrument (C2 method) |
| measurable-vs-imaginable | 10.5281/zenodo.21645350 | computable-real boundary (complicates C4) |
| electron-hook-treatise | 10.5281/zenodo.21975507 | load-bearing-assumptions critique (same critical method) |
| 29-schism-synthesis | 10.5281/zenodo.21458373 | schism catalogue (C1 adjacent) |
| embodied-mathematics-lakoff-nunez | 10.5281/zenodo.21440894 | embodiment/map perspective (C2 adjacent) |
| monna-map-generation-and-hallucination | R2 qnfo/releases/2026/04 (no DOI) | Monna map in generation/hallucination |
| universe-category-functor | 10.5281/zenodo.21880064 | structural realism in corpus (C2 adjacent) |
| conditional-state-distances-pw-clocks | 10.5281/zenodo.21120286 | "when does ultrametricity emerge" (C3/C4 adjacent) |

## 3. Cross-system ID validation (resolve_paper_id per hit)

Validated 8 hits. **Mismatches flagged (data-quality findings, not footnotes):**
- FIND-2 (SOFT): `ostrowski-dimensionless-reformulation` KG node properties carry `doi: 10.5281/zenodo.21751722` (v1) while D1 papers carries 21756190. KG node stale.
- FIND-3 (SOFT): UMP.010 D1 papers row now carries `doi: 10.5281/zenodo.21979032` (v0.3, published 2026-08-17, `version: null` — LEGACY-PUT-VERSION-OMISSION-1 pattern) while D1 program_registry row still says v0.2/21969784. Registry row stale (concurrent session published v0.3 today).
- FIND-4 (INFO): D1 FTS5 `JOIN papers p ON p.rowid = f.rowid` returns EMPTY (no error) despite content_rowid='rowid'; two-step rowid lookup required. Kaizen candidate.

## 4. Taxonomy breadth (>=2 adjacent WBS domains — satisfied)

- **UMP** (primary): Monna/ultrametric/adelic records above.
- **RES** (adjacent): universal-ignorance-audit, electron-hook-treatise, measurable-vs-imaginable, 29-schism-synthesis, measurement-stratigraphy.
- **SLB** (adjacent, via memory): Laws-of-Form Number Builder (memory mem-1785346052270) — Monna-map projection as step 6 of the LoF number construction ("lossy: creates non-computable reals that have no discrete counterpart; projection artifacts") — complicates AND supports C4.
Records that CONTRADICT/COMPLICATE (surfaced, not suppressed): non-anthropocentric-natural-units and ostrowski-dimensionless-reformulation pre-empt C4's framing; s10-observer pre-empts the observer side of C3; measurable-vs-imaginable challenges the naive real-line picture.

## 5. External verification (independent sources)

- Monna 1952: Crossref exact — "Sur une transformation simple des nombres P-adiques en nombres reels", Indag. Math. vol 55, pp 1–9 (10.1016/s1385-7258(52)50001-5). ✓
- Ladyman & Ross: "Every Thing Must Go", OUP 2007 (10.1093/acprof:oso/9780199276196.001.0001). ✓
- Pitkänen: arXiv hep-th/9506097 "p-Adic TGD: Mathematical Ideas" + hep-th/9412103. ✓ (described epistemically: [UNTESTED] mathematical program — KIF-16.)
- Burgess EFT: hep-th/0701053 "Introduction to Effective Field Theory" + 4 sibling intros. ✓
- OpenAlex "Monna map p-adic": 125 works; top hit "P-adic Poissonian pair correlations via the Monna map" (Indag. Math. 2024, 10.1016/j.indag.2024.09.012) — external Monna-map literature ACTIVE. ✓
- OpenAlex conditional-truths search: no direct "locale framework" record in top hits → supports net-new for the framework (weak signal, noted).

## 6. Gap analysis (honest novelty — UIA Q12 applied)

- **C1 (conditional truths):** mainstream EFT doctrine + philosophy of physics; corpus has NO "locale/domain-of-applicability" doctrine record → the synthesis INTO a named framework is new within QNFO, but C1 as physics is a restatement. Novelty: LOW–MODERATE (framing).
- **C2 (map≠territory → OSR):** imported (Ladyman-Ross) + our own UIA instrument. Novelty: LOW (application).
- **C3 (interface underdetermination generalized):** UMP.010 proves the visual case; s10-observer the self-location case; NO record generalizes to arbitrary first-person channels and all physics statements. **This is the net-new core.** Novelty: MODERATE–HIGH, bounded by UMP.010 (premise-depth).
- **C4 (counts/ratios/Ostrowski):** pre-empted inside QNFO by 21480756 / 21756190 / 21590155 / 21595214. Novelty: LOW (integration only).
- **Net-new claim (SO-WHAT-GATE):** the unified four-move LOCALE FRAMEWORK — EFT-conditionality + map-territory + interface-undecidability + scale primitives as ONE doctrine with the Monna-map rendering as worked instance — is not present in the 997-record corpus (T1: 0 doctrine hits) nor in the external top-hits. The paper's honest contribution: C3 generalization + the unification; C1/C2/C4 are synthesis with named premises.
- `[CONFIRMATION-BIAS-RISK]`: all corpus hits QNFO-internal; mitigated by external verification above.
- `[AI-CONVERGENCE-WARNING]` (KIF-17): the seed notes are AI-drafted; multiple AI evaluations converged on the conditional-truth/OSR framing — convergence reflects shared training priors; external checks are the countermeasure.

## 7. SO-WHAT-GATE (reader-care + premise-depth) — restated from PROJECT-PLAN §5

Reader-care and premise-depth disclosure are locked in PROJECT-PLAN §5 and artifacts/core-claim.md. Depth: C1=EFT-restatement; C2=imported OSR (premise ENDS at Ladyman-Ross); C3=generalization of UMP.010 (premise ENDS at the interface/rendering primitive); C4=integration of QNFO records + standard metrology (premise ENDS at Ostrowski's theorem). No dynamical theory of seams is proposed.

## 8. Phase 1 verdict

PASS. Net-new confirmed for the unified framework (bounded by premise depth). Adjacent domains satisfied (UMP×RES×SLB). External verification 6/6. 3 SOFT/INFO data-quality findings logged (FIND-2/3/4) + 1 channel-outage finding (FIND-1). Next: P2 literature triage with the evidence here as the seed set.
