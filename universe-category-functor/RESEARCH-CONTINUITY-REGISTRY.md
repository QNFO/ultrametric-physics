# RESEARCH CONTINUITY REGISTRY — Universe Category Functor (QNFO.UMP.006)

**Maintained:** 2026-08-10 — living document, version-bumped with each session.

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | Does the functor \(F: \mathcal{P} \to \mathcal{M}\) encode quantization, stability, AND factorization as ONE categorical object? | OPEN — core synthesis claim (B1) | Formalize B2 (∞-category extension) | YES |
| FQ2 | Does multiplicity (prime powers) matter? \(F(8)=F(2)=S^1\) — can a "Universe Category" distinguish them? | OPEN — Adversary 4 objection | Address in paper; consider graded enrichment | YES |
| FQ3 | Does the functor factor through the adelic ring \(\mathbb{A} = \mathbb{R} \times \prod_p \mathbb{Q}_p\) (adelic-scheme reframing)? | OPEN | Reframe as "computable shadow of adelic object" | YES |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument | Disconfirmation Condition |
|:---|:-----------|:------------|:-----------|:--------------------------|
| P1 | Homology rank of \(F(n)\) = \(2^{\omega(n)}\) for all square-free n | 2026 (computable now) | Python/coq (notebooks/functor_formalization.py) | Any square-free composite yields rank ≠ \(2^k\) → framework wrong (D1) |
| P2 | Modular-curve-topology system exhibits quantized behavior | 2027-2030 | Metamaterial experiment | No quantization at predicted scale → quantization leg falsified (D2) |
| P3 | Bruhat-Tits quantum state space preserves ultrametric error bound | 2028-2032 | Ultracold-atom treelike system | Bound violated → stability leg falsified (D3) |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

| RQ | Disconfirmed if |
|:---|:----------------|
| FQ1 | The three legs are shown to be categorically distinct after formalization (no common object) |
| FQ2 | Physical predictions require distinguishing n from p^a in a way the functor cannot express |
| FQ3 | No categorical construction factors the functor through Spec(Z)-torsion / adelic ring |

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|:---|:-----------|:--------------|:-----|:---------|
| REG-UMP006-001 | \(F\) is a functor with rank \(2^{\omega(n)}\) | Any morphism-preservation or rank failure | notebooks/functor_formalization.py | 2026-08-20 |
| REG-UMP006-002 | Prime-power criterion: n prime power iff rank = 2 | Counterexample | Same notebook | 2026-08-20 |
| REG-UMP006-003 | Three-leg synthesis conjecture | Formal categorical distinctness proof | Future ∞-category extension | 2027-12-31 |

## 5. CALIBRATION REGISTER

```
[CHECK: 2027-06] D1 computation verified for all square-free n < 10^6.
Strength: [STRONG] | Status: [DONE 2026-08-10 for n <= 100000 — extend bound]

[CHECK: 2028] ≥1 independent group engages with the "Universe Category" conjecture.
Strength: [MEDIUM] | Status: [PENDING]

[CHECK: 2029] Adelic-scheme reframing shown (functor factors through Spec(Z)-torsion).
Strength: [MEDIUM] | Status: [PENDING]

[CHECK: 2030] Experimental signature (prime-indexed mass-ratio structure) confirmed independently.
Strength: [STRONG] | Status: [PENDING]
```

## 6. NEXT ACTIONS (Prioritized)

| Priority | Action | Target |
|:---------|:-------|:-------|
| P0 | Extend D1 computation to n < 10^6 (formal proof-quality bound) | 2026-08-11 |
| P0 | Author Phase 5 paper `<slug>.md` with honest [RETRODICTION] labels | 2026-08-18 |
| P1 | Address Adversary 4 (multiplicity) in paper §Obstructions | 2026-08-18 |
| P1 | Write RESEARCH-CONTINUITY-REGISTRY into published artifact | Phase 5 closeout |
| P2 | ∞-category extension for B2 | 2027 Q1 |

## 7. SESSION LOG

| Date | Session | Action |
|:-----|:--------|:-------|
| 2026-08-10 | this | P0-P4: init, diligence, consilience, classification, citations, forecast, KIF-60, D1 computation. Commits 84527e3..55cce69. |
