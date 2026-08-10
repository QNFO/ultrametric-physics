# Literature Classification — Universe Category Functor (QNFO.UMP.006)

**Date:** 2026-08-10
**WBS:** QNFO.UMP.006.P2
**Status:** COMPLETE
**Evidence:** `artifacts/external-search/*.json` (16 queries × 4 sources: OpenAlex, Crossref, arXiv, Zenodo) + QNFO Vectorize/KG internal anchors.

---

## Classification Matrix

| Class | Definition | Count |
|:------|:-----------|:------|
| Core | Directly addresses RQ | 8 |
| Supporting | Adjacent work | 8 |
| Background | Context, foundations | 6 |
| Reject | Irrelevant / caution | 3 |
| **Total classified** | | **25** |

**Search-space denominator:** 16 queries, ~46 top hits screened, 25 classified. Hit/miss ratio documented — no cherry-picking.

---

## CORE (8) — Directly addresses the functor \(F: \mathbb{N} \to \mathbf{Man}\)

| # | Paper | Source | DOI / ID | Why core |
|:--|:------|:-------|:---------|:---------|
| C1 | Prime Numbers as Universal Optimization Primitives | QNFO internal | 10.5281/zenodo.17516239 | **SOURCE** — defines \(F: \mathcal{P} \to \mathcal{M}\), homology rank = \(2^{\omega(n)}\) |
| C2 | Functoriality in Morse theory on closed manifolds | arXiv | 0805.2131 | Functoriality of Morse-theoretic invariants — the functor leg |
| C3 | p-adic CFT is a holographic tensor network | JHEP 2019 | 10.1007/jhep04(2019)170 | Bruhat-Tits tree as bulk substrate |
| C4 | Tensor networks, p-adic fields, and algebraic curves | ATMP 2018 | 10.4310/atmp.2018.v22.n1.a4 | Arithmetic AdS3/CFT2 correspondence |
| C5 | A geometric approach to integer factorization | arXiv | 1802.03658 | Factorization-as-geometry precedent |
| C6 | p-Adic valued quantization | p-Adic Numbers 2009 | 10.1134/s2070046609020010 | p-adic quantization framework |
| C7 | Quantization of algebraic invariants through TQFTs | J. Geom. Phys. 2023 | 10.1016/j.geomphys.2023.104849 | Topological quantization of invariants |
| C8 | Spectral Analysis of Anomalous Diffusion on p-Adic Fractals | QNFO internal | 10.5281/zenodo.18606514 | **CONSTRAINS** — pure ultrametricity insufficient for GUE; broken symmetry required |

---

## SUPPORTING (8) — Adjacent work

| # | Paper | Source | DOI / ID | Why supporting |
|:--|:------|:-------|:---------|:---------------|
| S1 | Nonarchimedean holographic entropy from networks of perfect tensors | ATMP 2021 | 10.4310/atmp.2021.v25.n3.a2 | Perfect tensors on ultrametric networks |
| S2 | Treelike interactions and fast scrambling with cold atoms | PRL 2019 | 10.1103/physrevlett.123.130601 | Experimental ultrametric (tree) substrate |
| S3 | Bending the Bruhat-Tits Tree II | JHEP 2021 | 10.1007/jhep09(2021)097 | p-adic BTZ / tree physics |
| S4 | Formalising the Bruhat-Tits Tree | arXiv 2026 | 2505.12933 | Formalization of BT substrate (2026!) |
| S5 | The boundary theory of a spinor field theory on the Bruhat-Tits tree | arXiv | 1910.09397 | Spinor fields on tree |
| S6 | Strange Loop Theory of Physical Quantization | QNFO internal | 10.5281/zenodo.17415145 | Quantization leg (\(L=2\), \(w=1\)) |
| S7 | Number-Theoretic Ultrametric Foundations (p-adic QEC) | QNFO internal | — | Stability leg (QEC classification) |
| S8 | Bruhat-Tits Tree as a Unifying Geometric Object (Ballistic Transport) | QNFO internal | — | Substrate leg |

---

## BACKGROUND (6) — Context, foundations

| # | Paper | Source | DOI / ID |
|:--|:------|:-------|:---------|
| B1 | Equivariant Morse theory and closed geodesics | J. Diff. Geom. 1984 | 10.4310/jdg/1214438424 |
| B2 | Invariant measures on p-adic Lie groups | Lett. Math. Phys. 2024 | 10.1007/s11005-024-01826-8 |
| B3 | Spin foams and noncommutative geometry | CQG 2010 | 10.1088/0264-9381/27/20/205025 |
| B4 | Topological photonics | Rev. Mod. Phys. 2019 | 10.1103/revmodphys.91.015006 |
| B5 | From Data to the p-Adic or Ultrametric Model | arXiv | 0809.0492 |
| B6 | p-Adic description of Higgs mechanism | arXiv | hep-th/9410058 |

---

## REJECT (3) — Caution / irrelevant / novelty-reduction risk

| # | Paper | Source | DOI / ID | Reason |
|:--|:------|:-------|:---------|:-------|
| R1 | Homological Invariants of Computational Hardness: Morse-Smale Obstruction to P≠NP | Zenodo | 10.5281/zenodo.18046058 | **Independent prior claim** on homological hardness framing — MUST be cited and differentiated (novelty-reduction risk) |
| R2 | 6m Theorem for Prime numbers | arXiv | 1810.02188 | Caution flag: prime-focused geometric claims have false-precision risks |
| R3 | O(N) and O(N) and O(N) (title artifact) | JHEP 2017 | 10.1007/jhep11(2017)107 | Low relevance; title-parsing artifact of search |

---

## KIF-18 Mandatory Symmetry Template

### Where External Literature Supports the Claim

External literature independently supports each leg of the functor claim:
- **Functor leg:** Functoriality in Morse theory on closed manifolds (0805.2131)
- **Ultrametric substrate leg:** p-adic CFT holographic tensor network (jhep04(2019)170), Tensor networks p-adic fields (atmp.2018.v22.n1.a4), Treelike interactions cold atoms (PRL 123.130601)
- **Factorization leg:** A geometric approach to integer factorization (1802.03658)
- **Quantization leg:** p-Adic valued quantization (10.1134/s2070046609020010), Quantization of algebraic invariants through TQFTs (10.1016/j.geomphys.2023.104849)

### Where External Literature Constrains or Contradicts the Claim

1. **Ultrametricity ≠ GUE (C8, QNFO-internal):** Spectral p-Adic (10.5281/zenodo.18606514) found pure ultrametricity yields a degenerate Laplacian spectrum distinct from the GUE statistics of the Riemann zeros. The "stability leg" cannot be claimed as sufficient for Riemann-zero statistics without broken symmetry — constrains any claim that ultrametric hierarchy alone reproduces the full Riemann spectrum.
2. **Independent prior claim (R1):** Homological Invariants of Computational Hardness (10.5281/zenodo.18046058) independently claims a Morse-Smale obstruction framing of P≠NP. The functorial-hardness framing is NOT QNFO-exclusive — must cite, differentiate, and avoid overclaiming novelty of the homological approach (the novelty is the SINGLE-functor three-leg synthesis, not homological hardness per se).
3. **No external source contradicts the existence of the functor**, but none confirms the three-leg synthesis either — the synthesis claim is QNFO-original and carries [CONFIRMATION-BIAS-RISK: synthesis is QNFO-internal].

---

## Status

- Classification: ✅ COMPLETE (25 classified: 8 Core / 8 Supporting / 6 Background / 3 Reject)
- KIF-18 Symmetry: ✅ COMPLETE (both sections present, specific evidence cited)
- **HARD GATE: Phase 2 classification PASSED → Phase 3 (Citation Management) may proceed**
