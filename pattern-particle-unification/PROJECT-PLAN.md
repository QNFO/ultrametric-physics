# WBS: QNFO.UMP.013

**Title:** One Table, Two Regimes: Unifying Standard-Model Particles and Condensed-Matter Excitations on the Bruhat–Tits Tree
**Slug:** pattern-particle-unification
**WBS:** QNFO.UMP.013 (parent: QNFO.UMP — Ultrametric Physics)
**Repo:** QNFO/ultrametric-physics · **Branch:** ump/paper/pattern-particle-unification
**Date:** 2026-08-19 · **Status:** Phase 0 (core claim locked, registry claimed)

**Origin:** CMD RESEARCH 2026-08-19 — "UNITE STANDARD MODEL OF PARTICLE PHYSICS (FERMIONS, BOSONS) AND CONDENSED MATTER (QUASIPARTICLES, ANYONS)".

## Charter

Produce a single publication that unifies the Standard Model's elementary particles (fermions, bosons) and condensed matter's emergent excitations (quasiparticles, anyons) as one structural object — the pattern–particle correspondence on the Bruhat–Tits (BT) tree — with a regime dictionary explaining when each reading applies, a practitioner-facing implementation path, and honest premise-depth disclosure.

## Why a reader should care

Physics runs two particle catalogs that never meet in one framework: the Standard Model's table of elementary fermions and bosons, and the condensed-matter zoo of quasiparticles and anyons. Textbooks treat them as different ontologies — fundamental fields versus emergent lattice excitations. This paper argues they are two projections of one table: both are labeled patterns of the same Bruhat–Tits tree, differing only in the statistics phase of the pattern (boson +1, fermion −1, anyon a root of unity on a ramified branch) and in the Compton count N_C* that fixes the mass-frequency scale. If the unification holds, then the spin-statistics theorem, braid statistics, and quasiparticle effective masses are three evaluations of a single tree structure, and every excitation — elementary or emergent — has a canonical tree address that practitioners can compute and compare. The claim is falsifiable: a fundamental particle whose statistics phase is not a tree-automorphism phase, or a quasiparticle whose N_C* is not a rational function of constituent counts, would break the framework.

## Premise-depth disclosure (where the premises END)

This paper DERIVES the unified table and the regime dictionary. It does NOT derive its load-bearing inputs, which are named imports:

1. **Compton count as the only primitive** — ODR thesis (10.5281/zenodo.21780909). Imported as the mass-frequency ontology.
2. **The Bruhat–Tits tree as the correct state-space geometry** — QNFO.UMP program claim (adelic cross-domain program lineage; DOI verified in Phase 1). Imported as the geometric substrate.
3. **Spin-statistics as a structural invariant of the tree** — RES.009 ("The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant"). Imported as the statistics reading.
4. **Quasiparticles as rational functions** — QP v2.0 (10.5281/zenodo.21784490): quasiparticle Compton counts N_C* as rational-function composites. Imported as the condensed-matter reading.
5. **Anyons as p-adic braid phases** — "Adelic Synthesis: The Pattern-Particle Correspondence and the Complete Arithmetic Theory of Anyons" + "p-Adic Anyon Fusion and Braiding" (slugs in corpus; DOIs verified in Phase 1). Imported as the braid-statistics reading.

Derived-in-this-paper content: the unification table (SM particles + condensed-matter excitations as labeled BT-tree patterns), the regime dictionary (which tree place/ramification corresponds to which physical regime), and the falsifiability conditions tying the framework to observation. Novelty claims are bounded by these five premises and nothing deeper.

## What a practitioner can DO with this (implementation path)

1. **Pattern-address classifier (tangible: lookup tool / SDK).** A decision tool that takes an experimentally measured excitation — statistics phase, mass or effective mass, composition — and returns its canonical BT-tree address (place, branch depth, node class, N_C*). Experimentalists characterizing new fractional-quantum-Hall states or emergent quasiparticles can classify an excitation against the unified table in seconds. Implementation: a spec-sheet table + braid-phase calculator (roots of unity from the tree data), shippable as a QWAV demo with a golden-value test suite.
2. **SM ↔ condensed-matter spec-sheet mapping.** A practitioner-grade dictionary: composite Higgs ↔ Cooper-pair node, photon ↔ phonon/edge mode, electron ↔ quasielectron with effective N_C*. Usable in quantum-materials pedagogy and as a device-modeling reference (engineering language: effective mass renormalization, statistics phase, topological boundary conditions).
3. **Topological-quantum-computing benchmark.** The anyon braid-phase table (roots of unity on ramified branches) as a spec-sheet for verifying fusion-rule implementations in TQC platforms — a checkable, machine-testable claim about what braid phases are permissible.

Every practitioner claim is conditional: it holds in the regime where the corresponding premise (above) applies, and nowhere else.

## Phases with WBS

| Phase | WBS | Deliverable | Gate |
|---|---|---|---|
| P0 Init | QNFO.UMP.013.P0 | Registry claim, branch, PROJECT-PLAN.md, core-claim lock, tag v0.1-phase0-ump013 | HARD: P1–P11 pre-flight |
| P0.5 Ignorance audit | QNFO.UMP.013.P0 | UIA 15 questions on core claim (artifacts/ignorance-audit.md) | HARD: all 15 answered, written |
| P1 Due diligence | QNFO.UMP.013.P1 | Full-corpus sweep, cross-system ID validation, adjacent-domain audit, external verification, gap analysis | HARD: DUE-DILIGENCE-DEPTH-1 |
| P1b Consilience | QNFO.UMP.013.P1 | artifacts/consilience-gate.md + artifacts/bayesian-evidential-weight.md | HARD: KIF-29 + KIF-60 |
| P2 Literature | QNFO.UMP.013.P2 | 8-source search, classification matrix, symmetry template | HARD: KIF-18 |
| P3 Citations | QNFO.UMP.013.P3 | Verified BibTeX, references.bib | HARD: P3.AUTHOR-GATE |
| P4 Deep research | QNFO.UMP.013.P4 | Structured forecast, derivation of unified table, red-team | HARD: calibration register |
| P5 Publication | QNFO.UMP.013.P5 | pattern-particle-unification.md/.html/.pdf + Zenodo DOI + all source files | HARD: BP-1..BP-10, SO-WHAT-GATE, PRACTITIONER-RELEVANCE-1, PUBLICATION-PROSE-GATE-1 |
| P6 Deploy | QNFO.UMP.013.P6 | D1 living-paper insert, Vectorize index, KG node | HARD: PUBLICATION-KG-INDEX-GAP-1 |
| P7 Disseminate | QNFO.UMP.013.P7 | Zenodo only (NO-JOURNALS-1); R2 mirror; social | HARD: R2-MIRROR-AFTER-PUBLISH-1 |
| P8 Distribute | QNFO.UMP.013.P8 | Closeout verification, post-publication adversarial audit | HARD: 7-layer closeout |

## Milestones with gate criteria

- M0: Phase 0 committed, tagged, pushed, verified via `git ls-remote` (this plan).
- M1: Gap analysis filed with >=3 query formulations per topic and evidence files per count.
- M2: Unified table derived with every claim carrying a falsifiability condition.
- M3: Published with concept DOI, R2 mirror, D1/KG/Vectorize records, post-publication audit clean or remediated.

## Deliverable Registry

| Deliverable | Location |
|---|---|
| Project plan | pattern-particle-unification/PROJECT-PLAN.md |
| Core claim lock | pattern-particle-unification/artifacts/core-claim.md |
| Ignorance audit | pattern-particle-unification/artifacts/ignorance-audit.md |
| Due diligence | pattern-particle-unification/artifacts/due-diligence-phase1.md |
| Consilience gate | pattern-particle-unification/artifacts/consilience-gate.md |
| Bayesian evidential weight | pattern-particle-unification/artifacts/bayesian-evidential-weight.md |
| External search evidence | pattern-particle-unification/artifacts/external-search/*.json |
| Paper | pattern-particle-unification/pattern-particle-unification.md (+ .html, .pdf) |
| Zenodo record | DOI (TBD, Phase 5) |

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Unification reads as absorption (everything = special case) | Medium | High | KIF-60 tautology-trap audit; pre-declared allowed dualities; falsifiability conditions per claim |
| Statistics phases fail to match some particle (e.g., quasiparticle with non-root-of-unity statistics) | Low | High (kills claim) | Named as disconfirmation condition, not absorbed |
| Corpus overlap: prior QNFO work already covers parts (anyons, quasiparticles, spin-statistics) | High | Medium (novelty bounded) | Gap analysis must name exactly what is NEW (the unified table + regime dictionary), not re-derive prior results |
| WBS collision with concurrent session | Low | Medium | Atomic check-then-insert executed (single statement, NOT EXISTS guard) |
| VECTORIZE-TOP-K-50-1: qnfo-memory-mcp 1101 at limit>=17 | Medium | Low | Retry at limit<=16; note cap in evidence file |

## Success Criteria

1. One falsifiable unified table covering all SM fermions + bosons and the major quasiparticle/anyon classes, each with a tree address.
2. Every cross-domain correspondence claim passes KIF-60 (Δlog-odds > 0 or labeled retrodiction).
3. Practitioner section delivers a runnable artifact path (spec-sheet + braid-phase calculator demo).
4. Published on Zenodo with full source set, R2 mirror, D1/KG/Vectorize records, and a clean post-publication adversarial audit.
