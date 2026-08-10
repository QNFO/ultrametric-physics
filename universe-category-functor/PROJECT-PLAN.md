# WBS: QNFO.UMP.006

# PROJECT PLAN — Universe Category Functor

**Slug:** `universe-category-functor`
**Branch:** `ump/paper/universe-category-functor`
**Program Repo:** `QNFO/ultrametric-physics`
**WBS Code:** `QNFO.UMP.006`
**Date:** 2026-08-10
**Status:** Phase 0 (Init) — IN PROGRESS

---

## Charter

This project answers the Frontier Question identified by the KIF-29 Cross-Domain
Consilience Gate (2026-08-10, 8-paper synthesis):

> Can the "Universe Category" be a single functor \(F: \mathbb{N} \to \mathbf{Man}\)
> whose image encodes quantization, stability, and factorization simultaneously?

The 8-paper corpus (Alpha Pi, Thermodynamic Genesis, Strange Loop, Spectral p-Adic,
Prime Numbers, Strange Loop Formal, Matter Without Mass, Geometric Factorization)
converges on a shared structural invariant — the hierarchical combinatorial tree with
p-adic cross-ratios — with a 525-year aggregate silo cost across four domains.
This project formalizes that convergence as a categorical object.

The paper proposes a single functor from the divisibility category of the positive
integers to the category of smooth compact manifolds, and argues that its image
simultaneously realizes:
- **Quantization** — via integer-valued topological invariants (Lefschetz \(L=2\), winding \(w=1\))
- **Stability** — via the ultrametric hierarchy (Bruhat-Tits tree geometry, \(|x+y|_p \le \max(|x|_p, |y|_p)\))
- **Factorization** — via homology rank \(= 2^{\omega(n)}\) (primality as a geometric property)

**Methodological stance (KIF-60, pre-registered):** this is a structural-map claim,
NOT an identity claim. All correspondences are [RETRODICTION] until pre-registered
predictions accrue evidential weight. The paper will pre-register its predictions in a
RESEARCH-CONTINUITY-REGISTRY.md (research v2.64 HARD gate).

---

## Core Claim (Locked, P6)

> **There exists a single functor \(F: \mathcal{P} \to \mathcal{M}\) from the divisibility
> category of positive integers to the category of smooth compact manifolds such that
> the image of \(F\) simultaneously encodes (i) quantization as integer-valued
> topological invariants, (ii) stability as ultrametric hierarchy, and (iii) prime
> factorization as homology rank \(2^{\omega(n)}\). The three are not coincidences but
> faces of one categorical structure.**

Falsifiable disconfirmation conditions:
- D1: If the homology rank of \(F(n)\) for a square-free composite with \(k\) distinct
  prime factors is ever found NOT to equal \(2^k\), the framework is wrong.
- D2: If a physical system engineered with the modular-curve topology (\(L=2\), \(w=1\))
  fails to exhibit quantized behavior at the predicted scale, the topological-quantization
  leg is falsified.
- D3: If the ultrametric-error-suppression bound \(|x+y|_p \le \max(|x|_p, |y|_p)\)
  is violated by a realized Bruhat-Tits-tree quantum state space, the stability leg is falsified.

---

## Phases with WBS (QNFO.UMP.006)

| Phase | WBS | Deliverables | Gate |
|:------|:----|:-------------|:-----|
| P0 Init | `QNFO.UMP.006.P0` | PROJECT-PLAN.md, branch, scaffold, core claim lock | HARD: committed/tagged/pushed |
| P1 Due Diligence | `QNFO.UMP.006.P1` | KG + D1 + Vectorize + external literature (8 sources), KIF-29 gate update | HARD: consilience artifact |
| P2 Literature | `QNFO.UMP.006.P2` | Classified literature, KIF-18 symmetry template | HARD: both sections present |
| P3 Citations | `QNFO.UMP.006.P3` | Verified BibTeX (P3.AUTHOR-GATE) | HARD: 0 fabricated |
| P4 Research | `QNFO.UMP.006.P4` | Structured Forecast Protocol, functor formalization, red-team, calibration | HARD: artifacts present |
| P5 Publish | `QNFO.UMP.006.P5` | `<slug>.md` + PDF (CDP pipeline) + Zenodo DOI | HARD: BP-1..BP-10, gates |
| P6 Deploy | `QNFO.UMP.006.P6` | D1 living-paper, papers-server | HARD: live verification |
| P7 Disseminate | `QNFO.UMP.006.P7` | SEO, Buffer, Internet Archive | SOFT |
| P8 Distribute | `QNFO.UMP.006.P8` | GitHub tag, newversion, R2, D1/KG records | HARD: 4-layer verify |

---

## Milestones with Gate Criteria

| Milestone | Criteria | Date |
|:----------|:---------|:-----|
| M0 Phase 0 complete | Branch pushed, PROJECT-PLAN committed, tag `v0.1-phase0` | 2026-08-10 |
| M1 Phase 1 complete | Due diligence artifact + consilience update | 2026-08-11 |
| M4 Core derivation | Functor \(F: \mathcal{P} \to \mathcal{M}\) fully formalized | 2026-08-18 |
| M5 Publication | Zenodo DOI resolves (HTTP 200) + P5.FRESH pass | 2026-08-22 |
| M8 Distribution | 4-layer core distribution verified | 2026-08-24 |

---

## Deliverable Registry

| ID | Deliverable | Path | Owner |
|:---|:------------|:-----|:------|
| D-01 | PROJECT-PLAN.md | `universe-category-functor/PROJECT-PLAN.md` | Agent |
| D-02 | Core claim lock | In PROJECT-PLAN.md §Core Claim | Agent |
| D-03 | Due diligence artifact | `artifacts/due-diligence.md` | Agent |
| D-04 | Consilience gate update | `artifacts/consilience-gate.md` | Agent |
| D-05 | Literature classification | `artifacts/literature-classification.md` | Agent |
| D-06 | Citation audit | `artifacts/citation-audit.md` | Agent |
| D-07 | Bayesian evidential weight | `artifacts/bayesian-evidential-weight.md` | Agent |
| D-08 | Functor formalization | `notebooks/functor-formalization.py` | Agent |
| D-09 | Paper source | `universe-category-functor.md` | Agent |
| D-10 | PDF | `universe-category-functor.pdf` | Agent |
| D-11 | Research Continuity Registry | `RESEARCH-CONTINUITY-REGISTRY.md` | Agent |

---

## Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|:---|:-----|:-----------|:-------|:-----------|
| R-01 | Category-theoretic formalization overclaims identity | HIGH | MEDIUM | KIF-60 cap: structural-map language, never identity |
| R-02 | D1 DOI drift (concept vs version) | MEDIUM | LOW | Verify ownership live per P5.OWNERSHIP |
| R-03 | Internal-ref leakage into published paper | MEDIUM | MEDIUM | Publication Language Gate (INTERNAL-REF-1) |
| R-04 | Reviewer rejects functor as "pure numerology" | MEDIUM | HIGH | Pre-registered falsifiable predictions + BP-8 classification |
| R-05 | MathJax/PDF pipeline failure | LOW | MEDIUM | Canonical CDP pipeline only, no fallbacks |

---

## Success Criteria

1. Functor \(F: \mathcal{P} \to \mathcal{M}\) formally defined with proof of the
   homology-rank property \(H_*(F(n)) = 2^{\omega(n)}\).
2. Quantization, stability, and factorization legs each mapped onto the functor image.
3. ≥3 pre-registered falsifiable predictions in RESEARCH-CONTINUITY-REGISTRY.md.
4. Publication through the full QNFO pipeline (GitHub → Zenodo → D1/KG → distribution).
5. All KIF-29/KIF-60/KIF-62 gates passed with honest [RETRODICTION] labeling.

---

## Session Log

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-10 | this | Phase 0 init: WBS resolve QNFO.UMP.006, branch, scaffold, plan |
