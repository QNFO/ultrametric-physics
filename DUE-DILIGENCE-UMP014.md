# P1 Due Diligence — QNFO.UMP.014 (distinction-based ultrametric)

> **Date:** 2026-08-28 · **Branch:** ump/paper/distinction-based-ultrametric · **Phase:** P1
> Evidence files: `artifacts/external-search/p1-arxiv-evidence-2026-08-28.json`

## 1. Scope

Full-corpus and external due diligence for the locked claim — the distinction-based
ultrametric formula d(a,b) = number of distinctions required to separate a and b as the
program's canonical finite distance, with realization independence (component ii) and the
surviving empirical content H1 (component iii, external benchmark).

## 2. External prior art (arXiv, live-verified 2026-08-28)

The cophenetic/taxonomic ultrametric lineage is classical (Sokal–Rohlf 1962; Jardine–Sibson
1971; Johnson 1967; Carlsson–Mémoli 2010). Modern live-verified arXiv anchors:

| ID | Title | Relevance |
|---|---|---|
| 1106.2229 | Fast, Linear Time Hierarchical Clustering using the Baire Metric | an independent realization of hierarchy-as-invariant (Baire metric → ultrametric) |
| 1905.10566 | Ultrametric Fitting by Gradient Descent | the fitting baseline for the H1 benchmark null model |
| 2012.02655 | A New Non-archimedean Metric on Persistent Homology | independent cophenetic/non-Archimedean metric on persistence |
| 2309.01301 | T-Stochastic Graphs | statistical ultrametricity handling in network analysis |
| 2504.06700 | LP-Rounding for Hierarchical Clustering / Fitting Ultrametrics | algorithmic fitting prior art |
| 1311.5068 | Gromov–Hausdorff stability of linkage methods | toolbox stability grounding |
| 2608.25586 | Individual Fairness in Hierarchical Clustering (2026-08-26) | same-week activity in the area |

No arXiv prior art claims the distinction-count reading d = number of distinctions to
separate as a foundational distance, nor the realization-independence statement of the
locked claim.

## 3. Zenodo DOI resolution (gate: DOI-DISCREPANCY-RESOLVE-1)

The auditable-attention citation was challenged as unresolvable by the Dependency re-check
reviewer. Records-API resolution: `GET /api/records/19648274` redirects to the version
record 19648275 (title "A Proof-of-Concept for Auditable Attention Using Ultrametric Tree
Distances", published 2026-04-19, conceptrecid 19648274, conceptdoi
10.5281/zenodo.19648274). **19648274 is the concept DOI — the plan's citation is correct
per ZENODO-CONCEPT-DOI-CITE-1**; the corpus row carries the version DOI. Both resolve; no
citation change. The reviewer's HARD finding is resolved as a corpus-tool limitation, and
the plan documents the concept/version pair (§3).

## 4. External H1 dataset candidates (P3 benchmark)

20 Newsgroups (sparse document-term), RCV1, MNIST (dense high-dim), Arcene (10k features,
n=100), Covertype, Golub/TCGA expression panels. Selection criteria: public, reproducible,
spanning sparse/dense and low/high-n regimes. Final set + null models are fixed at P3.

## 5. Adjacent WBS domains (CROSSWALK-TRANSLATION-1)

UMP (primary), SLB (the formula's home language — calculus of distinction), INM
(information reading: distinctions = information; H1 is a compression claim), JPC/PLT
(practitioner: QEC code-space geometry, attention auditability). Crosswalk table is drafted
for P4: number of distinctions ↔ cophenetic distance ↔ LCA depth ↔ graded
distinguishability; realization ↔ base/radix; Bruhat–Tits tree ↔ regular-tree
specialization.

## 6. Gap analysis (summary)

- H1 external benchmark: **genuinely uncovered** (0 corpus records; only the internal
  taxonomy audit exists — RES.022).
- Standalone LCA-depth verification suite: **new** (records axiomatize; none verify the
  formula in code).
- DAG min-fixity refinement: **new** (note-level insight, unrecorded in the corpus).
- Practitioner hierarchy-detection toolbox: **partial** (auditable-attention PoC exists
  without task metrics).

## 7. Corpus data-quality findings (logged, pre-existing)

Duplicate slug rows for 21485556; duplicate 20108536 row with mangled title; 22046458
identifier carries pre-remediation 22044379; ultrametric-program r2_key convention
violation; FMO null lacks a standalone anchor. All SOFT; queued for the data-quality
sweep; none affects the locked claim's dependencies.

## 8. Verification

This phase produced no quantitative claims requiring computational verification beyond the
DOI/registry resolves above (recorded in the evidence JSON). P2 carries the formula
verification suite.
