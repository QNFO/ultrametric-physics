# Bayesian Evidential Weight Report — QNFO.UMP.005

**Paper:** qwave-qudit-advantage
**Date:** 2026-08-06
**Gate:** KIF-60 (HARD — Bayesian Evidential Weight Gate)

---

## 1. Claim Audit

Each claimed correspondence or finding audited for Δlog-odds.

### Claim 1: Qudit encoding density ($\log_2 d$ bits/carrier) yields $N_{\text{phys}}$ reduction

| Test | Result |
|:-----|:-------|
| **Pre-registration** | ❌ NOT pre-registered — Shannon (1948) predates this paper by 78 years. The $\log_2 d$ identity is a mathematical theorem, not a prediction. |
| **Falsifiability condition** | If any $d$-level quantum system carried *less* than $\log_2 d$ qubit-equivalent bits → the identity would be mathematically contradicted. This is impossible. |
| **Surprise accounting** | $P(\text{match} \mid \text{random}) \approx 1$ — this is a definitional identity. |
| **Δlog-odds** | $\approx 0$ |
| **Classification** | **[RETRODICTION — not evidence]** — a coding-theory identity presented as a finding. The paper correctly presents it as background (Section 2.2), not a discovery. |

### Claim 2: Hierarchical decoder complexity $\mathcal{O}(\log_p N)$ vs. $\mathcal{O}(N^2 \log N)$

| Test | Result |
|:-----|:-------|
| **Pre-registration** | ❌ NOT pre-registered — the complexity analysis post-dates this paper's framing. |
| **Falsifiability condition** | If a planar-lattice decoder achieves sub-exponential complexity on a surface-code lattice → the tree-decoder advantage is algorithmic, not topological. |
| **Surprise accounting** | $P(\text{match} \mid \text{random}) \approx 0.3$ — hierarchical structures with sub-exponential traversal are well-known in CS (tries, B-trees). The isomorphism is not surprising once the structure is identified. |
| **Δlog-odds** | Low positive |
| **Classification** | **[SPECULATIVE — requires adversarial validation]** — the paper correctly labels the decoder as [speculative] (Section 3.3). |

### Claim 3: Passive error resilience eliminates ancilla overhead + cooling energy

| Test | Result |
|:-----|:-------|
| **Pre-registration** | ❌ NOT pre-registered |
| **Falsifiability condition** | If ultrametric error separation degrades under realistic noise models to the point where active QEC overhead is still required → passive resilience claim falsified. |
| **Surprise accounting** | $P(\text{match} \mid \text{random}) \approx 0.2$ — error separation by metric distance is standard QEC but the ultrametric specific claim that separation is *passive* (no syndrome extraction) is novel and untested. |
| **Δlog-odds** | $\approx 0$ (no pre-registration) |
| **Classification** | **[SPECULATIVE — not yet evidence]** — the paper correctly labels claims involving passive resilience as [speculative]. |

### Claim 4: Room-temperature qudit operation at 300 K

| Test | Result |
|:-----|:-------|
| **Pre-registration** | ❌ NOT pre-registered |
| **Falsifiability condition** | If no physical qudit platform at $d \geq 3$ achieves coherence times sufficient for fault-tolerant operation at 300 K by 2032 → claim falsified. |
| **Surprise accounting** | $P(\text{match} \mid \text{random}) \approx 0.05$ — no existing qudit processor operates at room temperature with fault-tolerant coherence times. This is a genuinely surprising claim if confirmed. |
| **Δlog-odds** | $\approx 0$ (no pre-registration) |
| **Classification** | **[SPECULATIVE]** — the paper correctly labels the 300 K assumption as [speculative] (Section 4.2). |

### Claim 5: JPCUB crossover at $d^* \approx 3$

| Test | Result |
|:-----|:-------|
| **Pre-registration** | ✅ PRE-REGISTERED — Section 5.1, Prediction P1: "A physical qudit platform with $d = 3$ achieves $J_{\text{CUB}} < 0.05$ J/sol." Timestamped with this paper. |
| **Falsifiability condition** | Measured $J_{\text{CUB}} > 0.05$ J/sol under adversarial validation → falsified. Explicitly stated in Section 1.2 and Section 5.1. |
| **Surprise accounting** | $P(\text{match} \mid \text{null}) \approx 0.1$ — under the null hypothesis that dimensional advantage is neutralized by overhead, the probability of $J_{\text{CUB}} < 0.05$ is low. A positive result would be surprising. |
| **Δlog-odds** | $\Delta \approx \log(0.9/0.1) \approx 2.2$ → **positive evidential weight if confirmed** |
| **Classification** | **[RISKY PREDICTION — carries evidential weight]** — this is the paper's only claim that qualifies as a genuine pre-registered prediction per KIF-60. |

---

## 2. Summary

| Claim | Δlog-odds | Classification |
|:------|:----------|:---------------|
| $\log_2 d$ encoding density | $\approx 0$ | [RETRODICTION — not evidence] |
| Hierarchical decoder complexity | Low positive | [SPECULATIVE — not yet evidence] |
| Passive error resilience | $\approx 0$ | [SPECULATIVE — not yet evidence] |
| Room-temperature operation | $\approx 0$ | [SPECULATIVE — not yet evidence] |
| **JPCUB crossover $d^* \approx 3$** | **$\approx 2.2$ (if confirmed)** | **[RISKY PREDICTION — carries evidential weight]** |

**1/5 claims carries positive evidential weight as a pre-registered prediction.** This is acceptable for a theoretical model paper whose primary output is a falsifiable prediction, not a confirmed finding. The paper correctly distinguishes retrodictions from predictions and labels speculative claims appropriately.

---

## 3. Tautology Trap Audit (Post-Paper)

| Trap | Status | Evidence |
|:-----|:-------|:---------|
| **Overfitting** | ⚠️ MONITOR — 4 free parameters ($d$, $f_{\text{OH}}$, $P_{\text{phys}}$, decoder complexity exponent) vs. 17 JPCUB data points. dof < data → not overfitted. | The sensitivity analysis (Section 3.7) varies $d$ and shows the crossover is robust at $d \geq 5$. |
| **Cherry-Picking** | ⚠️ MONITOR — the comparison table (Section 3.6) includes all three qubit families (SC, neutral-atom, trapped-ion), not just the worst-performing. | The full Landscape v2.0 table is cited. |
| **Absorption** | ⚠️ MONITOR — if a measured JPCUB exceeds the qubit floor, the paper MUST NOT absorb this with "the dimensional advantage is masked by [new parameter]" without pre-registering the parameter. | The falsification condition (Section 1.2) is unambiguous: $J_{\text{CUB}} > 0.05$ J/sol → advantage falsified. No absorption escape clause. |

---

## 4. Gate Verdict

**KIF-60: PASS.** 1/5 claims carries positive evidential weight as a pre-registered prediction (P1: $d^* \approx 3$ crossover). 4/5 claims are correctly classified as retrodiction or speculative. All speculative claims are labeled `[speculative]` in the paper. The falsification condition is explicit and pre-registered.
