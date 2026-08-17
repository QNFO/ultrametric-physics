# WBS: QNFO.UMP.011

**Title:** Conditional Truths and the Locale Framework: Map, Territory, and the Rendering Interface
**Slug:** conditional-truths-locale-framework
**WBS:** QNFO.UMP.011 (parent: QNFO.UMP — Ultrametric Physics)
**Repo:** QNFO/ultrametric-physics · **Branch:** ump/paper/conditional-truths-locale-framework
**Date:** 2026-08-17 · **Status:** Phase 0 (core claim locked, registry claimed)

**Origin:** CMD RESEARCH 2026-08-17 from four vault notes:
- `_26228215041.md` (2026-08-16) — quantum surface distinction; wavelength/frequency as recurrence counts; Ostrowski's theorem (the Archimedean real line is one completion among many); Compton frequency vs thermal frequency; temperature as inverse scale; entropy before temperature.
- `_26228233551.md` (2026-08-16) — Monna-map perspective: the experienced metric is the metric of the image space V, not the substrate X; no finite set of first-person observations distinguishes an Archimedean from an ultrametric substrate; objects are clusters in nested neighborhoods (individuation is partition-theoretic); "a rendering with structure leaks structure."
- `_26229070121.md` (2026-08-17) — map vs territory: the pedagogical map (spinning charged sphere) must be burned at the seam; the territory is the transformation law; question: is the ontological territory "pure mathematical structure" or not?
- `_26229070448.md` (2026-08-17) — conditional truths of physics: photon mass, speed of light, energy conservation, electron charge/mass, second law, Newton's law, vacuum, spin — each holds only within a locale; the ontological territory is invariant relational constraint (ontic structural realism), actualized as process.

**Ancestor:** QNFO.UMP.010 "Non-Archimedean Projective Perspective" (latest v0.3 10.5281/zenodo.21979032, 2026-08-17; cite via concept DOI 10.5281/zenodo.21969603, P8 complete) — visual projective perspective as the worked special case of the Monna-map rendering argument. This project generalizes that argument to ALL physical statements (the locale framework) and states its epistemology.

---

## 1. Charter

Formalize the four-note synthesis as a UMP paper with four moves:

1. **Locale-conditionality of physics statements** — "the photon is massless," "energy is conserved," "spin is angular momentum," "c is constant" are conditional truths: each holds only within a specified locale (vacuum/symmetry sector, stationary background, inertial frame, representation/scale). The interesting physics lives at the seams where the locale changes.
2. **Map ≠ territory** — pedagogical maps fail quantitatively and structurally at seams (spinning-sphere surface velocity > c; g=1 vs 2.0023…). The ontological territory is the invariant relational structure — the transformation law, the commutation algebra, the gauge-invariant observable — that transfers across locales.
3. **Interface underdetermination (generalization of UMP.010)** — an observer constrained to first-person observations inside a rendering interface experiences the metric of the image space V, not the substrate X. No finite set of such observations decides the substrate metric class. The substrate metric is not decidable from inside the interface — but the interface can be probed: a rendering with structure leaks structure.
4. **Scale primitives** — stripped of anthropocentric units, frequency is a recurrence count, α is a ratio, temperature is an inverse scale (∂E/∂S), not motion. By Ostrowski's theorem the Archimedean real line is one completion among many; counts and ratios live in Q, which has many places. The physics is in dimensionless ratios (L/λ_F, λ/λ_T, α), not in meters or seconds.

## 2. Core claim (locked at P6 — see artifacts/core-claim.md)

> **C1 (Locale-conditionality):** Every physical statement is a conditional truth — it holds only relative to a specified locale, and the physics lives at the seams.
> **C2 (Map ≠ Territory):** The pedagogical map is never the ontological territory; the territory is the invariant relational structure that transfers across locale seams (ontic structural realism as named imported input, not derived).
> **C3 (Interface Underdetermination):** First-person observation inside a rendering interface cannot decide the substrate metric — Archimedean or ultrametric — yet structure leaks, so the interface can be probed from inside.
> **C4 (Scale primitives):** Natural observables are counts and ratios; the Archimedean real line is one completion among many (Ostrowski); the physics is in dimensionless ratios.

## 3. Phases (WBS-coded)

| Phase | WBS | Status |
|:------|:----|:-------|
| P0 init + claim lock | QNFO.UMP.011.P0 | DONE 2026-08-17 (commit 41b88b6, tag v0.1-phase0-ump011, D1 row readback-verified) |
| P1 due diligence | QNFO.UMP.011.P1 | DONE 2026-08-17 (16-formulation FTS sweep, 997-paper corpus; cross-system validation; external verification 6/6; evidence in artifacts/) |
| P1b consilience gates | QNFO.UMP.011.P1B | DONE 2026-08-17 (KIF-29 consilience-gate.md MVF-1..3 + silo cost table; KIF-60 bayesian-evidential-weight.md — C3 is the only positive-weight claim, MVF-1 capped [RETRODICTION]) |
| P2 literature triage | QNFO.UMP.011.P2 | DONE 2026-08-17 (10-source external triage, literature-triage-evidence.json + phase2 doc; OSR-criticism engagement set 3 refs; EFT-philosophy lineage; p-adic-cognition positioning; Monna-map use net-new) |
| P3 citations | QNFO.UMP.011.P3 | DONE 2026-08-17 (28/28 field-level PASS via Crossref/Zenodo/arXiv live APIs; references.bib auto-generated from verified evidence; citation-audit.md; FIND-5 INFO: ostrowskidimless Zenodo title v4.0.4 vs D1 stale) |
| P4 deep research + draft | QNFO.UMP.011.P4 | DONE 2026-08-17 (conditional-truths-locale-framework.md PANDOC-SAFE draft, SO-WHAT abstract, F1-F4 register, OSR-criticism engaged; docs/deep-research.md with Q15 measurement-model sketch + F3 probe analysis; scripts/p4-gates.py PASS 0 failures) |
| P5 publication | QNFO.UMP.011.P5 | pending (Zenodo only — NO-JOURNALS-1) |
| P6 deploy | QNFO.UMP.011.P6 | pending |
| P7 dissemination | QNFO.UMP.011.P7 | pending |
| P8 distribution | QNFO.UMP.011.P8 | pending |

## 4. Gate criteria

- P0: HARD gates P1-P8 per Pre-Flight Checklist; D1 program_registry row claimed atomically (WHERE NOT EXISTS) and readback-verified; git ls-remote verify.
- P1: DUE-DILIGENCE-DEPTH-1 (≥3 query formulations per topic, limit ≥20, cross-system ID validation, ≥2 adjacent WBS domains, external verification, evidence files in artifacts/external-search/).
- P4: red-team ≥1 reviewer slot + direct-audit fallback; PANDOC-SAFE; SO-WHAT-GATE-1; AI-QUALITY-GATE-1; MAP-TERRITORY gate (scripted).
- P5: BP-1/BP-2; PUBLICATION-SOURCE-COMPLETENESS-1; TITLE-DUPLICATION-1 gate; INTERNAL-REF-1; P5.FRESH self-DOI ordering; Tool-Call Execution Mandate.

## 5. SO-WHAT-GATE (reader-care + premise-depth)

**Why a reader should care.** Map-territory conflation is a live failure mode in physics education and interpretation debates. This paper turns "conditional truth" from a footnote into a first-class epistemic category, gives the interface-underdetermination claim a precise, falsifiable form ("the substrate metric is not decidable from inside the interface"), and identifies what survives — structure leaks. It connects metrology (frequency as count), number theory (Ostrowski's completions), condensed matter (skin effect vs topological boundary), thermodynamics (temperature as inverse scale), and philosophy (structural realism) under one doctrine, with the Monna-map rendering (UMP.010) as its worked instance.

**Premise-depth disclosure (where the premises END).**
- *Named imported inputs:* Ladyman–Ross ontic structural realism (C2 ontology, imported not derived); Ostrowski's theorem (standard); Monna map construction (Monna 1952); UMP.010 underdetermination result (our own prior published record); effective-field-theory locale doctrine (running couplings, standard).
- *Primitives:* "locale" (a specified domain of applicability) and "interface/rendering" (a map from substrate to image space) are unanalyzable primitives — defined ostensively, not derived.
- *Derived:* C1 is a synthesis of documented cases; C3 generalizes UMP.010 from visual perspective to arbitrary first-person observation; C4 restates standard metrology.
- *Premises end here:* the framework proposes no dynamical theory of seams (no explanation of why locales change or which locales exist in nature); it does not claim the substrate IS ultrametric — only undecidable from inside; it derives no new unit or completion.

## 6. Risk register

| Risk | Mitigation |
|:-----|:-----------|
| WBS collision | Atomic WHERE NOT EXISTS claim done; UMP.011 free in D1 (authoritative), KG, wbs_state, qnfo-audit.projects |
| Overlap with UMP.010 | UMP.010 = visual-perspective special case; this = general locale framework across all physics statements; explicit BUILDS_ON citation |
| Novelty vs mainstream EFT doctrine | Contribution = interface-undecidability generalization + count/ratio/Ostrowski framing + falsifiable probe questions, not the EFT doctrine itself |
| Philosophy labeling | This IS a philosophy-of-physics paper: philosophy-class keywords are legitimate (judicious-labeling policy) |

## 7. Deliverables

`<slug>.md/.html/.pdf` · `references.bib` · `citation-audit.md` · `artifacts/external-search/*` evidence · `docs/deep-research.md` · `artifacts/universal-ignorance-audit.md` · `artifacts/core-claim.md`.
