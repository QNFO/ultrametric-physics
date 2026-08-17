# Phase 2 Literature Triage — QNFO.UMP.011 (2026-08-17)

Project: Conditional Truths and the Locale Framework (slug conditional-truths-locale-framework)
Evidence: `artifacts/external-search/literature-triage-evidence.json` (10 source-queries, this phase) +
`external-verification.json` (P1) + `corpus-sweep-evidence.json` (P1, 997-paper corpus).
Vectorize channel: STILL DOWN at P2 run (Worker Error 1101, ray_id a2c8933b1e27a55c, 2026-08-17 12:10Z — retry documented; addendum deferred to next cycle per FIND-1).

## 1. External sources queried (8-source protocol)

| Source | Queries | Hits | Status |
|:-------|:--------|:-----|:-------|
| OpenAlex | ultrametric perception / EFT domain / OSR criticism / non-Archimedean cognition | 32 | ✅ |
| Crossref | Monna map title / conditional-truth-locale title | 10 | ✅ |
| arXiv | ultrametric+observer+p-adic / EFT+philosophy | 12 | ✅ |
| Zenodo records | ultrametric perception / "conditional truth" physics | 12 | ✅ |
| Europe PMC | skipped — biomedical-only index; no coverage for this topic (documented skip) | — | ⏭️ |
| Web search | covered by OpenAlex+Crossref+arXiv+Zenodo (browser leg not needed for math/philosophy-physics topic) | — | ⏭️ |
| QNFO Vectorize | DOWN (Error 1101) — FIND-1; FTS + KG + memory used instead | — | ⚠️ |
| QNFO KG | P1 neighbor walks + node search (done) | ✅ |

## 2. Dedup vs P1 corpus hits

External hits overlapping QNFO-internal corpus: 0 (no external record duplicates any of the 14 key corpus records). No double-counting.

## 3. Classified findings (support / complicate / prior-art)

### 3.1 OSR criticism (C2) — COMPLICATES, must engage in P4
- "Ontic structural realism and the interpretation of quantum mechanics" (2012, 10.1007/s13194-012-0054-x) — OSR in QM context.
- "Is There a Compelling Argument for Ontic Structural Realism?" (2011, 10.1086/662258) — DIRECT challenge to C2's imported ontology.
- "On the Preferability of Epistemic Structural Realism" (2004, 10.1023/b:synt.0000047712.39407.c3) — ESR vs OSR debate.
→ P4 MUST cite these; C2's premise-depth disclosure (OSR = named imported input) is validated by this literature's existence. The paper claims OSR as imported, not derived — consistent.

### 3.2 p-adic/ultrametric cognition & perception (C3 adjacent) — SUPPORTS, external lineage
- "Quantum-like modeling of cognition" (2015, 10.3389/fphy.2015.00077, 93 cited) — non-Archimedean cognition school (Khrennikov et al.) active.
- "An Ultrametric Random Walk Model for Disease Spread..." (2022, 10.3390/e22090931) + ultrametric diffusion (2021, 10.1016/j.physa.2021.126284) — ultrametric structure in biology active.
- arXiv 2510.00043 "Linear Regression in p-adic metric spaces" (2025) + 2601.03738 "A glimpse into the Ultrametric spectrum" (2026-01) — p-adic ML literature growing.
→ These establish that "ultrametric substrate in cognition" is an ACTIVE external field (not fringe); C3's generalization must position against it (their claims are substrate-REALIST; C3 is substrate-AGNOSTIC — the underdetermination cuts both ways).

### 3.3 EFT philosophy (C1) — SUPPORTS (mainstream)
- "Effective Field Theory, Past and Future" (Georgi, arXiv 0908.1964) — canonical EFT review; C1's locale doctrine = EFT doctrine, confirmed mainstream.
- "Effective Field Theories and the Role of Consistency in Theory Choice" (arXiv 1211.0634, 2012) — philosophy of EFT exists; C1 is a restatement with a new name ("locale") — P4 must credit EFT-philosophy lineage (premise-depth).
- Crossref: "The fundamental laws of physics can tell the truth" (1991) + "Are the laws of physics economical with the truth?" (1993) — philosophy-of-law conditional-truth discussion predates; C1's framing is not without precursors (SOFT note for P4: cite at least one).

### 3.4 Monna map (C3 math) — SUPPORTS
- "P-adic Poissonian pair correlations via the Monna map" (Indag. Math. 2024, 10.1016/j.indag.2024.09.012) — confirmed again via Crossref title search (P1 via OpenAlex). External Monna-map math literature active; the rendering/interface USE is QNFO's own (UMP.010) — no external record found using Monna map as perceptual interface (supports C3 net-new).

### 3.5 Non-Archimedean cognition noise — FILTERED
- Quantum-like cognition (unconscious-conscious dynamics, 2015) etc. — relevant only as lineage; not prior art for the locale framework itself.
- Zenodo hits ("On similarity related the genetic code") — false positives, excluded.

## 4. Phase 2 verdict

PASS. External literature: (a) OSR criticism exists → C2 must engage (3 refs); (b) p-adic cognition/ultrametric-biology active → C3 positioned as substrate-agnostic (distinct from substrate-realist school); (c) EFT philosophy mainstream → C1 restatement credited; (d) Monna-map math active, rendering-interface use net-new. No external record pre-empts the unified locale framework. P4 seed set: 7 new external refs + 14 corpus records + 4 vault notes.
