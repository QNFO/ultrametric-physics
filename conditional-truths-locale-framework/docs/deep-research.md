# Deep Research — QNFO.UMP.011 P4 (2026-08-17)

Project: Conditional Truths and the Locale Framework (slug conditional-truths-locale-framework)
This document is the P4 reasoning trail: how the draft was built from the evidence, the synthesis decisions, the UIA-Q15 measurement-model formulation, the F3 probe-design analysis, and the honesty register. It is part of the publication provenance set.

## 1. Synthesis decisions (evidence → draft)

| Draft section | Evidence | Decision |
|:--------------|:---------|:---------|
| §2 catalog | seed note `_26229070448` (conditional-truths list) + Burgess [4]/Georgi [5]/Wells [28] | Kept the EFT framing explicit; catalog presented as synthesis, not discovery (KIF-60 verdict from bayesian-evidential-weight.md) |
| §3 map/territory | seed notes `_26229070121` + `_26229070448` (spin) + Ladyman-Ross [2] + critics [20][21][22] | OSR kept as NAMED IMPORTED PREMISE; the three OSR-criticism refs cited so C2 is argued against, not asserted |
| §4 rendering | seed note `_26228233551` (Monna-map perspective) + UMP.010 [6] + Monna [1] + Cantor [18] + Pitkänen [27] + Weiß [19] | C3 generalization stated as the net-new core; discontinuity argument uses the digit proof (UMP.010 v0.2 remediation) not the invalid disconnectedness shorthand |
| §5 scale primitives | seed note `_26228215041` (frequency as count, T=∂E/∂S, Compton clock) + Ostrowski [3] + prior records [9][10][11][12] | C4 = integration with explicit prior-record lineage |
| §6 framework | consilience-gate.md MVF-1 | The completion↔background isomorphism is LABELED retrodictive (KIF-60) — pedagogical unification, not discovery |
| §8 register | core-claim.md F1-F4 | F1-F4 preserved verbatim in substance; F3 probe-design question kept OPEN |

## 2. UIA Q15 formulation (measurement-model sketch)

Q15 seed from artifacts/universal-ignorance-audit.md: "What would make the interface-underdetermination claim PHYSICS rather than epistemology — a derivation from a Hamiltonian/measurement model of the rendering channel?"

Sketch (P4 register, NOT yet a theorem):
- Define a rendering channel as a stochastic map $\Phi: \mathcal{O}(X) \to \mathcal{P}(V)$ from substrate observables to probability measures over image observables.
- Two substrates $(X_1, d_1)$, $(X_2, d_2)$ are observationally equivalent under $\Phi$ if for every finite set of channel outputs the induced joint distributions coincide.
- C3 becomes: for $(X_1, d_1) = (\mathbb{R}^n, \text{Archimedean})$ and $(X_2, d_2) = (\text{ultrametric}, |\cdot|_p)$ with $\Phi$ = Monna-type digit rendering, the equivalence class is nonempty; no finite probe separates the fibers.
- F3 becomes: exhibit a probe (a statistic of channel outputs whose expectation distinguishes the fibers) — OR prove none exists. The open question is which.

Status: FORMULATION-ONLY. The draft (§9) commits to this as the next pass; the paper does NOT claim the theorem.

## 3. F3 probe-design analysis

Candidates considered (from UMP.010's open-question register + this paper):
1. **Discrete apparent-size steps at p-adic rationals.** In the visual case, an ultrametric substrate would render sizes that jump at digit boundaries; an Archimedean substrate renders smooth size gradients. Status: the RENDERING is known (Monna staircase [6]); whether a first-person observer can distinguish "staircase rendered smoothly" from "smooth" WITHOUT knowing the rendering is exactly the open question. Not ruled out; not proven.
2. **Absent smooth parallax.** Continuous motion in an ultrametric substrate has no continuous path; rendered motion would show hops. Same status as (1): the hop signature is a rendering artifact, and the observer cannot separate "substrate hops" from "rendering quantizes".
3. **Structure-leak statistics.** Count the statistical regularities of image-space discontinuities (seam rate, digit-boundary alignment). This is the most promising: digit-boundary alignment (events at $p^{-k}$ scales for a definite prime $p$) is a rendering-construction fingerprint, and it is testable in principle against the null of Archimedean rendering with noise. Status: proposed as the P4→P5 falsification target; no data yet.

Verdict: F3 stays OPEN; the register records the strongest candidates and their status honestly.

## 4. Honesty register (what this paper does NOT claim)

1. C1 is a restatement of EFT doctrine (KIF-60: [RETRODICTION — framing only]).
2. C2's ontology is imported OSR [2], argued against its critics [20][21][22]; replaceable without loss.
3. The completion↔background isomorphism (MVF-1) is a pedagogical unification, not a discovery.
4. C3's visual case is prior art [6]; the generalization is new but unproven — F3 is open.
5. C4 is standard metrology restated + integration of [9][10][11][12].
6. No claim that the substrate IS ultrametric — only that it is undecidable from inside.
7. No dynamical theory of seams; "locale" and "interface" are primitives.
8. The instantiation problem (why one gauge group) is raised, not solved.

## 5. Gate status at P4

- PANDOC-SAFE: scripted check in scripts/p4-gates.py (unicode math glyphs, bare pipes, $ balance).
- INTERNAL-REF-1: scripted check (WBS codes, repo paths, internal program names, skill refs, "QNFO" possessive).
- TITLE-DUPLICATION-1: exactly one title (YAML only; no body H1).
- SO-WHAT-GATE-1: abstract carries reader-care + premise-depth (present).
- AI-QUALITY-GATE-1: no fabricated citations (28/28 verified in P3); no energy-budget claims; no synthetic anchors.
- MAP-TERRITORY: TERRITORY claims (C2/C3) carry falsification conditions in §8.
