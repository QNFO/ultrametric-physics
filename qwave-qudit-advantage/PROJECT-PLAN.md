# WBS: QNFO.UMP.005

## PROJECT-PLAN: The Qudit Advantage — JPCUB Comparison of QWAV vs. Conventional Qubit Platforms

**Slug:** `qwave-qudit-advantage`
**WBS:** `QNFO.UMP.005`
**Program:** Ultrametric Physics (UMP)
**Repository:** `QNFO/ultrametric-physics`
**Branch:** `ump/paper/qwave-qudit-advantage`
**Created:** 2026-08-06

---

## 1. Charter

This paper directly extends the **JPCUB Competitive Landscape v2.0** (Zenodo DOI `10.5281/zenodo.21821767`, companion to JPCUB P0 DOI `10.5281/zenodo.21637028`), which computed system-level joules-per-solution (JPCUB) estimates for **17 conventional qubit-based** quantum computing platforms (13 gate-model, 2 annealing, 1 photonic, 1 pre-commercial target).

The qubit platforms span superconducting (0.05-0.71 J/sol), neutral-atom (0.32-0.62 J/sol), and trapped-ion (8.5-16.3 J/sol) architectures — all using 2-level quantum systems.

**The QWAV alternative** uses **qudits** — $d$-level quantum systems hosted on Bruhat-Tits trees with p-adic stabilizer codes, hierarchical ultrametric decoding, and passive error resilience through ultrametric geometry. The critical architectural distinction: qudits deliver higher logical clock rate per physical-qudit ratio, room-temperature operation (300 K vs 10 mK), and zero ancilla overhead.

This paper:
1. **Models the QWAV qudit platform within the JPCUB framework** — computing joules-per-solution for the qudit architecture
2. **Compares against the 17-qubit JPCUB Landscape** — places the qudit result on the same competitive axis
3. **Identifies the structural source of the qudit advantage** — dimensional scaling (qudit dimension $d$), Bruhat-Tits tree topology, and passive error resilience vs. active error correction overhead

---

## 2. Research Question

**Primary:** What is the joules-per-solution (JPCUB) estimate for the QWAV qudit architecture, and how does it compare to the 17 conventional qubit platforms benchmarked in JPCUB Competitive Landscape v2.0?

**Secondary:** What structural features of qudit computation (dimensional scaling, hierarchical decoding, passive error resilience) account for any observed advantage over qubit platforms?

---

## 3. Core Claim (Locked at Phase 0)

The QWAV qudit architecture achieves a JPCUB advantage over all 17 conventional qubit platforms through three compounding factors: (1) dimensional encoding density ($\log_2 d$ bits per physical carrier vs. 1 for qubits), (2) ultrametric hierarchical decoding with sub-exponential complexity, and (3) passive error resilience that eliminates ancilla overhead and cryogenic cooling energy.

**Disconfirmation condition:** If the modeled joules-per-solution for the qudit architecture, under conservative assumptions, exceeds the best superconducting qubit platform ($0.05$ J/sol), the claimed advantage is falsified.

---

## 4. Phases with WBS

| WBS Code | Phase | Description | Gate Criteria |
|:---------|:------|:------------|:--------------|
| `QNFO.UMP.005.P0` | Init | Repo scaffold, branch, WBS resolution, core claim lock | Branch created, PROJECT-PLAN.md committed, v0.1-phase0 tagged |
| `QNFO.UMP.005.P1` | Due Diligence | KG + D1 + Vectorize cross-ref, external literature (OpenAlex, Crossref, Zenodo, arXiv) | All sources queried, gap analysis complete, KIF-29 consilience gate |
| `QNFO.UMP.005.P2` | Literature | JPCUB framework review, qudit literature, dimensional scaling theory | Symmetry template complete, 5-10 core papers classified |
| `QNFO.UMP.005.P3` | Citations | Extract, verify BibTeX, P3.AUTHOR-GATE | Every entry verified against Crossref/OpenAlex |
| `QNFO.UMP.005.P4` | Deep Research | JPCUB model for qudit architecture, dimensional advantage derivation, hierarchical decoder energy model, passive resilience energy savings | Structured forecast, assumption audit, red-team challenge |
| `QNFO.UMP.005.P5` | Publication | `<slug>.md` + PDF (pandoc -> MathJax SVG -> puppeteer-core CDP) + all BP gates + Zenodo DOI | PDF verified, U+FFFD scan clean, Zenodo DOI resolves |
| `QNFO.UMP.005.P6` | Deployment | D1 living-paper, papers-server verification, R2 archive | D1 entry verified, papers.qnfo.org 200 |
| `QNFO.UMP.005.P7` | Dissemination | SEO, Buffer social, papers.qnfo.org, Internet Archive | All checks pass |
| `QNFO.UMP.005.P8` | Core Distribution | GitHub tag, Zenodo newversion, R2 archive, D1/KG records | All 4 layers verified |

---

## 5. Deliverable Registry

| ID | Deliverable | Phase | Format | Location |
|:---|:------------|:------|:-------|:---------|
| D-01 | Project paper | P5 | `qwave-qudit-advantage.md`, `.pdf`, `.html` | Repo + Zenodo |
| D-02 | JPCUB computation script | P4 | Python | `notebooks/` |
| D-03 | Due diligence report | P1 | Markdown | `artifacts/` |
| D-04 | Consilience gate report | P1 | Markdown | `artifacts/consilience-gate.md` |
| D-05 | Literature review | P2 | Markdown | `artifacts/` |
| D-06 | Citation audit | P3 | Markdown | `artifacts/citation-audit.md` |
| D-07 | Structured forecast | P4 | Markdown | `artifacts/` |
| D-08 | Bayesian evidential weight | P4 | Markdown | `artifacts/bayesian-evidential-weight.md` |
| D-09 | Existential claim verification | P5 | Markdown | `artifacts/existential-claim-verification.md` |

---

## 6. Risk Register

| ID | Risk | Likelihood | Impact | Mitigation |
|:---|:-----|:-----------|:-------|:-----------|
| R-01 | Insufficient published qudit-implementation specs for JPCUB modeling | Medium | High | Use theoretical bounding from dimensional scaling + hierarchical decoder complexity; flag as [UPPER BOUND] with explicit assumptions |
| R-02 | JPCUB advantage depends on qudit dimension $d$ exceeding a threshold not yet demonstrated | Medium | High | Parametrize by $d$; show advantage crossover point explicitly |
| R-03 | QEC darwinism / passive resilience energy models are [speculative] — not yet verified by physical implementation | High | Medium | Label as [speculative]; provide disconfirmation conditions; compute under both optimistic and conservative assumptions |
| R-04 | Overlap with prior QNFO papers (QEC darwinism, ultrametric metrology) | Low | Low | Cross-reference; this paper provides the JPCUB framework integration those papers lack |

---

## 7. Success Criteria

1. A joules-per-solution estimate for the QWAV qudit architecture is computed and traceable to published specifications or derived bounds
2. The estimate is placed on a single comparison table alongside all 17 JPCUB Landscape v2.0 platforms
3. The structural sources of any advantage (dimensional scaling, ultrametric decoding, passive resilience) are identified with explicit formulas
4. At least one falsifiable prediction is registered (with timestamp)
5. Published to Zenodo with DOI and deployed to papers.qnfo.org
