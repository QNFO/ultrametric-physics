# Improvement Audit — QNFO.UMP.013 v0.4 → v0.5 candidate

**Date:** 2026-08-20 · **Gate:** CMD EXECUTE RED TEAM — "Is this the best we can do? Are there other QNFO publications or external papers that may inform an improved new version?" · **Status:** COMPLETE
**Target:** published v0.4 (10.5281/zenodo.22022313), 55 files, references.bib (33 entries)

## 1. Verdict

**v0.4 is NOT the best we can do.** The published paper is scientifically clean (three red-team rounds, zero open HARD findings), but the reference set has material gaps — both canonical external works and high-value internal corpus works — and one structural opportunity: the paper's central evidential vehicle (REG-UMP013-001 / prediction P2) has **live test data available since 2023–2025 that the paper does not engage**. A v0.5 is warranted.

## 2. External gaps (canonical works missing from references.bib)

| # | Work | Why it matters | Where it belongs |
|---|---|---|---|
| E1 | **Arovas, Schrieffer, Wilczek 1984** (PRL 53, 722) — exchange phase e^{iπ/m} | **The paper's own docs/unified-pattern-table.md attributes the e^{iπ/3} Laughlin exchange phase to "Arovas–Schrieffer–Wilczek" by name, but references.bib has NO entry for it.** The attribution exists in the docs table (§1.2) without a bibliographic record — a citation-completeness defect of the same class already remediated in v0.2/v0.3. | §2.2, §5.2, docs table |
| E2 | **Jain 1989** (PRL 63, 199) — composite fermions | §2.2 explicitly names "the composite fermion the attached-flux object of the fractional quantum Hall effect [3,20]" — cites Laughlin + Lerda but NOT Jain's composite-fermion paper. Canonical reference missing. | §2.2 |
| E3 | **Leinaas & Myrheim 1977** (Nuovo Cim. 37B, 1) | The ORIGINAL anyon paper. §4's statistics discussion traces braid statistics without citing its origin. | §2.2, §4 |
| E4 | **Wilczek 1982** (PRL 49, 957) — "Quantum Mechanics of Fractional-Spin Particles" | Coined "anyons". Missing from an anyon paper. | §2.2, §4 |
| E5 | **Halperin 1984** (PRL 52, 1583) — statistics of FQHE quasiparticles | Canonical companion to Laughlin. | §2.2, §5.2 |
| E6 | **Kitaev 2003** (Ann. Phys. 303, 2) — fault-tolerant TQC by anyons | §10.3 presents a "topological-quantum-computing benchmark" without the canonical anyonic-TQC reference. | §10.3 |
| E7 | **Nayak et al. 2008** (Rev. Mod. Phys. 80, 1083) — non-Abelian anyons and TQC | §2.2/§8 discuss non-abelian anyons (Moore–Read) without the canonical review. | §2.2, §8 |
| E8 | **Fredenhagen, Rehren, Schroer 1989** (Commun. Math. Phys. 125, 613) — braid-group statistics (plektons) in QFT | The QFT lineage behind Mund's theorem; strengthens §4.1's historical grounding. | §4.1 |

## 3. External experimental gap — the C3 vehicle has live test data (HIGHEST VALUE)

| # | Experiment | Data | Relevance |
|---|---|---|---|
| E9 | **Cai et al. 2023** (arXiv 2304.08470, tMoTe₂) | FQAH signatures at ν = −2/3 and −3/5 | **Exactly the "new abelian anyon system characterized in a 2D material" that REG-UMP013-001/P2 was pre-registered to catch.** The paper's central evidential vehicle (C3) is currently promissory ("excitations not yet characterized"); these 2023–2025 experiments are its first real test set. |
| E10 | **Zeng et al. 2023** (arXiv 2305.00973, tMoTe₂) | Integer + fractional Chern insulators at ν = 1, 2/3 | Same: first zero-field fractional Chern insulators in semiconductor moiré. |
| E11 | **Park et al. 2023** (ν=1/3 FQAH, tMoTe₂; Nature 622, 74) | Fractionally quantized anomalous Hall effect at ν = 1/3 | The Laughlin-type case the paper's §5.2 table treats — now measured in a material. |
| E12 | **Lu et al. 2024** (pentalayer graphene FQAH) | ν = 1/3, 2/3, 3/5 in rhombohedral graphene | Second platform; strengthens the "regime dictionary is platform-independent" claim. |

**Structural recommendation:** a v0.5 should add a short "first tests" passage (or a §5.3 extension) applying the pre-registered address scheme to these systems: predicted phases (ν=2/3 → θ with denominator 3; ν=1/3 → e^{iπ/3} exchange) vs. measured signatures, and update REG-UMP013-001 status to "first data in hand, address scheme applied." This converts the paper's only promissory element into a tested one — the single largest improvement available.

## 4. Internal corpus gaps (QNFO works NOT cited in v0.4)

| # | Slug | Why it matters | Where |
|---|---|---|---|
| I1 | **ultrametric-quantum-computation-langlands** | Directly relevant to FQ1 (automorphism representations / Langlands correspondence on the tree) — the paper's open problem #1 has in-corpus machinery. | §8, FQ1 (registry) |
| I2 | **spectral-dynamics-on-bruhat-tits-trees** + **ballistic-transport-on-the-bruhat-tits-tree** ("Bruhat-Tits Tree as a Unifying Geometric Object") | Tree DYNAMICS exists in-corpus — partially answers the day-2 critique's "no Hamiltonian" charge by showing the corpus's tree-dynamics program; §3 should cite. | §3 |
| I3 | **structural-mediation-of-planckian-dissipation-in-strongly-correlated-electron-systems** + **superconductivity-quadrangle** | The strong-correlation regime that §7 explicitly exempts — citing in-corpus work on it sharpens the exemption from "ignored" to "corpus-aware scoping." | §7 |
| I4 | **operationalizing-generalized-symmetries** (external Zenodo 18199397, in KG) | "Anyon Halos and Stretched Exponential Splitting in Moiré Superlattices" — a falsifiable dictionary for moiré anyon systems; the direct experimental bridge for REG-UMP013-001. | §5.3/§10, REG-001 |
| I5 | **zbw-p5-capstone-synthesis** + **zbw-majorana-tqc-p3-bruhat-tits-readout** (and p1/p2 series) | Majorana/ZBW topological fermion distinction + BT readout protocol — in-corpus machinery for the §5.1 Majorana open question and §10.3 readout. | §5.1, §10.3 |
| I6 | **adelic-core-synthesis** + **consilience-physics-numtheory** + **wbs-6-five-pillars-consilient-synthesis** | The adelic-QFT foundations and cross-pillar consilience context behind premise 2 ("tree as correct state-space geometry"). | §1, §3 |
| I7 | **beyond-the-qubit** ("Constructive Paradigms for Post-Particle Computation") | Practitioner-facing post-particle computation framing; enriches §10's engineering language. | §10 |

## 5. Gap classification & severity

- **HARD-adjacent (citation integrity):** E1 (docs attribute a result to a work absent from the bibliography), E2 (named concept, uncited origin). Same class as the v0.2 H-1/H-2 concept-DOI findings — a reader following the docs table cannot find ASW in the bibliography.
- **HIGH-VALUE structural:** E9–E12 — the C3 vehicle's first live test data, absent.
- **SOFT (completeness):** E3–E8 canonical canon; I1–I7 internal engagement.
- **Not re-litigating:** scientific content, scope discipline, epistemic posture — all passed three red-team rounds; the day-2 critique's charges were verified not-sustained.

## 6. Recommendation

**Yes — a v0.5 newversion is warranted**, scoped as:
1. Add E1–E8 + I1–I7 to references.bib (verify each live at build time per P3.AUTHOR-GATE; E9–E12 via arXiv/Crossref).
2. Add a "First tests" passage applying the address scheme to the moiré FQAH systems (E9–E12) — predicted phases vs. measured; update REG-UMP013-001 status.
3. Cite the tree-dynamics corpus (I2) in §3 and the strong-correlation corpus (I3) in §7.
4. Update §5.1 Majorana note (I5), §8/FQ1 (I1), §10 (I4, I7).
5. Re-run all gates (PANDOC-SAFE, INTERNAL-REF, title-dup, 33→~50 refs cited==received), publish, R2/D1/KG/registry sync per the established loop.

Estimated delta: content changes are additive and modest (~2–4 pages equivalent); the value jump is in the reference integrity and the C3 vehicle becoming data-tested. Cost: one standard newversion cycle. **Recommendation: proceed with v0.5 in the next CMD EXECUTE cycle.**
