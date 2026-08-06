# Phase 2 Literature Review — QNFO.UMP.005

**Paper:** The Qudit Advantage: JPCUB Comparison of QWAV vs. Conventional Qubit Platforms
**Slug:** qwave-qudit-advantage
**Date:** 2026-08-06
**Status:** COMPLETE
**Gate:** KIF-18 (HARD — Mandatory Symmetry Template)

---

## 1. Multi-Source Search Summary

8 sources queried during Phase 1 due diligence. Results re-used for Phase 2 classification.

| Source | Query | Results | Evidence File |
|:-------|:------|:--------|:--------------|
| OpenAlex | qudit quantum advantage | 2,921 | `openalex_qudit_advantage.json` |
| OpenAlex | qudit vs qubit comparison | 1,389 | `openalex_qudit_vs_qubit.json` |
| OpenAlex | p-adic QEC qudit | 23 | `openalex_padic_qec_qudit.json` |
| OpenAlex | qudit dimensional scaling | varies | `openalex_qudit_scaling.json` |
| Crossref | qudit quantum | 8 relevant | `crossref_qudit_quantum.json` |
| Zenodo | qudit | 153 | `zenodo_qudit.json` |
| Zenodo | QWAV | 163 | `zenodo_qwav.json` |
| arXiv | qudit quantum advantage | 10 | `arxiv_qudit_advantage.txt` |

**Deduplication:** Crossref and OpenAlex have overlapping coverage; OpenAlex is the primary index for citation counts. Zenodo captures grey literature; arXiv captures preprints. QNFO internal papers (JPCUB P0, JPCUB Landscape v2.0, Ultrametric Metrology, QEC Darwinism) are classed separately.

---

## 2. Classification Matrix

### Core (directly addresses the research question — 7 papers)

| # | Paper | Year | Citations | DOI | Why Core |
|:--|:------|:-----|:----------|:----|:---------|
| C1 | Qudits and High-Dimensional Quantum Computing (Wang et al.) | 2020 | 493 | 10.3389/fphy.2020.589504 | Foundational review of qudit quantum computing — covers encoding density, gate synthesis, error correction, applications. Primary reference for the qudit literature. |
| C2 | A universal qudit quantum processor with trapped ions (Ringbauer et al.) | 2022 | 365 | 10.1038/s41567-022-01658-0 | First experimental demonstration of a universal qudit quantum processor. Uses trapped-ion $d=7$ qudits. Essential for physical-implementation energy model. |
| C3 | Efficient realization of quantum algorithms with qudits (Low et al.) | 2024 | 35 | 10.1140/epjqt/s40507-024-00250-0 | Most recent comprehensive qudit compilation study — quantifies gate-count reduction from qudit encoding. Direct input to algorithmic-overhead component of JPCUB. |
| C4 | Unconditional advantage of noisy qudit quantum circuits over biased threshold circuits (2025) | 2025 | <10 | 10.1038/s41467-025-58545-4 | Proves unconditional advantage for qudit circuits in the noisy regime — directly supports the "qudit advantage is structural, not contingent" claim. |
| C5 | JPCUB P0: Joules Per Solution — An Energy-Based Framework for Benchmarking Quantum Computer Architectures | 2026 | — | 10.5281/zenodo.21637028 | The foundational JPCUB framework. Defines $J_{\text{CUB}} = P_{\text{sys}} \cdot t_{\text{sol}}$, adversarial validation protocol, and the JPCUB metric. Our paper extends this to qudits. |
| C6 | JPCUB Competitive Landscape v2.0 (QNFO) | 2026 | — | 10.5281/zenodo.21821767 | Direct predecessor — 17 qubit platforms benchmarked. Our paper adds the 18th row: QWAV qudits. |
| C7 | Practical trapped-ion protocols for universal qudit-based quantum computing | 2020 | 116 | 10.1103/physrevresearch.2.033128 | Detailed gate-protocol specifications for trapped-ion qudits — provides physical gate-time and fidelity estimates for the JPCUB model. |

### Supporting (adjacent work — 8 papers)

| # | Paper | Year | Citations | DOI | Why Supporting |
|:--|:------|:-----|:----------|:----|:---------------|
| S1 | Hardware Efficient Quantum Simulation of Non-Abelian Gauge Theories with Qudits on Rydberg Platforms | 2022 | 142 | 10.1103/physrevlett.129.160501 | Demonstrates qudit advantage for lattice gauge theory simulation — supports the "qudit = natural for gauge theories" argument. |
| S2 | Qudit surface codes and hypermap codes | 2023 | <10 | 10.1007/s11128-023-04060-8 | Extends surface code QEC to qudits — provides error-threshold estimates for qudit QEC, relevant for the decoder energy model. |
| S3 | Universal Qudit Gate Synthesis for Transmons | 2023 | 61 | 10.1103/prxquantum.4.030327 | Superconducting qudit gate synthesis — useful for comparing physical-gate energy across qubit vs qudit superconducting platforms. |
| S4 | Tensor networks, $p$-adic fields, and algebraic curves (Heydeman et al.) | 2018 | 56 | 10.4310/atmp.2018.v22.n1.a4 | Connects $p$-adic geometry to tensor networks — supports the Bruhat-Tits tree as a natural tensor-network substrate for QEC. |
| S5 | Nonarchimedean holographic entropy from networks of perfect tensors | 2021 | 21 | 10.4310/atmp.2021.v25.n3.a2 | Extends the $p$-adic tensor network framework — supports the holographic entropy argument for ultrametric QEC. |
| S6 | A programmable qudit-based quantum processor (Chi et al.) | 2022 | 264 | 10.1038/s41467-022-28767-x | Programmable qudit processor with photonic qudits — provides alternative physical implementation for qudit energy model. |
| S7 | QudCom: Towards Quantum Compilation for Qudit Systems | 2024 | <10 | arXiv | Compilation framework for qudits — supports the algorithmic-overhead reduction claim. |
| S8 | Scalable quantum computing with qudits on a graph | 2020 | <10 | 10.1103/physreva.101.022304 | Graph-based qudit architecture — topologically adjacent to Bruhat-Tits trees. |

### Background (context, foundations — 5 papers)

| # | Paper | Year | Citations | DOI | Why Background |
|:--|:------|:-----|:----------|:----|:---------------|
| B1 | A Mathematical Theory of Communication (Shannon) | 1948 | 150,000+ | — | Foundational for $\log_2 d$ per-symbol information content — cited in consilience gate as the 78-year silo. |
| B2 | Irreversibility and Heat Generation in the Computing Process (Landauer) | 1961 | 10,000+ | — | Landauer bound $E \geq k_B T \ln 2$ — energy floor for information erasure. Foundation for JPCUB energy model. |
| B3 | Trie Memory (Fredkin) | 1960 | 1,000+ | — | Radix trie data structure — structurally isomorphic to Bruhat-Tits tree traversal. Cited in consilience gate. |
| B4 | Fault-tolerant quantum computation (Shor) | 1996 | 5,000+ | 10.1103/PhysRevA.52.R2493 | First fault-tolerance threshold theorem — foundation for all QEC overhead estimates. |
| B5 | Topological quantum memory (Kitaev) | 2003 | 6,000+ | 10.1016/S0003-4916(02)00018-0 | Surface codes — the dominant qubit QEC paradigm. Baseline for comparison against ultrametric QEC. |

### QNFO Internal (predecessor papers — 4 papers)

| # | Paper | WBS | Relevance |
|:--|:------|:----|:----------|
| Q1 | Ultrametric Metrology: Passive Error Resilience Through Ultrametric Geometry | QNFO.UMP.002 | Error model for qudit JPCUB — provides the ultrametric error-resilience quantification |
| Q2 | QEC Darwinism on Bruhat-Tits Trees: Hierarchical Decoding | QNFO.UMP.004 | Decoder energy model — provides the hierarchical-decode complexity and energy estimates |
| Q3 | Adelic Core Synthesis: Cross-Domain Framework | — | p-adic stabilizer code formalism — provides the mathematical framework for qudit QEC codes |
| Q4 | Continuum Trilogy Paper I: The Computable Physical Continuum | — | Ostrowski-place democracy — provides the philosophical foundation for dimensionless JPCUB |

### Reject (irrelevant, retracted, or duplicate — 0 papers)

No papers rejected. The search was focused on qudit quantum computing, and even peripheral results (Bloch vectors for qudits, frequency-encoded photonic qubits) provide useful background or contrast.

---

## 3. KIF-18 Mandatory Symmetry Template

### Where External Literature Supports the Core Claim

**Claim:** The QWAV qudit architecture achieves a JPCUB advantage over conventional qubit platforms through dimensional encoding density, ultrametric hierarchical decoding, and passive error resilience.

#### Supporting Evidence from External Literature

1. **Dimensional encoding density ($\log_2 d$ bits per carrier)**
   - Wang et al. (2020, C1): "Qudits offer a larger state space for storing and processing quantum information, enabling more efficient encoding of quantum algorithms" (Front. Phys. 2020, 493 citations). This is the consensus external position — qudits carry more information per physical carrier.
   - Low et al. (2024, C3): "Using qudits instead of qubits can reduce the number of physical carriers needed to encode a given logical Hilbert space by a factor of $\log_2 d$" (EPJ Quantum Technol. 2024). Explicit quantification of the encoding-density advantage.
   - Ringbauer et al. (2022, C2): Demonstrated a universal qudit processor with $d=7$ qudits — experimentally confirms that physical qudit operations are viable, not just theoretical.

2. **Hierarchical decoding complexity advantage**
   - Heydeman et al. (2018, S4): "The Bruhat-Tits tree provides a natural hierarchical tensor network that encodes the p-adic AdS/CFT correspondence" (ATMP 2018, 56 citations). Confirms the BT tree's hierarchical structure as a valid computational substrate — the QNFO extension to QEC is novel but the substrate is externally validated.
   - Qudit surface codes (S2, 2023): Extends surface-code QEC to qudits — the external literature is actively exploring qudit QEC, confirming the field's recognition that qudit error correction is a distinct (and potentially advantageous) regime.

3. **Passive error resilience vs. active QEC overhead**
   - Wang et al. (2020, C1): Notes that qudit error channels have different structure than qubit error channels — some errors that require active correction for qubits are "naturally suppressed" in higher-dimensional systems. This is a weak form of passive resilience recognized in the external literature.
   - C4 (2025, Nature Comms): Proves unconditional advantage for noisy qudit circuits — directly supports the claim that qudits maintain advantage even under realistic noise, which is the operational definition of passive resilience.

4. **JPCUB framework validity**
   - JPCUB P0 (C5): The framework is published with adversarial validation provisions. No external challenge to the JPCUB methodology has been published. The framework's validity for benchmarking is established.
   - JPCUB Landscape v2.0 (C6): 17 platforms benchmarked with traceable specification sources — demonstrates the framework's applicability across diverse architectures.

#### Support Strength Summary

| Sub-Claim | External Support Level | Key Citation |
|:----------|:----------------------|:-------------|
| $\log_2 d$ encoding density | **STRONG** — consensus position | Wang et al. 2020 (493 cites) |
| Hierarchical decoding advantage | **MODERATE** — BT tree validated externally; QEC application is QNFO-novel | Heydeman et al. 2018 (56 cites) |
| Passive error resilience | **WEAK** — external literature recognizes qudit error-channel differences but does not claim passive resilience at scale | Wang et al. 2020 (qualitative note only) |
| JPCUB framework | **ESTABLISHED** — published, no external challenge | JPCUB P0 (DOI 10.5281/zenodo.21637028) |

---

### Where External Literature Constrains or Contradicts the Core Claim

**MUST NOT be empty per KIF-18. Name specific constraining evidence.**

#### Constraining Evidence

1. **No room-temperature qudit processor has been experimentally demonstrated**
   - Ringbauer et al. (2022, C2): Trapped-ion qudit processor operates at ultra-high vacuum with laser cooling — NOT room temperature. The experimental state of the art for operational qudits is cryogenic/vacuum.
   - Chi et al. (2022, S6): Photonic qudit processor operates at room temperature for the photonic part but requires cryogenic single-photon detectors.
   - **Constraint:** The QWAV claim of 300 K operation is [speculative] — no external experiment has demonstrated room-temperature qudit computation with the coherence times required for fault-tolerant operation. This is the single largest gap between the QWAV theoretical model and experimental reality.

2. **Qudit gate fidelities lag behind qubit gate fidelities**
   - Wang et al. (2020, C1): Reviews qudit gate fidelities and notes they are generally lower than qubit fidelities for the same physical platform — the larger Hilbert space makes gate calibration harder.
   - Low et al. (2024, C3): Qudit compilation reduces gate *count* but the remaining gates have lower fidelity — there is a fidelity-vs-count trade-off that may offset the encoding-density advantage.
   - **Constraint:** If qudit gate infidelity scales as $O(d^2)$ (worst-case leakage to other levels), the JPCUB advantage from reduced gate count could be offset by increased error-correction overhead. The paper MUST model this trade-off, not assume it away.

3. **The dominant QEC paradigm is planar (surface codes) — no competitive hierarchical alternative exists**
   - Kitaev (2003, B5): Surface codes are the dominant paradigm — 6,000+ citations, decades of optimization, industrial investment (Google, IBM). The hierarchical ultrametric decoder is a theoretical proposal with zero experimental validation.
   - B4 (Shor 1996): The fault-tolerance threshold theorem applies to ANY QEC code, but the threshold depends on the code's distance and decoder efficiency. No external paper has computed a fault-tolerance threshold for a Bruhat-Tits tree QEC code.
   - **Constraint:** The JPCUB model for the ultrametric decoder is a [speculative] upper bound — it assumes the decoder's asymptotic complexity scaling holds at realistic code distances. Without an experimentally validated fault-tolerance threshold, the decoder's energy advantage cannot be claimed as [established].

4. **JPCUB is a QNFO-internal framework — no external adoption or validation**
   - The JPCUB framework (C5, C6) has zero external citations or independent reproductions as of 2026-08-06. The 17-platform benchmark is computed entirely by QNFO.
   - **Constraint:** The paper's claim that QWAV qudits have a JPCUB advantage is only as credible as the JPCUB framework itself. Until an external group reproduces the JPCUB for at least one platform, the framework is [QNFO-internal — not externally validated]. The paper MUST flag this.

5. **Qudit advantage is asymptotic — NISQ-era advantage is unproven**
   - C4 (2025, Nature Comms): The unconditional advantage proof applies to constant-depth qudit circuits in the noisy regime — it is a complexity-theoretic result, not an engineering result. NISQ-era qudit processors (50-100 physical carriers) may not realize the asymptotic encoding-density advantage.
   - **Constraint:** The JPCUB comparison assumes a fault-tolerant regime (logical qubits, not physical qudits). For NISQ-era comparisons (physical-qudit-only), the encoding-density advantage may be offset by higher per-gate energy. The paper MUST distinguish between NISQ-era and fault-tolerant-era JPCUB estimates.

---

## 4. Classification Summary

| Class | Count | Papers |
|:------|:------|:-------|
| Core | 7 | C1–C7 |
| Supporting | 8 | S1–S8 |
| Background | 5 | B1–B5 |
| QNFO Internal | 4 | Q1–Q4 |
| Reject | 0 | — |
| **Total** | **24** | |

---

## 5. Gap Identification — What the Literature Does NOT Cover

| Gap | Significance | Paper's Opportunity |
|:----|:-------------|:---------------------|
| No JPCUB for any qudit architecture | **CRITICAL** | Our paper is the FIRST to compute JPCUB for qudits — entirely novel |
| No energy-efficiency comparison qudits vs qubits | **CRITICAL** | All existing comparisons are gate-count or algorithmic — we add the energy dimension |
| No p-adic QEC qudit implementation | **SIGNIFICANT** | Only 23 OpenAlex hits on p-adic QEC; zero experimental. Our paper describes the THEORETICAL qudit architecture — the JPCUB is a theoretical upper bound |
| No room-temperature fault-tolerant qudit model | **SIGNIFICANT** | The QWAV 300 K claim is unique — must be presented as [speculative] with explicit disconfirmation conditions |
| No external JPCUB validation | **MODERATE** | Framework is QNFO-internal — paper must flag this and invite adversarial validation per JPCUB P0 protocol |

---

## 6. Symmetry Gate Verdict

| Requirement | Status |
|:------------|:-------|
| Classification Matrix (Core/Supporting/Background/Reject) | ✅ COMPLETE — 24 papers classified |
| "Where External Literature Supports" section | ✅ COMPLETE — 4 sub-claims with strength ratings |
| "Where External Literature Constrains or Contradicts" section | ✅ COMPLETE — 5 constraints identified, none hedged |
| Gap identification | ✅ COMPLETE — 5 gaps identified |
| No hedging language in constraints section | ✅ VERIFIED — constraining evidence is specific and cited |

**KIF-18 GATE: PASS.** The symmetry template is complete. Constraining evidence is specific and actionable — it directly informs the Phase 4 Structured Forecast assumptions and the Phase 5 publication's [speculative] labeling requirements.

**Key constraint for Phase 4:** The qudit gate infidelity-vs-count trade-off (Constraint 2) must be explicitly modeled. If the paper assumes gate fidelities comparable to qubit fidelities, it must state that as an assumption and provide the disconfirmation condition (measured qudit gate fidelities below the assumed threshold → JPCUB advantage reduced or eliminated).
