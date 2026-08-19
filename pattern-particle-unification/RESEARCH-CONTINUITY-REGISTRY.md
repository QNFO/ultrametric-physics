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

- P0: Phase 5 publication (spec-sheet + REG scaffolds on Zenodo) — dependency: this registry + Phase 4 artifacts.
- P0: FQ2 automorphism-group specification (feeds claim 2 wording).
- P1: Classifier SDK prototype (Stage 9 A2) — after publication.
- P1: FQ5 heavy-fermion data collection (external literature).
- P2: FQ1 category-theoretic construction (external collaboration).

## 7. SESSION LOG + MAINTENANCE PROTOCOL

- 2026-08-19: registry created at Phase 4 (commit pending — see git log); entries FQ1-FQ6, P1-P5, REG-001/002, calibration rows.
- Maintenance: bump version + log entry at every phase gate; cross-reference companion registries (ODR/QP: QNFO/odr-thesis RESEARCH-CONTINUITY-REGISTRY.md).
