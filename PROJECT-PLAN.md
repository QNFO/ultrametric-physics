---
title: "The Distinction-Based Ultrametric Formula: Realization-Independent Hierarchy Distance and the Surviving Empirical Claim"
wbs: "QNFO.UMP.014"
slug: "distinction-based-ultrametric"
branch: "ump/paper/distinction-based-ultrametric"
repo: "QNFO/ultrametric-physics"
phase: "P0"
status: "active"
core_claim_locked: "2026-08-28 (revision 2 — supersedes the p-adic-observable-program claim)"
author: "Rowan Brad Quni-Gudzinas"
---

# PROJECT-PLAN — QNFO.UMP.014 (revision 2)

## 0. Revision history

- **v1 (2026-08-28):** locked "the p-adic observable program" (α as a p-adic length ratio; RS-1 137-coincidence evaluation; anisotropic α test).
- **v2 (2026-08-28):** superseded by user directive — *"NO, WE'VE ALREADY TESTED P-ADIC STRUCTURES AND ALL FAILED TO BE SIGNIFICANT. WHAT ABOUT DISTINCTION-BASED ULTRAMETRIC FORMULA?"* — and by the three-slot red-team audit (READ-ONLY): Completeness HARD-1 (the null ledger was never confronted) and HARD-2 (the distinction formula is already the program's primitive) are fixed on the record below; Dependency SOFT S2 (the RS-1 rosetta artifact has no durable home) is resolved by removing the RS-1 dependency from the claim.
- Disposition of the v1 claim: retired by directive. The Accuracy reviewer confirmed the α length-ratio claim was never executed and sits outside every falsified class; the empirical base rate of the p-adic-signature class is nonetheless 100% nulls (§2), which is the directive's ground. The v1 claim remains an untested, deprioritized idea, not a falsified one — recorded as such.

## 1. Core claim (LOCKED)

The distinction-based ultrametric formula — **d(a,b) = the number of distinctions required to separate a and b** — is the program's canonical finite distance. Three components:

- **(i) exact:** d(a,b) = min{#distinctions} = the LCA depth on any finite hierarchy, and the induced distance satisfies the ultrametric inequality. The formula's own mathematics, verified in code with golden values (the note's "min is fixed" observation, hardened).
- **(ii) structural:** realization-independence — the metric survives base change across p-adic valuation, formal Laurent series, and plain nested partitions. The prime-specific arithmetic is accidental; the hierarchy is essential (RES.023's invariant, exercised computationally).
- **(iii) empirical (the surviving hypothesis, H1):** ultrametric structure is an effective compression and clustering prior for high-dimensional sparse measurement data — tested on **external** datasets against pre-registered null models. This is the live leg of the program's 2028 decision point: if neither H1 nor H3 yields positive, the program's claim of a physics-relevant non-Archimedean substrate is falsified.

## 2. The null ledger, carried on the record (red-team HARD-1 fix)

What was tested against p-adic/ultrametric structure in physical systems, and failed:

1. CMB log-periodic — certified radix-agnostic null, Planck 2018, p = 0.89 — 10.5281/zenodo.21902891
2. CMB bispectrum — upper bounds only, no signal — 10.5281/zenodo.21901664
3. FMO coupling matrix — **anti**-ultrametric (cophenetic 0.426, p = 0.984); exact-clustering null (p = 0.598) — named program-level in the register 10.5281/zenodo.22025544; no standalone corpus record (memory Disconfirming Registry, 2026-07-17)
4. PW-WDW — strict ultrametricity falsified for generic clock-rest coupling (29–35% violation, 8,000 sims) — 10.5281/zenodo.21120286
5. Ultrametric-QEC — independent-error threshold 2.0e-4 (~55× below the surface-code threshold) — register §2; ultrametric-quantum corpus record
6. Compton cross-ratios — pre-registered adelic search over the SM mass spectrum: 1 weak hint in 15 tests, null not rejected — 10.5281/zenodo.21485556
7. A1 anharmonic mass ladder — pre-registered null; harmonic-paradigm retraction — 10.5281/zenodo.21529948 (adelic-particle-spectrum record; C1 falsified by pre-registered null)

**Inside/outside mapping:** all seven target the p-adic *realization's* empirical signatures in physical systems (the H3 family). Components (i)–(ii) of the claim are definitional/structural — not in the falsified class. Component (iii) (H1) has never been tested on external data; it is the surviving empirical claim and the 2028-decision-relevant test. Any P4 draft must carry this ledger verbatim or by reference.

## 3. Prior coverage (red-team HARD-2 fix)

The distinction formula is already the program's primitive. This project builds on three published anchors and adds what they do not carry:

- **UMP.004 — "Valuation Without ℝ"** (10.5281/zenodo.21803677): axiomatizes measurement as a graded distinguishability map v: S² → ℕ ∪ {∞} satisfying the ultrametric inequality. → This project adds the formula's explicit LCA-depth reading and a deposited verification suite.
- **RES.021 — Finite-Distinction Quantum Mechanics** (10.5281/zenodo.22046458): distinct-or-not at fixed resolution; the induced distance is ultrametric; "the distinction, the counting of distinctions, and finite resolution are unanalyzable primitives." → This project inherits that premise boundary verbatim and adds the standalone formula record + the external H1 benchmark.
- **RES.023 — The Ultrametric Program** (10.5281/zenodo.22076816): "the prime-specific arithmetic is accidental; the hierarchy is essential"; H1/H2/H3; the 2028 decision point. → This project executes the H1-external leg.
- Practitioner lineage: auditable-attention PoC (10.5281/zenodo.19648274 — concept DOI, verified against the Zenodo records API 2026-08-28; version record 10.5281/zenodo.19648275; corpus row carries the version DOI).

## 4. Hypothesis cards

- **H-DIST-1 (formula exactness).** Prediction: on any finite tree hierarchy, d(a,b) = min{#distinctions over paths} = k − depth(LCA) (k = leaf depth) and the induced distance satisfies the ultrametric inequality; the "min is fixed" identity is checked computationally, including a DAG counterexample where min-over-paths differs from the tree value. Falsifier: a finite hierarchy whose induced distance violates the ultrametric inequality, or a tree where min-over-paths ≠ k − depth(LCA).
- **H-DIST-2 (realization independence).** Prediction: under a stated digit-tree embedding rule, the metric's values are identical across realizations — plain nested partitions (LCA depth), p-adic valuation on embedded integer labels, and formal Laurent series valuation on embedded digit polynomials. Falsifier: any stated embedding rule under which the distance matrices differ on a shared leaf set (the computational suite exercises at least three realizations and asserts identical matrices).
- **H-DIST-3 (H1 external).** Prediction: on external high-dimensional sparse datasets, ultrametric hierarchical structure yields a statistically significant compression/clustering advantage over flat and random baselines under a pre-registered null model. Falsifier: no significant advantage — a certified null that feeds the 2028 decision point. Disconfirmation criterion (placeholder, fixed at P5 OSF pre-registration): effect size below a pre-registered threshold with p ≥ 0.01 after multiple-comparison control.
- **H-DIST-4 (practitioner toolbox).** Prediction: empirical ultrametricity testing distinguishes hierarchical from non-hierarchical data generators. Falsifier: the test has no power at benchmark sizes.

## 5. Premise-depth disclosure

- **L0:** the distinction, the counting of distinctions, and finite resolution are unanalyzable primitives (inherited verbatim from RES.021).
- **L1:** the ultrametric inequality — definitional.
- **L2:** the LCA-depth construction — derived, exact.
- **L3:** realization-independence — structural, computationally verified.
- **L4:** H1 — empirical hypothesis; the claim's frontier.

The claim is as deep as L0 and L4. Everything between is derived or verified; L4 is where the empirical risk sits.

## 6. Why a reader should care; what a practitioner can do

The p-adic empirical program has a 100% null base rate (§2). This project states what survives: the hierarchy invariant, carried by a distance that needs no primes at all — the number of distinctions required to separate. It then puts the surviving empirical content to the test that the 2028 decision point demands: H1 on external data. A reader gets (a) a clean statement of the formula and its realization-independence, and (b) the first external benchmark of the compression-prior claim — a positive result is the program's first non-null empirical leg; a null is a certified, decision-feeding result.

Practitioner deliverable: a hierarchy-detection toolbox — empirical ultrametricity tests that classify a dataset as hierarchical or not, applicable to QEC code-space geometry, taxonomies, and attention auditability (the 10.5281/zenodo.19648274 lineage, extended with task metrics).

Crosswalk: number of distinctions ↔ cophenetic distance ↔ LCA depth ↔ graded distinguishability; realization ↔ base/radix; the Bruhat–Tits tree ↔ the regular-tree specialization of a finite hierarchy.

## 7. UIA (Universal Ignorance Audit, administered on the revised claim)

- **Q1 (target):** the distinction formula is the canonical finite distance; realization-independent; H1 is its empirical content.
- **Q2 (falsity):** H-DIST-1..4 falsifiers; an H1 null feeds the 2028 decision point.
- **Q3 (truth):** golden-value verification; a significant H1 advantage against the null model.
- **Q4 (objects unknown):** whether "number of distinctions" admits a reading beyond LCA depth (the "min" fixity question).
- **Q5 (methods unknown):** whether empirical ultrametricity tests can separate hierarchy from mere sparsity at benchmark sizes (H-DIST-4 power).
- **Q6 (prior falsifications):** the seven-null ledger, §2 — carried on the record.
- **Q7 (unstatable unknowns):** a dependence of the formula on the observer's resolution that current vocabulary cannot state.
- **Q8 (surprise):** a large-effect H1 advantage on natural external datasets.
- **Q9 (vocabulary failure):** "distinction" may be a primitive of epistemology rather than physics — the map/territory boundary.
- **Q10 (smallest experiment):** H-DIST-3 on one external dataset with a pre-registered null model.
- **Q11 (smallest computation):** the H-DIST-1 golden-value suite (the note's own Python, hardened and seeded).
- **Q12 (imported unanalyzed):** the L0 primitives; the ultrametric inequality.
- **Q13 (avoided question):** whether the hierarchy invariant is the agent's preferred data structure rather than nature's.
- **Q14 (silence):** [held]
- **Q15 (recursive):** this audit assumes "measurement hierarchies organize as nested partitions" is the right frame at all; the next audit starts there.

## 8. Pipeline (WBS-coded)

- **[QNFO.UMP.014.P1]** Due diligence: external H1 dataset candidates; cophenetic-distance prior art (Sokal–Rohlf 1962, Jardine–Sibson 1971); evidence files to artifacts/external-search/.
- **[QNFO.UMP.014.P2]** Computational verification pass: H-DIST-1 golden values; H-DIST-2 base-change invariance; H-DIST-4 toolbox; sim scripts deposited.
- **[QNFO.UMP.014.P3]** H1 external benchmark: datasets, null models, pre-registration content.
- **[QNFO.UMP.014.P4]** Paper draft: distinction-based-ultrametric.md/.html/.pdf; rendering gates; reference list rendered FROM references.bib.
- **[QNFO.UMP.014.P5]** OSF pre-registration of the H-DIST-3 disconfirmation criterion.
- **[QNFO.UMP.014.P6]** Red-team review (Accuracy/Completeness/Dependency); fix all HARD findings.
- **[QNFO.UMP.014.P7]** Zenodo publish (deposit integrity gates; PUBLISH-LOCK-1); D1/KG/R2 distribution.
- **[QNFO.UMP.014.P8]** Post-publication adversarial audit; dissemination (CAMPAIGNS-OUTREACH-1).

## 9. Phase 1–2 evidence (executed 2026-08-28)

- **P1 due diligence:** `DUE-DILIGENCE-UMP014.md` + `artifacts/external-search/p1-arxiv-evidence-2026-08-28.json` — arXiv prior art live-verified (cophenetic lineage, ultrametric fitting, Baire-metric realization); Zenodo concept-DOI resolution for 19648274/19648275 (DOI-DISCREPANCY-RESOLVE-1 via records API); H1 external dataset candidates; adjacent-domain scan (UMP/SLB/INM/JPC); corpus data-quality findings logged.
- **P2 computational verification (COMPUTATIONAL-VERIFICATION-1):** `scripts/sim-distinction-ultrametric-verification.py` — 6/6 checks PASS, exit 0, seed 20260828, Python 3.12.10, script sha256 `b0bdcaf261ecc8210c972ce5617223adbc14d4cefa2affd0bfbb842385fbe978`; outputs `artifacts/verification/verification-output.json` + `verification-run.txt`.
- **Reproducibility:** `python scripts/sim-distinction-ultrametric-verification.py` from the branch root reproduces all six checks deterministically (fixed seed; stdlib only).
- **Verified claims:** H-DIST-1 — golden taxonomy distances (d(Dog,Wolf)=1 < d(Dog,Cat)=2 < d(Dog,Human)=3 < d(Dog,Snake)=4), ultrametric inequality on 30 seeded random trees (10–40 leaves), min-over-common-ancestors = LCA value on balanced trees, and a DAG counterexample (min-over-paths 4 ≠ tree value 3) proving the falsifier checkable. H-DIST-2 — the three realizations (plain partitions, p-adic valuation, formal Laurent valuation) yield identical distance matrices on 8/9/16-leaf trees under the stated digit-embedding rule d = (k−1) − v.
