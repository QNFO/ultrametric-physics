# RESEARCH-CONTINUITY-REGISTRY — QNFO.UMP.013 (pattern-particle-unification)

**Living document** · Created 2026-08-19 (Phase 4) · Per research skill v2.64 (HARD): any publication with frontier questions / falsifiable predictions MUST track them here.

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next action | Pre-Reg suitable |
|---|---|---|---|---|
| FQ1 | Can non-abelian (matrix-valued) statistics be realized as higher-dimensional automorphism REPRESENTATIONS of the same tree (not 1-dim characters)? | OPEN | Formalize Ising/Fibonacci data on BT-building representations (Aubert 2023 machinery) | YES (REG-UMP013-002) |
| FQ2 | What is the exact automorphism group of the relevant BT tree and its 1-dim character set? (UIA-A2) | OPEN | Specify group + characters; check against ±1 and cyclotomic characters | YES |
| FQ3 | Does the regime dictionary (place ↔ physical regime) admit a precise statement in which SM = unramified evaluation? | OPEN | Derive from adelic product structure; test against Higgs (composite ambiguity) | PARTIAL |
| FQ4 | What measurement REQUIRES the tree (indispensability, UIA-A6)? | OPEN | Scan candidate measurements vs non-tree alternatives | YES |
| FQ5 | Do quasiparticle N_C* rational functions extend to strongly-correlated regimes via algebraic (non-rational) functions? | OPEN | Collect heavy-fermion m* data; test algebraic closure | YES |
| FQ6 | Does a place-parameterized diagram calculus reproduce abelian anyon braid outcomes without ad-hoc inputs? (P4) | OPEN | Implement calculus + calculator | YES |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test window | Instrument | Disconfirmation condition |
|---|---|---|---|---|
| P1 | Address classifier assigns every published SM+CM excitation a consistent statistics-phase address | [CHECK: 2028] | Classifier SDK + catalog audit | ≥1 catalog entry with unresolvable phase address (misses reported, not hidden) |
| P2 | New abelian anyon system: measured phase θ = e^{2πi p/q}, q prime (ramified branch) | [CHECK: 2029] | FQH/moiré interferometry (external) | Phase measured that is NOT a root of unity (F3) |
| P3 | Weakly-interacting composite catalog fits N_C* rational functions within 1% | [CHECK: 2027] | Band-structure data, k·p theory | Any weak-coupling composite with >1% non-rational residual |
| P4 | Place-parameterized calculus reproduces Laughlin e^{2πi/3} + abelian FQH braid phases, no ad-hoc inputs | [CHECK: 2028] | Implementation + ≥3 published braid experiments | Per-system phase inputs required |
| P5 | ≥1 CM quasiparticle maps onto a previously unassigned SM pattern class | [CHECK: 2030] | Table audit | No cross-catalog overlap beyond trivial ±1 |

## 2b. PAPER FALSIFIABILITY MIRROR (paper §9, F1–F4 — added v0.3 per red-team S7)

| ID | Condition | Status |
|---|---|---|
| F1 | A fundamental particle with a statistics phase that is NOT a tree-automorphism phase (e.g., fundamental fermion with integer spin, or statistics outside the root-of-unity set) falsifies the statistics reading | active, ongoing |
| F2 | A weakly interacting composite quasiparticle whose N_C* is not a rational function of the background counts falsifies the quasiparticle reading (strongly-correlated scales exempt by stated scope) | active, ongoing |
| F3 | A physical system exhibiting braid statistics with a phase that is not a root of unity falsifies the anyon reading (abelian scope) | [CHECK: 2036] |
| F4 | A Standard-Model particle that cannot be assigned a unique tree address consistent with its spin, charge sector, and statistics falsifies the table | active, ongoing |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

- FQ1 disconfirmed if: a UMTC with no BT-building representation is proven to realize physical anyons.
- FQ2 disconfirmed if: the automorphism group's characters cannot host {±1} ∪ cyclotomic phases.
- FQ3 disconfirmed if: no adelic evaluation reproduces the SM statistics column (exact ±1, Sₙ).
- FQ4 disconfirmed if: for every candidate measurement, a non-tree framework predicts identical outcomes (indispensability false).
- FQ5 disconfirmed if: heavy-fermion m* is shown non-algebraic (transcendental) in the couplings.
- FQ6 disconfirmed if: any abelian braid experiment contradicts the calculus's output.

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|---|---|---|---|---|
| REG-UMP013-001 | A new abelian anyon system's phase = e^{2πi p/q}, q prime (ramified branch valuation) | Phase outside roots of unity | Interferometry publication, ≥3 independent groups | 2029-12-31 |
| REG-UMP013-002 | Ising/Fibonacci anyon data embeds in automorphism representations of a BT building | No embedding exists | Category-theoretic construction + check | 2030-12-31 |

## 5. CALIBRATION REGISTER (all entries, this project)

P1 0.80 [CAP] · P2 0.80 · P3 0.80 [CAP] · P4 0.70 · P5 0.60 · BC1 0.35 · BC2 0.20 · BC3 0.10 · BC4 0.15 (anchors in artifacts/likelihood-calibration.md, artifacts/structured-forecast.md, artifacts/counterfactual-backcasting.md).

## 6. NEXT ACTIONS (Prioritized)

- P0: v0.3 remediation (red-team RT-H1..H4 + S1/S2/S3/S7) — executed 2026-08-19, see session log.
- P0: FQ2 automorphism-group specification (feeds claim 2 wording).
- P1: Classifier SDK prototype (Stage 9 A2) — after publication.
- P1: FQ5 heavy-fermion data collection (external literature).
- P2: FQ1 category-theoretic construction (external collaboration).

## 7. SESSION LOG + MAINTENANCE PROTOCOL

- 2026-08-19: registry created at Phase 4 (commit pending — see git log); entries FQ1-FQ6, P1-P5, REG-001/002, calibration rows.
- 2026-08-19 (v0.3): post-publication red-team remediation — RT-H1..H4 fixed (frontmatter version, README DOI, core-claim.md added to source set, Declarations rewrite); S1 adelic-program concept 21691414 (bib + citation-audit); S2 evidence-file renames (5); S3 citation-audit refresh; S7 F1-F4 mirror added (§2b).
- 2026-08-19 (v0.3 residual, SOFT): published v0.3 paper reference [32] still cites version record 21698355 while references.bib cites concept 21691414 — repo patched; v0.4 candidate (or accept: both resolve; version-record citation of a version-titled work).
- 2026-08-20 (v0.4): round-3 red-team closeout — all 33 refs cited in body (S2: [13][14] in §3, [19] in §10.3, [33] in §2.2); provenance note corrected to [23]-[33] (S4); unattested "F. Wilczek" chapter attribution corrected to Crossref-attested volume author Alberto Lerda in paper [20] + bib key lerda1992anyons (S5); README license line added (S6); [32] concept 21691414 shipped in published record (S1 closed); KG node + R2 re-synced (H1/H2); junk files deleted (H3).
- Maintenance: bump version + log entry at every phase gate; cross-reference companion registries (ODR/QP: QNFO/odr-thesis RESEARCH-CONTINUITY-REGISTRY.md).
