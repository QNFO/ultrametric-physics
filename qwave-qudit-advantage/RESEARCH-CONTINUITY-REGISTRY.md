# RESEARCH-CONTINUITY-REGISTRY

**Project:** QNFO.UMP.005 — qwave-qudit-advantage (The Qudit Advantage: JPCUB Comparison of QWAV vs. Conventional Qubit Platforms)
**Canonical DOI:** 10.5281/zenodo.21827737 (v0.4)
**Version chain:** 21826596 (v0.1) → 21826679 (v0.1-fix) → 21827268 (v0.2) → 21827347 (v0.3) → 21827737 (v0.4)
**Created:** 2026-08-06 (research v2.64 HARD gate — post-publication registry)
**Maintained:** LIVING DOCUMENT — updated on every version bump, correction, or external-engagement event

---

## 1. FRONTIER RESEARCH QUESTIONS

| ID | Question | Status | Next Action | Pre-Reg Suitable |
|:---|:---------|:-------|:------------|:-----------------|
| FQ1 | What is the minimum qudit dimension $d^*$ at which the encoding-density benefit definitively exceeds the per-gate fidelity penalty? (paper estimate: $d^* \approx 3$ under conservative assumptions) | OPEN | Derive rigorous error-propagation model for qudit QEC codes; bound $d^*$ from below | YES |
| FQ2 | Can the $\mathcal{O}(\log_p N)$ vs. $\mathcal{O}(N^2 \log N)$ decoding-complexity gap between hierarchical tree decoders and planar-lattice decoders be proven as a LOWER BOUND advantage (topological), or is it contingent (algorithmic — e.g., defeated by preprocessing)? | OPEN | Complexity-theoretic proof attempt; check whether planar decoders can reach sub-exponential via preprocessing | YES |
| FQ3 | What physical substrates support $d \geq 3$ qudits with coherence times sufficient for fault-tolerant computation at $T = 300$ K? (ultrametric error model predicts passive separation by valuation depth) | OPEN | Literature scan for room-temperature qudit candidates; experimental validation needed | YES |

## 2. FALSIFIABLE PREDICTIONS

| ID | Prediction | Test Window | Instrument / Protocol | Disconfirmation Condition |
|:---|:-----------|:------------|:----------------------|:--------------------------|
| P1 | A physical qudit platform with $d = 3$ achieves $J_{\text{CUB}} < 0.05$ J/sol | 2027–2030 | JPCUB P0 adversarial validation protocol | Measured $J_{\text{CUB}} > 0.05$ J/sol under adversarial validation |
| P2 | A physical qudit platform with $d = 7$ achieves $J_{\text{CUB}} < 10^{-4}$ J/sol | 2028–2032 | JPCUB P0 adversarial validation protocol | Measured $J_{\text{CUB}} > 10^{-4}$ J/sol |
| P3 | An external group independently computes a JPCUB for a qudit platform and the result is within $10\times$ of this paper's estimate | 2027–2030 | Independent replication (any group) | No external JPCUB for any qudit platform published by 2030 |

## 3. PER-RQ FALSIFIABILITY CONDITIONS

| RQ | Disconfirmed if... |
|:---|:-------------------|
| FQ1 ($d^*$) | A $d \geq 5$ qudit platform under adversarial validation measures $J_{\text{CUB}} > 0.05$ J/sol (encoding-density benefit neutralized at high $d$) |
| FQ2 (decoder gap) | A planar-lattice decoder achieves sub-exponential complexity at $N > 10^6$ without hierarchical structure |
| FQ3 (room-temp) | No $d \geq 3$ qudit platform with fault-tolerant-grade coherence is demonstrated at 300 K by 2032 |

## 4. PRE-REGISTRATION SCAFFOLDS

| ID | Hypothesis | Falsification | Data | Deadline |
|:---|:-----------|:--------------|:-----|:---------|
| REG-UMP005-001 | JPCUB(qudit, $d=3$) < JPCUB(best superconducting qubit) = 0.05 J/sol | Measured $J_{\text{CUB}} \geq 0.05$ J/sol for a $d=3$ platform | Energy metering + timing of a $d=3$ qudit platform under JPCUB P0 protocol | 2030-12-31 |
| REG-UMP005-002 | Dimensional advantage is robust at $d \geq 5$ against the fidelity-overhead factor | $f_{\text{OH}}(d) \geq 10$ at $d=5$ (overhead dominates encoding gain) | Gate-fidelity measurements at $d=5$ | 2032-12-31 |
| REG-UMP005-003 | Ultrametric tree decoder achieves sub-exponential decode latency on real error syndromes | Decoder latency scales polynomially with code distance on Bruhat-Tits tree codes | Decoder benchmark on simulated syndromes | 2031-12-31 |

## 5. CALIBRATION REGISTER

```
[CHECK: 2027] This paper's qudit JPCUB estimate survives adversarial validation
  per JPCUB P0 protocol — independent red-team reproduces the computation.
Strength: [STRONG] | Status: [PENDING]

[CHECK: 2028] At least one external group computes a JPCUB for a qudit platform
  (trapped-ion qudit, photonic qudit, or Rydberg qudit) and the result is
  consistent with this paper's dimensional-advantage prediction.
Strength: [WEAK] | Status: [PENDING]

[CHECK: 2029] A physical qudit processor ($d > 2$) demonstrates a measured
  joules-per-solution below the 2026 superconducting-qubit floor ($0.05$ J/sol).
Strength: [STRONG] | Status: [PENDING]
```

## 6. NEXT ACTIONS (Prioritized)

| Priority | Action | Dependency | Target |
|:---------|:-------|:-----------|:-------|
| P0 | Monitor outreach replies (Ringbauer, Kais, Tavernelli, Heydeman, Lei — sent 2026-08-06) | External response time | ongoing |
| P0 | Re-evaluate journal submission (deferred 2026-08-06; cronjob `qwave-qudit-journal-reconsider` fires 2026-11-06) | 3-month reminder | 2026-11-06 |
| P1 | FQ1: qudit QEC error-propagation model to bound $d^*$ | — | 2027 |
| P1 | FQ2: complexity-theoretic lower-bound attempt for tree decoders | — | 2027 |
| P2 | FQ3: room-temperature qudit substrate literature scan | — | 2027 |
| P2 | Post-acceptance (IF journal submission later succeeds): newversion v0.5 with `related_identifiers: isPublishedIn` | Journal decision | conditional |

## 7. SESSION LOG + MAINTENANCE PROTOCOL

| Date | Event | Registry Action |
|:-----|:------|:----------------|
| 2026-08-06 | Publication v0.4 (DOI 10.5281/zenodo.21827737); outreach sent; journal deferred | Registry created (research v2.64 HARD gate) |

**Maintenance protocol:** update this registry on every (a) version bump, (b) correction (ERRATA), (c) external engagement (outreach reply, citation, PhilPapers indexing), (d) journal submission outcome, (e) any new frontier question or prediction arising from the work. Version bumps require re-verification that prediction text matches the published paper's Section 5.

**Cross-references:** paper §5 (Calibration Register and Frontier Questions), ERRATA.md (BP-4 correction record), artifacts/outreach-log.md (external engagement), artifacts/journal-submission-strategy.md (deferral decision + triggers).
