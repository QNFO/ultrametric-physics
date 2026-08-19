# Phase 2 Literature Triage — QNFO.UMP.013 (pattern-particle-unification)

**Date:** 2026-08-19 · **Gate:** KIF-18 Mandatory Symmetry Template (HARD) · **Status:** COMPLETE

## 1. Multi-Source Search Log (8 sources)

| Source | Query set | Evidence file | Yield |
|---|---|---|---|
| OpenAlex (PRIMARY) | "Bruhat-Tits tree particle physics statistics"; "p-adic anyons braid statistics"; "spin-statistics exchange phase topological spin"; "holographic codes Bruhat-Tits buildings"; "ultrametric condensed matter statistics unification" | openalex_bt_tree_particles.json, openalex_padic_anyons.json, openalex_padic_anyons_v2.json, openalex_spin_statistics.json, openalex_holographic_bt.json, openalex_ultrametric_cm.json | 55 rows |
| Crossref | "Feynman rules for any spin Weinberg"; "Theory of Superconductivity Bardeen"; "Anomalous quantum Hall Laughlin"; "p-adic analysis mathematical physics Vladimirov"; "Spin p-adic AdS/CFT"; "anyons fractional statistics review" | crossref_weinberg.json, crossref_bcs.json, crossref_laughlin.json, crossref_vladimirov.json, crossref_spin_padic_ads.json, crossref_anyons_review.json | 30 rows |
| Zenodo records | title:"Bruhat-Tits" AND statistics (0 hits); "Bruhat-Tits" AND anyon (5 hits — ALL QNFO: 21208366, 21214358, 21214362, 21208370, 21208568) | zenodo_bt_statistics.json, zenodo_bt_anyon_all.json | **All-of-Zenodo novelty proof** |
| Europe PMC | "Bruhat-Tits" AND "anyons" | europepmc_bt_anyons.json | 0 hits — life-sciences index N/A, documented |
| arXiv | ti:"Bruhat-Tits" physics (6); spin-statistics anyons (6); Moore-Read nonabelian (6); Weinberg spin-statistics (0 via ti — resolved via Crossref) | (arXiv MCP results, session log) | 18 rows |
| Web | Covered via OpenAlex/Crossref/arXiv/Zenodo primary indexes; no web-specific claim requires CDX this phase | — | — |
| QNFO Vectorize | 12 formulations × 4 topics (Phase 1, limit 16, VECTORIZE-TOP-K-50-1 compliant) | due-diligence-phase1.md §2 | 192 rows |
| QNFO KG | Paper nodes: anyon (4), quasiparticle (0 — DQ6), stats 8,303 nodes | due-diligence-phase1.md §1,§3 | — |

## 2. Classification Matrix

### Core (directly addresses RQ — 10)
| # | Reference | DOI / ID | Role |
|---|---|---|---|
| C1 | RES.009 The Boson/Fermion Distinction (internal) | 10.5281/zenodo.21964598 (concept 21962904) | Premise 3: statistics as structural invariant, R = e^{2πis}, dimension quantizes s |
| C2 | The Exchange Phase as a Logical Scalar (internal) | 10.5281/zenodo.21964104 | Half-turn reading: R = (e^{iπ})^{2s}; logical-scalar family e, π, R |
| C3 | Adelic Synthesis: Pattern-Particle Correspondence (internal) | 10.5281/zenodo.21208568 | Premise 5: complete arithmetic theory of anyons |
| C4 | p-Adic Anyon Fusion and Braiding (internal) | 10.5281/zenodo.21208491 | Quantum groups at roots of unity |
| C5 | Quasiparticles as Rational Functions (internal) | concept 10.5281/zenodo.21768756 (v2.0: 21784490) | Premise 4: N_C* rational-function composites |
| C6 | Weinberg, Feynman Rules for Any Spin (1964) | 10.1103/physrev.133.b1318 | ±1 forced by Lorentz invariance + microcausality in 3+1D (constraint!) |
| C7 | Mund, Spin-Statistics Theorem for Anyons and Plektons in d=2+1 (2008) | arXiv 0801.3621 | External: spin-statistics relation R = e^{2πis} PROVEN for braid statistics in 2+1D — directly supports claim 2's anyon clause |
| C8 | Laughlin, Anomalous Quantum Hall Effect (1983) | 10.1103/physrevlett.50.1395 | ν=1/3 fractionally charged excitations; abelian anyon anchor |
| C9 | Moore–Read, FQHE and nonabelian statistics (1991) | arXiv hep-th/9202001 | NON-ABELIAN statistics — matrix-valued (constraint!) |
| C10 | Bardeen–Cooper–Schrieffer (1957) | 10.1103/physrev.108.1175 | BCS gap Δ~exp(−1/N(0)V) — non-analytic (constraint on premise 4!) |

### Supporting (adjacent — 12)
| # | Reference | DOI / ID | Role |
|---|---|---|---|
| S1 | Marcolli, Holographic Codes on BT buildings (2018) | arXiv 1801.09623 / 10.4310/pamq.2020.v16.n1.a1 | External BT-tree-as-physics substrate |
| S2 | Heydeman et al., Tensor network and (p-adic) AdS/CFT (2018) | 10.1007/jhep01(2018)139 | p-adic holographic tensor networks |
| S3 | Gubser et al., p-adic CFT is a holographic tensor network (2019) | 10.1007/jhep04(2019)170 | p-adic CFT = tensor network on tree |
| S4 | Holographic tensor networks from hyperbolic buildings (2022) | 10.1007/jhep10(2022)169 | BT-building physics continues |
| S5 | Spin in p-adic AdS/CFT (2019) | 10.1088/1751-8121/ab0757 | EXTERNAL spin structure on p-adic geometry — key adjacent |
| S6 | Chen, Liu, Hung, Bending the BT Tree II: p-adic BTZ black hole (2021) | arXiv 2102.12024 | p-adic AdS/CFT dynamics on BT tree |
| S7 | Aubert, BT buildings, representations of p-adic groups, Langlands (2023) | arXiv 2306.06735 | UIA-A2 anchor: automorphism-group representation theory exists |
| S8 | Configuration-Space Topology (internal) | 10.5281/zenodo.21962450 | Exchange scalar ±1 shadow, pre-registered derivation program |
| S9 | Compton Frequency Cross-Ratios v2.3 (internal) | 10.5281/zenodo.21485556 | SM mass spectrum pre-registered search on BT trees |
| S10 | Adelic Cross-Domain Program v5.0 (internal) | 10.5281/zenodo.21965332 | α to SM mass spectrum via BT trees |
| S11 | Signal-Worker Boundary Confinement (internal) | 10.5281/zenodo.21974194 | Cooper-pair + spin-statistics accounting (INM.001) |
| S12 | Vladimirov–Volovich–Zelenov, p-Adic Analysis and Mathematical Physics (1994) | 10.1142/1581 | Canonical p-adic physics reference |

### Background (context — 6)
| # | Reference | DOI |
|---|---|---|
| B1 | Quantum spin liquids: a review (2016) | 10.1088/0034-4885/80/1/016502 |
| B2 | Topological superconductors: a review (2017) | 10.1088/1361-6633/aa6ac7 |
| B3 | Topological insulators and superconductors: tenfold way (2010) | 10.1088/1367-2630/12/6/065010 |
| B4 | Anyons and the Fractional Quantum Hall Effect (1992) | 10.1007/978-3-540-47466-1_8 |
| B5 | A p-adic version of AdS/CFT (2017) | 10.4310/atmp.2017.v21.n7.a3 |
| B6 | ODR Thesis (internal, premise 1) | 10.5281/zenodo.21780909 |

### Reject (with reason — 5)
| # | Reference | Reason |
|---|---|---|
| R1 | Primacohedron preprints (2025, ×3) | p-adic string/random-matrix framing WITHOUT statistics structure; no cross-catalog claim; preprint-only, no peer structure |
| R2 | ZEBTS monograph (2026) | Noise; no verifiable structure |
| R3 | Genetic code / dark matter "physics realizations" (2013/2010) | Irrelevant numerology |
| R4 | LIV searches (H.E.S.S. 2016) | Different Lorentz question; irrelevant to statistics-phase claim |
| R5 | O'Hara / Suoranta / Santamato spin-statistics re-derivations (2003–2017) | Alternative derivations noted for background only; no BT-tree or two-catalog content (kept as background note, not core) |

## 3. KIF-18 Mandatory Symmetry Template

### Where External Literature Supports [Claim]
- **Claim 2 (statistics = phase e^{2πis}, anyons at roots of unity):** Mund (2008, arXiv 0801.3621) proves the spin-statistics theorem for particles obeying braid-group statistics in 2+1D Minkowski space — the phase relation extends to anyons externally, independent of QNFO. Laughlin (1983) supplies the ν=1/3 abelian case (phase 2π/3). Weinberg (1964) supplies the 3+1D forced-±1 anchor. [SUPPORT — with the caveat that this makes claim 2 a retrodiction per KIF-60]
- **Premise 2 (BT tree as legitimate physics substrate):** an external, independent literature exists: holographic codes and tensor networks on BT buildings/trees (Marcolli 2018; Heydeman et al. 2018; Gubser et al. 2019; JHEP 2022; Chen–Liu–Hung 2021) and spin structure in p-adic AdS/CFT (2019). The tree is not a QNFO invention — premise 2 is externally anchored. [SUPPORT]
- **Premise 4 (quasiparticle effective masses, N_C*):** BCS (1957) and Laughlin (1983) empirically establish that condensed-matter excitations carry environment-dependent masses/scales; the QP rational-function reading is a QNFO-specific formalization of this established fact. [SUPPORT — empirical anchor]
- **UIA-A2 (automorphism-group representations):** Aubert (2023) and Neretin (2013) show BT-building representation theory and Langlands correspondences are an active external field — the requested group/representation specification is feasible with external precedent. [SUPPORT]

### Where External Literature Constrains or Contradicts [Claim]
- **C9 — Moore–Read (1991):** non-abelian anyon statistics is MATRIX-VALUED (braid-group representations of dimension >1), NOT a root-of-unity phase. Claim 2's anyon clause is therefore RESTRICTED to abelian anyons; non-abelian statistics cannot be absorbed as "a phase." This is a HARD constraint on the core claim (UIA-A4 confirmed). The paper must state the abelian scope and record the non-abelian extension (fusion multiplicities / UMTC) as an open problem.
- **C10 — BCS (1957):** Δ ~ exp(−1/N(0)V) is non-analytic in the coupling; heavy-fermion effective masses m* ∝ 1/T_K are exponential. Premise 4 (quasiparticle N_C* as RATIONAL function of background counts) is FALSE for strongly-correlated composites. HARD constraint: the quasiparticle clause must be scoped to weakly-interacting/band composites, with exponential-scale regimes explicitly outside (UIA-A3 confirmed). The paper must not absorb this counterexample (KIF-60 absorption trap).
- **C6 — Weinberg (1964):** in 3+1D, ±1 statistics is FORCED by Lorentz invariance + microcausality. The tree reading of boson/fermion is therefore explanatory, not predictive, in 3+1D (UIA-A5 confirmed). The paper must state what the tree adds beyond the forced result (the unified two-catalog table + the 2D interpolation + the pre-registered address scheme), and must NOT claim to "derive" spin-statistics.
- **[NO CONSTRAINING EVIDENCE FOUND]** for the unification claim itself: "the SM particle table and the condensed-matter quasiparticle/anyon zoo are two projections of one labeled pattern table on the Bruhat–Tits tree." Exhaustive cross-checks: OpenAlex (p-adic anyons/BT sweeps: top hits are QNFO + holographic codes only), Crossref (no two-catalog unification work), Zenodo all-corpus (5 "Bruhat-Tits+anyon" records, ALL QNFO), Europe PMC (0). The novelty claim stands with no external contradictor — but per KIF-60 it carries ZERO evidential weight until the pre-registered C3 address scheme is tested on unseen excitations.

## 4. Gate Output

Phase 2 COMPLETE: 8 sources searched, 55+30+18+192 rows screened, 10 Core + 12 Supporting + 6 Background + 5 Reject classified, KIF-18 symmetry template both sections populated (3 supports, 3 hard constraints, 1 explicit NO-CONSTRAINING-EVIDENCE for the novel claim). Evidence files: artifacts/external-search/*.json (all cited above).
