---
title: "One Table, Two Regimes: Standard-Model Particles and Condensed-Matter Excitations as Patterns on the Bruhat-Tits Tree"
author: "Rowan Brad Quni-Gudzinas"
affiliation: "QNFO"
ORCID: "0009-0002-4317-5604"
date: "2026-08-19"
license: "cc-by-4.0"
doi: "10.5281/zenodo.22017149"
status: "published"
version: "v0.1"
---

## Abstract

Physics currently maintains two particle catalogs that never meet in one framework: the Standard Model's finite table of elementary fermions and bosons, and the open-ended zoo of quasiparticles and anyons that condensed matter discovers in every new material. This paper assembles both catalogs into a single pattern table on the Bruhat-Tits tree, the regular infinite tree whose structure underlies p-adic geometry. The organizing claim is that every entry in both catalogs is a labeled pattern of this one tree, distinguished by a five-field address: the place and branch of the tree, the node class (edge, vertex, or composite), the Compton count that fixes the mass scale, and the statistics phase. Statistics is read as a tree-automorphism phase: bosons carry the trivial phase, fermions the sign phase of an edge half-turn, and abelian anyons the root-of-unity phases that open on ramified branches. The framework's new content is the table itself, the regime dictionary that says when each reading applies, and a set of falsifiability conditions spanning both catalogs. Its premises end at five named inputs: the Compton count as the only primitive, the tree as the state-space geometry, the exchange-phase invariant for spin-statistics, the rational-function reading of quasiparticle masses, and the p-adic braid phases of abelian anyons. Nothing here derives these inputs; the contribution is the assembly. For every known particle the table recapitulates established results; its evidential value lies in the pre-registered address scheme, to be tested against excitations not yet characterized.

**Keywords:** Bruhat-Tits tree; spin-statistics; anyons; quasiparticles; p-adic physics; unification

## 1. Introduction

Two particles catalogs exist in physics. The first is the Standard Model: six quarks, six leptons, five gauge bosons, and the Higgs scalar — a finite, closed list in which every entry is elementary [1,2]. The second is the condensed-matter catalog: phonons and magnons, excitons and polarons, Cooper pairs and composite fermions, quasiparticles whose masses depend on the host material [17,18], and, in two-dimensional systems, anyons whose exchange produces phases that interpolate between the bosonic and fermionic cases [4,20]. The two catalogs are taught as different ontologies. Elementary particles are thought of as fundamental fields; quasiparticles are thought of as emergent excitations. Anyons occupy a category of their own, possible only in two spatial dimensions.

This separation is practical, but it hides a structural question: is there a single object of which both catalogs are projections? This paper proposes one. The Bruhat-Tits tree — the (p+1)-regular tree whose vertices are the homothety classes of lattices in the p-adic plane [6] — has appeared independently in arithmetic geometry, in p-adic mathematical physics, and, more recently, in holographic constructions where tensor networks live on its vertices [7,8,9,10,11,12,21]. Previous work in this program has used the tree as the state-space geometry of a counting ontology in which a particle is identified with its Compton count, the dimensionless ratio of its mass to the Planck mass [23]; has shown that the tree's structure reproduces the mass ratios of the Standard Model [31,32]; has read the exchange phase of identical particles as a structural invariant $R = e^{2\pi i s}$ from which the boson-fermion dichotomy follows as a three-dimensional shadow [24,25,26]; has extended the counting ontology to quasiparticles, whose effective masses become rational functions of the background counts [27]; and has constructed abelian anyons as braid phases on the same tree [28,29,30].

What has not been done is the assembly. This paper places both catalogs side by side in one table, with one address scheme, and states the dictionary that says when each regime applies. Section 2 reviews the two catalogs. Section 3 introduces the tree. Section 4 develops the reading of statistics as a phase, including the categorical distinction that resolves the homonymy of "spin" between three and two dimensions. Section 5 presents the unified table. Section 6 gives the regime dictionary. Section 7 treats quasiparticles. Section 8 states the epistemic status of each claim. Section 9 gives the falsifiability conditions. Section 10 addresses practitioners. Section 11 concludes.

## 2. The Two Catalogs

### 2.1 The Standard Model catalog

The Standard Model lists twelve fermions — six quarks (up, down, charm, strange, top, bottom) and six leptons (electron, muon, tau, and their neutrinos) — all of spin 1/2, plus the gauge bosons (photon, eight gluons, W and Z) of spin 1, and the Higgs scalar of spin 0 [1,2]. The exchange statistics of identical particles in three spatial dimensions admits exactly two possibilities, because exchanging twice is topologically trivial: the exchange phase must square to one, so it is either +1 (bosons) or -1 (fermions). The spin-statistics theorem fixes which: the phase is $(-1)^{2s}$ [1]. Every entry in this catalog carries an exact statistics phase, and every mass is a fixed constant of nature, expressible as a Compton count $N_C = m/m_P$, a dimensionless rational number [23].

### 2.2 The condensed-matter catalog

Condensed matter supplies excitations with environment-dependent properties. A phonon is a quantized lattice vibration; a magnon a quantized spin wave; an exciton a bound electron-hole pair; a Cooper pair the bound state underlying superconductivity [2,17]; a composite fermion the attached-flux object of the fractional quantum Hall effect [3,20]. Their effective masses are functions of the host material, temperature, doping, and fields. In two dimensions, braid statistics becomes possible: exchanging quasiparticles twice need not be trivial, and the exchange phase can be any root of unity. The Laughlin state at filling fraction $\nu = 1/3$ hosts quasiparticles with exchange phase $e^{2\pi i/3}$ [3]; the Moore-Read state at $\nu = 5/2$ hosts excitations whose statistics is described by matrices rather than phases [5,22]. Anyons of the abelian kind have topological spin $\theta = e^{2\pi i s}$ with fractional $s$ [4,20].

### 2.3 The asymmetry

The Standard Model catalog is finite, elementary, and exact. The condensed-matter catalog is open, emergent, and approximate. Textbooks treat the difference as ontological. This paper treats it as structural: the two catalogs are the two readings of one tree — the free-particle reading at the tree's unramified places, and the dressed, braided reading on its ramified branches.

## 3. The Bruhat-Tits Tree as the Common Substrate

For a p-adic field $\mathbb{Q}_p$, the Bruhat-Tits tree is the building of $\mathrm{PGL}(2,\mathbb{Q}_p)$ [6]. Its vertices are the homothety classes of lattices in $\mathbb{Q}_p^2$; two vertices are adjacent when their lattices can be chosen to nest with index $p$. The tree is $(p+1)$-regular and infinite, and its ends correspond to the points of the projective line over $\mathbb{Q}_p$. An ultrametric hierarchy is a tree: distances arrange objects by their first point of difference, and the prime factorization of a rational number assigns it a path through the product of trees over all primes — the adelic object [6,23].

Three facts make the tree a legitimate substrate rather than a metaphor. First, it carries the counting ontology: a particle with Compton count $N_C = m/m_P \in \mathbb{Q}^+$ has a definite position in the tree via its prime factorization [23]. Second, the tree is already physics in the independent literature: holographic tensor networks have been built on Bruhat-Tits trees and buildings [7,8,9,10,11,12,21], and the representation theory of the relevant groups is an active field [15,16]. Third, the tree's place structure is the natural home of the word "regime": choosing a completion of the rationals — an archimedean or a p-adic place — chooses which tree one is on, and passing to a ramified extension changes the tree's structure in a controlled way [6]. The regime dictionary of Section 6 will use exactly this structure.

## 4. Statistics as a Tree-Automorphism Phase

### 4.1 The exchange-phase invariant

The primitive content of spin-statistics is not the boson-fermion dichotomy but the relation between the exchange phase of identical particles and their topological spin [24]:

$$R = e^{2\pi i s}$$

In three spatial dimensions the exchange is involutive, so $s \in \{0, 1/2\}$ and $R = \pm 1$; the sign is fixed by Lorentz invariance and microcausality [1]. In 2+1 dimensions the spin-statistics theorem continues to hold for particles obeying braid statistics: the phase is still $e^{2\pi i s}$, with fractional $s$ permitted [4]. The same invariant therefore covers bosons, fermions, and abelian anyons; dimension enters only by quantizing the allowed values of $s$ [24]. A distinction-based calculus exhibits the same structure: the exchange phase is the $(2s)$-fold half-turn of the re-entrant mark, $R = (e^{i\pi})^{2s}$ [25].

### 4.2 The category is the parameter

The word "spin" means different things in the two catalogs, and diagrams do not resolve the difference — the category does. In the symmetric setting, exchange is involutive: wires untangle, two crossings cancel, and the statistics content is captured by the symmetric group $S_n$; this is the three-dimensional case, and it is the case silently fixed by a Hilbert-space semantics. In the braided setting, exchange is genuinely braided: wires do not untangle, and the statistics content is captured by the braid group $B_n$ with the ribbon twist $\theta = e^{2\pi i s}$ [20,26]. The same diagrams, two categories, two spins.

The tree supplies the parameter that chooses the category. At an unramified evaluation of the tree, the symmetric collapse applies: exchange is involutive, statistics phases are exactly $\pm 1$, and the Standard Model reading holds. On a ramified branch, the braided setting applies: exchange is non-involutive, the twist $\theta = e^{2\pi i s}$ is a genuine root of unity, and the anyon reading holds. This is the constructive content of the framework's statistics claim: the tree adds a single parameter — place and ramification — that selects which statistical setting applies, and it is the same parameter that separates the free regime from the dressed regime. The framework does not re-derive the spin-statistics theorem; it locates the place where each of its readings holds.

## 5. The Unified Pattern Table

Every entry in both catalogs receives a five-field address:

$$\text{address} = (\text{place}, \text{branch}, \text{node class}, N_C^*, \text{statistics phase})$$

The node class is one of three: edge (fermionic — the traversal picks up a half-turn, phase $-1$), vertex (bosonic — the traversal is trivial, phase $+1$), or composite (a rational-function node whose effective Compton count $N_C^*$ is a function of the background counts, Section 7). Two transformations are allowed between addresses, and only two: the change of place (the adelic map) and the rational-function composition that defines $N_C^*$. Nothing else may be invoked to fit an entry.

### 5.1 Standard-Model sector

| Entry | Spin | Statistics phase | Node class | Place |
|---|---|---|---|---|
| electron, muon, tau | 1/2 | $-1$ | edge | unramified |
| up, down, charm, strange, top, bottom | 1/2 | $-1$ | edge | unramified |
| electron, muon, tau neutrinos | 1/2 | $-1$ | edge | unramified |
| photon | 1 | $+1$ | vertex | unramified |
| eight gluons | 1 | $+1$ | vertex | unramified |
| W and Z bosons | 1 | $+1$ | vertex | unramified |
| Higgs scalar | 0 | $+1$ | vertex or composite | unramified |

The neutrino rows carry an open question: if neutrinos are Majorana, their node class differs from the Dirac reading; the table does not adjudicate this. The Higgs row carries a similar openness: the elementary reading assigns a vertex class, the composite reading assigns a rational-function node, and both are consistent with the statistics phase $+1$. The framework records the ambiguity and does not resolve it.

### 5.2 Condensed-matter sector

| Entry | Spin | Statistics phase | Node class | Place |
|---|---|---|---|---|
| phonon | 0 | $+1$ | composite vertex | ramified |
| magnon | 0 | $+1$ | composite vertex | ramified |
| exciton | 0 | $+1$ | composite vertex | ramified |
| Cooper pair | 0 | $+1$ | composite vertex | ramified |
| quasielectron | 1/2 | $-1$ | dressed edge | ramified |
| composite fermion | 1/2 | $-1$ | dressed edge | ramified |
| Laughlin quasiparticle, $\nu = 1/3$ | 1/6 | $e^{2\pi i/3}$ | ramified branch node | ramified |

The anyon rows are restricted to abelian anyons: their phases are roots of unity, and the table records them as such. Non-abelian anyons — the Moore-Read excitation with matrix-valued statistics [5,22] — are outside the phase reading; the table marks the extension to automorphism representations of the tree as an open problem rather than absorbing it.

### 5.3 Status of the table

For every known entry, the assignments above recapitulate established results: the phases are the phases of the spin-statistics theorem [1,4], the composite nodes are the standard quasiparticles [17,27], the anyon phases are the standard Laughlin phases [3,20]. The table's value is not that it fits what is known; any framework with enough labels can fit a finite list. Its value is that the address scheme was fixed in advance, with two allowed transformations and no others, so that future entries — excitations not yet characterized — can be tested against it. The evidential weight of the scheme accrues only from those future entries.

## 6. The Regime Dictionary

| Tree structure | Physical regime | Mechanism |
|---|---|---|
| Unramified evaluation | Free Standard-Model particles; exact phases $\pm 1$ | Symmetric exchange; spin-statistics [1] |
| Ramified p-adic branch | Two-dimensional systems; fractional statistics | Braided exchange; twist $\theta = e^{2\pi i s}$ [4,20] |
| Composite node at depth $n$ | Quasiparticle dressing of order $n$ | Effective count $N_C^*$ as rational function [27] |
| Finite quotient of the tree | Emergence of anyons in lattice systems | Lattice symmetry opens root-of-unity phases [28,29,30] |

The dictionary says when each reading applies. The same tree, read at different places and with different composition depths, yields the two catalogs. No dynamics is introduced anywhere in this paper: the dictionary is a statement about classification, not about forces.

## 7. Quasiparticles as Rational-Function Nodes

A quasiparticle's effective mass depends on its environment; in the counting ontology its effective Compton count is a rational function of the background counts [27]:

$$N_C^*(\alpha) = f(N_C^{\text{bare}}, N_C^{\text{lattice}}, \ldots)$$

This is the precise sense in which a quasiparticle is a composite node: its address is computed from the addresses of its constituents and its host. The reading is scoped. It holds for weakly interacting composites — band electrons, phonons, excitons, Cooper pairs in the weak-coupling regime. It does not hold for strongly correlated scales: the BCS gap is exponential in the coupling [2], and heavy-fermion masses inherit an exponential scale. Those regimes are outside the rational-function reading, and the framework says so rather than absorbing them.

## 8. Epistemic Status

The paper's premises end at five named inputs, none derived here: the Compton count as the only primitive [23]; the Bruhat-Tits tree as the state-space geometry [6,23,31,32]; the exchange-phase invariant $R = e^{2\pi i s}$ for spin-statistics [24,25,26]; the rational-function reading of quasiparticle masses [27]; and the p-adic braid phases of abelian anyons [28,29,30]. The derived content is the assembly: the unified table of Section 5, the regime dictionary of Section 6, and the falsifiability conditions of Section 9.

Three honest limits follow. First, for every known entry the table is a retrodiction in the strict sense: it reorganizes established results, and it claims no more. Second, the framework does not re-derive the spin-statistics theorem; in three dimensions the phases are forced by Lorentz invariance and microcausality without any tree [1], and in 2+1 dimensions by the anyon spin-statistics theorem [4]. What the tree contributes is a single parameter that selects which statistical setting applies — the same parameter that separates free particles from dressed excitations. Third, the non-abelian regime is open, and the Higgs question is recorded but not adjudicated. A reader who holds that the two catalogs are unrelated is holding the null hypothesis; the paper's task is to make the alternative precise enough to be tested.

## 9. Falsifiability Conditions

Four conditions were pre-registered with the address scheme.

1. A fundamental particle whose statistics phase is not a tree-automorphism phase — for example a fundamental fermion with integer spin, or statistics outside the root-of-unity set — falsifies the statistics reading.
2. A weakly interacting composite quasiparticle whose effective Compton count is not a rational function of the background counts falsifies the quasiparticle reading. Strongly correlated scales are exempt by the stated scope.
3. A physical system exhibiting braid statistics with a phase that is not a root of unity falsifies the anyon reading. The condition is restricted to abelian anyons; non-abelian statistics is a separate question.
4. A Standard-Model particle that cannot be assigned a unique tree address consistent with its spin, charge sector, and statistics falsifies the table.

These conditions are the same ones that bound the framework's claims in Sections 5-8: the paper is a conjecture with a kill-test ledger, not an achieved result.

## 10. What a Practitioner Can Do With This

Four concrete uses follow from the table, each stated in engineering terms.

**1. Excitation classifier.** Given a measured excitation — its statistics phase (from interferometry or transport), its mass or effective mass, and its composition — the address scheme returns a tree address and a catalog match. A practitioner characterizing a new fractional quantum Hall plateau or a new moire material can run the excitation through the scheme and read off whether its address is consistent with the table or falls outside it (condition 3). The implementation is a lookup table plus a braid-phase calculator: phases are computed as roots of unity from the filling fraction, and the node class from the effective-mass ratio.

**2. Cross-catalog spec sheet.** The table doubles as a translation dictionary between the two catalogs: the photon and the phonon are both vertex nodes at their respective places; the Cooper pair and the composite Higgs are both composite nodes; the electron and the quasielectron are the same edge class, dressed at the ramified place. A materials modeler can use the dictionary to transfer intuition between quantum optics and lattice dynamics, and an educator can teach one table instead of two ontologies.

**3. Topological-quantum-computing benchmark.** The anyon rows of the table form a braid-phase specification: abelian anyon phases are roots of unity fixed by the filling fraction. A topological quantum computing platform that claims an abelian anyon phase outside this set contradicts the table; a platform whose braid phases match it passes a necessary condition. The table is a checkable spec, not a theory of the platform.

**4. Diagrammatic extension.** The regime dictionary parameterizes the diagrammatic gap: the braided setting is exactly the extension a crossing calculus needs beyond the symmetric case [4,26]. A practitioner working on diagrammatic quantum computing can use the place parameter as the switch between the symmetric and braided semantics.

Each use is conditional on the regime in which it applies; the conditions are stated in the corresponding rows of the table and the falsifiability conditions of Section 9.

## 11. Conclusion

The Standard Model's particles and the condensed-matter catalog of quasiparticles and anyons are two readings of one tree. The assembly is a single pattern table with a five-field address scheme, a regime dictionary keyed to the tree's place and ramification structure, and four falsifiability conditions spanning both catalogs. The statistics reading resolves the homonymy of spin by making the category the parameter and the tree the selector of the category. The claims are bounded: the premises end at five named inputs, the known entries are retrodictions, the non-abelian regime is open, and the evidential value of the scheme rests on excitations not yet characterized. If those excitations land on consistent addresses, the table earns its keep; if any of them falls outside, the corresponding condition is the framework's exit.

## Declarations

**Funding.** This research received no external funding.

**Conflicts of interest.** The author declares no conflicts of interest.

**Data availability.** All numerical values cited are from the referenced public records; the address scheme and its pre-registered conditions are recorded in the project repository accompanying this paper.

**Code availability.** The classification tools described in Section 10 are planned; no code accompanies this version.

**Author contributions.** Rowan Brad Quni-Gudzinas conceived the unification, assembled the table, and authored the paper.

**Use of artificial intelligence.** This paper was authored by the named human author with AI assistance for drafting and verification.

**Provenance of named inputs.** Inputs [23]-[32] are prior work in the same research program; inputs [1]-[22] are external literature. All bibliographic entries were verified against live registry metadata at the time of writing.

**Prior publication.** No prior version of this assembly has been published.

**Availability of this version.** This document is a draft under the CC BY 4.0 license; the published version supersedes it.

## References

[1] S. Weinberg, "Feynman Rules for Any Spin," Physical Review 133 (1964) B1318. doi:10.1103/physrev.133.b1318

[2] J. Bardeen, L. N. Cooper, J. R. Schrieffer, "Theory of Superconductivity," Physical Review 108 (1957) 1175. doi:10.1103/physrev.108.1175

[3] R. B. Laughlin, "Anomalous Quantum Hall Effect: An Incompressible Quantum Fluid with Fractionally Charged Excitations," Physical Review Letters 50 (1983) 1395. doi:10.1103/physrevlett.50.1395

[4] J. Mund, "The Spin-Statistics Theorem for Anyons and Plektons in d=2+1," arXiv:0801.3621 (2008).

[5] N. Read, G. Moore, "Fractional quantum Hall effect and nonabelian statistics," arXiv:hep-th/9202001 (1991).

[6] V. S. Vladimirov, I. V. Volovich, E. I. Zelenov, "p-Adic Analysis and Mathematical Physics," World Scientific (1994). doi:10.1142/1581

[7] M. Marcolli, "Holographic Codes on Bruhat-Tits buildings and Drinfeld Symmetric Spaces," arXiv:1801.09623 (2018).

[8] A. Bhattacharyya, L.-Y. Hung, Y. Lei, W. Li, "Tensor network and (p-adic) AdS/CFT," Journal of High Energy Physics 01 (2018) 139. doi:10.1007/jhep01(2018)139

[9] L.-Y. Hung, W. Li, C. M. Melby-Thompson, "p-adic CFT is a holographic tensor network," Journal of High Energy Physics 04 (2019) 170. doi:10.1007/jhep04(2019)170

[10] E. Gesteau, M. Marcolli, S. Parikh, "Holographic tensor networks from hyperbolic buildings," Journal of High Energy Physics 10 (2022) 169. doi:10.1007/jhep10(2022)169

[11] M. Heydeman, M. Marcolli, S. Parikh, "Nonarchimedean holographic entropy from networks of perfect tensors," Advances in Theoretical and Mathematical Physics 25 (2021) 591. doi:10.4310/atmp.2021.v25.n3.a2

[12] S. S. Gubser, "A p-adic version of AdS/CFT," Advances in Theoretical and Mathematical Physics 21 (2017) 1655. doi:10.4310/atmp.2017.v21.n7.a3

[13] S. S. Gubser, C. Jepsen, B. Trundy, "Spin in p-adic AdS/CFT," Journal of Physics A 52 (2019) 144004. doi:10.1088/1751-8121/ab0757

[14] L. Chen, X. Liu, L.-Y. Hung, "Bending the Bruhat-Tits Tree II: the p-adic BTZ Black hole and Local Diffeomorphism on the Bruhat-Tits Tree," arXiv:2102.12024 (2021).

[15] A.-M. Aubert, "Bruhat-Tits buildings, representations of p-adic groups and Langlands correspondence," arXiv:2306.06735 (2023).

[16] Y. A. Neretin, "On p-adic colligations and 'rational maps' of Bruhat-Tits trees," arXiv:1301.5453 (2013).

[17] L. Savary, L. Balents, "Quantum spin liquids: a review," Reports on Progress in Physics 80 (2017) 016502. doi:10.1088/0034-4885/80/1/016502

[18] M. Sato, Y. Ando, "Topological superconductors: a review," Reports on Progress in Physics 80 (2017) 076501. doi:10.1088/1361-6633/aa6ac7

[19] S. Ryu, A. P. Schnyder, A. Furusaki, A. W. W. Ludwig, "Topological insulators and superconductors: tenfold way and dimensional hierarchy," New Journal of Physics 12 (2010) 065010. doi:10.1088/1367-2630/12/6/065010

[20] F. Wilczek, "Anyons and the Fractional Quantum Hall Effect," Lecture Notes in Physics Monographs 68 (1992). doi:10.1007/978-3-540-47466-1_8

[21] M. Marcolli, "Holographic codes on Bruhat-Tits buildings and Drinfeld symmetric spaces," Pure and Applied Mathematics Quarterly 16 (2020) 1. doi:10.4310/pamq.2020.v16.n1.a1

[22] N. Read, "Non-Abelian adiabatic statistics and Hall viscosity in quantum Hall states and p_x+ip_y paired superfluids," arXiv:0805.2507 (2008).

[23] R. B. Quni-Gudzinas, "ODR Thesis: The Compton Count as the Only Primitive," Zenodo (2026). doi:10.5281/zenodo.21780909

[24] R. B. Quni-Gudzinas, "The Boson/Fermion Distinction: Spin-Statistics as Structural Invariant," Zenodo (2026). doi:10.5281/zenodo.21962904

[25] R. B. Quni-Gudzinas, "The Exchange Phase as a Logical Scalar: R = e^(2 pi i s) from the Re-Entrant Calculus," Zenodo (2026). doi:10.5281/zenodo.21941184

[26] R. B. Quni-Gudzinas, "Configuration-Space Topology and the Distinction Calculus: The Exchange Scalar, Its +-1 Shadow, and a Pre-Registered Derivation Program," Zenodo (2026). doi:10.5281/zenodo.21957291

[27] QNFO, "Quasiparticles as Rational Functions: Extending ODR to Condensed Matter," Zenodo (2026). doi:10.5281/zenodo.21768756

[28] R. B. Quni-Gudzinas, "p-Adic Anyon Fusion and Braiding: Quantum Groups at Roots of Unity," Zenodo (2026). doi:10.5281/zenodo.21208491

[29] R. B. Quni-Gudzinas, "Adelic Synthesis: The Pattern-Particle Correspondence and the Complete Arithmetic Theory of Anyons," Zenodo (2026). doi:10.5281/zenodo.21208568

[30] R. B. Quni-Gudzinas, "p-Adic Braid Groups on Bruhat-Tits Buildings," Zenodo (2026). doi:10.5281/zenodo.21208366

[31] R. B. Quni-Gudzinas, "Compton Frequency Cross-Ratios on Bruhat-Tits Trees: A Pre-Registered Search for Adelic Structure in the Standard Model Mass Spectrum," Zenodo (2026). doi:10.5281/zenodo.21485556

[32] R. B. Quni-Gudzinas, "The Adelic Cross-Domain Program v5.0: From the Fine-Structure Constant to the Standard Model Mass Spectrum via Bruhat-Tits Trees," Zenodo (2026). doi:10.5281/zenodo.21698355

[33] R. B. Quni-Gudzinas, "Signal-Worker Boundary Confinement: A Corrected Ontology of Surface vs Bulk Transport," Zenodo (2026). doi:10.5281/zenodo.21974194
