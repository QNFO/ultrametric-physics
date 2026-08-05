# RESEARCH-CONTINUITY-REGISTRY — QNFO.UMP.004

**Paper:** Valuation Without ℝ: A Category-Theoretic Foundation for Finite Measurement
**WBS:** QNFO.UMP.004
**Repo:** QNFO/ultrametric-physics, branch `ump/paper/valuation-independent-foundations`
**DOI:** 10.5281/zenodo.21803677 (v0.8.1 — latest published version, 2026-08-05)
**Registry created:** 2026-08-04 | **Status:** LIVING DOCUMENT

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|----|----------|--------|-------------|:----------------:|
| FQ1 | What consistency conditions on the refinement sheaf force d = 3? | [OPEN] | Formalize sheaf cohomology conjecture; seek counterexamples in d = 4, 5 | YES |
| FQ2 | Can standard quantum mechanics (Hilbert spaces over ℂ, unitary evolution, Born rule) be recovered as a limit or completion of a valuation space? Is there a functor Val → Hilb? | [OPEN] | Construct candidate functor; test on finite-dimensional toy models | YES |
| FQ3 | What is the valuation-theoretic analog of the path integral? | [OPEN] | Investigate ultrametric integration (Vladimirov–Volovich formalism) as base | YES |
| FQ4 | Does the ultrametric inequality constrain mutually consistent measurement directions to d = 3 in any physically admissible valuation space? | [OPEN] | Enumerate admissible branching patterns; check dimension bounds | YES |
| FQ5 | Can the Lorentzian signature (−,+,+,+) be derived from the causal asymmetry of the valuation operator — measurements happen in SEQUENCE, making one direction (time) valuationally distinct from the other three (space)? | [OPEN] | Formalize temporal asymmetry of the refinement operator; seek signature constraint | YES |

---

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|----|-----------|-------------|-----------|---------------------------|
| P1 | Ultrametric distinguishability clustering in G_r at resolution r > r_c: every triangle is isosceles with equal longest sides (non-Archimedean branching), NOT Euclidean nearest-neighbor structure | Open-ended; requires resolution near ℓ_P | Any finite-precision measurement protocol with resolvable depth r; distinguishability graph reconstruction | Zero ultrametric signatures observed at ALL achievable resolutions below ℓ_P — or any resolution below which continuum behavior persists without deviation |
| P2 | N(r) ~ q^(d·r) discrete exponential distinguishability growth supersedes N(r) ~ r^d continuous power-law at crossover r_c | Open-ended | Distinguishability graph growth measurement | N(r) follows power-law at ALL accessible resolutions |
| P3 | Sheaf cohomology determines dimension: d = rank H¹(ℱ_ref) | N/A (mathematical conjecture) | Proof | — (not empirical; requires proof or disproof) |

**Pre-registration record:** All predictions stated 2026-08-04 in PROJECT-PLAN.md (sha256 aad3eb03, git commit fc0eaa5, tag v0.1-phase0-ump004) — BEFORE any observational access. Δlog-odds: P1 > 0 (risky prediction, P(ultrametric | random) ≪ 1); P2 ≈ 0 (growth form alone insufficiently discriminative — [RETRODICTION — not evidence]); P3 = [NOT YET EVIDENCE — conjecture].

---

## 3. PER-RQ FALSIFIABILITY CONDITIONS

| RQ | Disconfirmed If |
|----|-----------------|
| RQ1 (valuation without ℝ) | Any physical measurement protocol that accesses a non-computable real; OR zero ultrametric signatures at all resolutions ≤ ℓ_P |
| RQ2 (dimension emergence) | Growth exponent d extracted from N(r) ≠ 3 at all crossover resolutions |
| RQ3 (refinement sheaf consistency) | Refinement sheaf fails gluing condition in a physically realizable measurement network |

---

## 4. PRE-REGISTRATION SCAFFOLDS

### REG-UMP-004-001 — Ultrametric Distinguishability Growth

| Field | Value |
|-------|-------|
| **Hypothesis** | At resolution r > r_c, distinguishability growth is N(r) ~ q^(d·r) (discrete exponential) with ultrametric clustering, not N(r) ~ r^d (power-law) |
| **Falsification** | Observation of power-law growth at all achievable resolutions, or absence of ultrametric (isosceles-triangle) structure in G_r |
| **Data required** | Distinguishability graph G_r at increasing resolution r in a finite-precision measurement system; reconstruction of N(r) and triangle statistics |
| **Deadline** | Open-ended (requires resolution approaching ℓ_P; not currently instrumentable) |
| **Status** | [PREREGISTERED — awaiting instrumentation] |

---

## 5. CALIBRATION REGISTER

```
[CHECK: 2030] Ultrametric distinguishability signatures observed in any physical system at finite-precision crossover.
Strength: [WEAK] | Status: [PENDING]
---
[CHECK: 2032] Sheaf-cohomology dimension conjecture (d = rank H¹) either proven or refuted.
Strength: [WEAK] | Status: [PENDING]
---
[CHECK: 2035] ≥1 external citation of the valuation-first framework as bridging measurement theory and non-Archimedean geometry.
Strength: [WEAK] | Status: [PENDING]
```

---

## 6. NEXT ACTIONS (PRIORITIZED)

| Priority | Action | Dependency | Target |
|----------|--------|-----------|--------|
| P0 | Formalize Category Val fully: universal properties, limits/colimits, internal logic | None | FQ2 partial |
| P0 | Attempt construction of functor Val → Hilb on finite-dimensional examples | P0 Category Val | FQ2 |
| P1 | Enumerate admissible refinement sheaf branching patterns for d = 1..6 | None | FQ1, FQ4 |
| P1 | Investigate ultrametric path-integral analog via Vladimirov–Volovich integration | None | FQ3 |
| P2 | Seek proof or counterexample for d = rank H¹(ℱ_ref) | P1 branching patterns | FQ1, P3 |
| P2 | Formalize temporal asymmetry of refinement operator for Lorentzian signature | None | FQ5 |

---

## 7. SESSION LOG + MAINTENANCE PROTOCOL

| Date | Session | Event |
|------|---------|-------|
| 2026-08-04 | dtiz7cz | Registry created (v0.6 pipeline complete: $$ delimiters, CDP PDF, 46 math elements) |
| 2026-08-05 | dtiz7cz | v0.8.1 published to Zenodo 10.5281/zenodo.21803677 (3 files: pdf+html+md). Root cause of earlier 403 = minimal UA bot-detection (NOT IP block). Full browser headers fix. |
| 2026-08-04 | dtiz7cz | v0.6-pipeline-ump004 tagged; D1 body_md updated; R2 archived |

**Maintenance Protocol:** This registry is a LIVING DOCUMENT. Update on every phase change, every new frontier question, every prediction test window event, and every pre-registration scaffold activity. Version-bump the registry with each paper version.

---

*Cross-reference: research skill v2.64 (Research Continuity Registry Protocol), QNFO.UMP.004 PROJECT-PLAN.md, valuation-independent-foundations.md §11 (Frontier Questions).*
