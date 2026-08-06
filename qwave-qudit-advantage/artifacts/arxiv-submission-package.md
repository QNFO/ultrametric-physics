# arXiv quant-ph Submission Package — QNFO.UMP.005

> **⚠️ STATUS: BLOCKED — NO arXiv ENDORSEMENT (2026-08-06).**
> The author does not hold endorsement to post to any arXiv category, and the standing
> preference is direct journal submission. **This package is superseded by
> `journal-submission-strategy.md`.** Retained for reference if endorsement is later
> granted (e.g., after a journal publication, arXiv endorsement can be requested from
> an established author in quant-ph).

**Paper:** The Qudit Advantage: System-Level Joules-per-Solution Comparison of a Qudit Architecture Against 17 Conventional Qubit Quantum Computing Platforms
**DOI:** 10.5281/zenodo.21827737 (v0.4 — canonical; supersedes 21827347 v0.3)
**Author:** Rowan Brad Quni-Gudzinas (Independent Researcher, QNFO)
**ORCID:** 0009-0002-4317-5604
**Date:** 2026-08-06

---

## Submission Fields

| Field | Value |
|:------|:------|
| **Category** | quant-ph (Quantum Physics) |
| **Primary subject** | Quantum information theory / quantum error correction / benchmarking |
| **Title** | The Qudit Advantage: System-Level Joules-per-Solution Comparison of a Qudit Architecture Against 17 Conventional Qubit Quantum Computing Platforms |
| **Author** | Rowan Brad Quni-Gudzinas |
| **Report-no / Comments** | 30 pages, 3 tables, 22 references; preprint version of Zenodo DOI 10.5281/zenodo.21827347. JPCUB framework previously published at 10.5281/zenodo.21637028 (P0) and 10.5281/zenodo.21821767 (17-platform landscape). All [speculative] claims carry pre-registered disconfirmation conditions. Adversarial validation invited per the JPCUB P0 protocol. |

## Abstract (verbatim from paper YAML)

The JPCUB Competitive Landscape v2.0 benchmarked 17 qubit-based quantum computing platforms across a single system-level energy-efficiency metric: joules per solution (J/sol). All 17 platforms use two-level quantum systems (qubits). This paper extends the JPCUB framework to qudit architectures — $d$-level quantum systems — and computes a joules-per-solution estimate for a qudit platform whose error-correction model is based on $p$-adic stabilizer codes on Bruhat–Tits trees with hierarchical ultrametric decoding and passive error resilience. Three compounding factors are analyzed: (1) dimensional encoding density, where each physical qudit carries $\log_2 d$ bits versus 1 for a qubit; (2) hierarchical decoding complexity, which is sub-exponential in tree depth versus polynomial for planar surface-code decoders; and (3) passive error resilience, which eliminates the ancilla overhead and cryogenic cooling energy of active quantum error correction. Under conservative assumptions, the qudit platform is projected to achieve a JPCUB value below $10^{-2}$ joules per solution, surpassing the 2026 superconducting-qubit floor of $0.05$ J/sol by at least one order of magnitude. The dominant uncertainty is the dimensional-advantage crossover parameter $d^*$, the minimum qudit dimension at which the encoding-density benefit overcomes the per-gate fidelity penalty. The paper provides an explicit disconfirmation condition — if a physical qudit platform with $d = 3$ or greater, under adversarial validation per the JPCUB P0 protocol, yields a measured joules-per-solution above $0.05$ J/sol, the claimed qudit advantage is falsified — and pre-registers three frontier questions for independent investigation.

---

## arXiv Notes & Warnings

1. **arXiv requires LaTeX or a supported format.** The paper is Markdown → the PDF is already built via the canonical CDP pipeline. For arXiv, submit the **PDF directly** (arXiv accepts PDFs) OR convert to LaTeX. PDF submission is simplest and preserves the MathJax-rendered math.

2. **arXiv moderation delay:** first submission from a new author takes 24–72h for moderation. Response to referee comments must be professional and non-defensive.

3. **Dual publication is fine:** arXiv preprint + Zenodo DOI are complementary, not conflicting. Zenodo remains the canonical versioned record; arXiv is the discovery layer.

4. **Licensing:** arXiv default license for the submission is the arXiv perpetual license (non-exclusive). The paper's QNFO-ULA license governs the Zenodo record. For arXiv, select "arXiv perpetual, non-exclusive license to distribute" and note the QNFO-ULA applies to the canonical version.

5. **"Independent researcher" affiliation:** arXiv allows an empty/unaffiliated author field. Use "Independent Researcher" — no institutional affiliation is required and does not reduce visibility. The paper's quality (verified citations, pre-registered predictions, adversarial-validation invitation) is the legitimacy signal.

---

## Falsifiability framing (for the comments field and any referee response)

The paper's strongest legitimacy asset is its pre-registered disconfirmation condition:

> A measured joules-per-solution above 0.05 J/sol for any physical qudit platform with $d \geq 3$ under adversarial validation falsifies the claimed qudit advantage.

This is explicitly designed to survive peer review — a referee cannot dismiss the claim as unfalsifiable, and the invitation to adversarial validation signals confidence without overclaiming.

---

## Next Steps (execution checklist)

- [ ] Register arXiv account (rowan.quni@qnfo.org) — needs user confirmation for the email
- [ ] Submit PDF via arXiv web upload (new submissions)
- [ ] Wait for moderation (24–72h)
- [ ] Respond to any referee comments professionally
- [ ] After acceptance: add arXiv identifier to D1 paper row + Zenodo metadata (`related_identifiers: isVersionOf / hasVersion`)
- [ ] Update Buffer/X/LinkedIn posts to reference the arXiv ID once live
