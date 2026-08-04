# WBS: QNFO.UMP.003

## Charter
Formalize the adelic distinction framework — the universe as a dynamical distinction network over the adeles — into a publishable research paper. The seed material (Obsidian note `_26216083410.md`, 2026-08-04) spans 4 iterations of dialogue synthesis connecting valuation theory, idele class groups, Bruhat-Tits trees, automorphic representations, and all of particle physics/cosmology.

## Core Claim
The universe is a dynamical distinction network over the adeles. Its fundamental entities are rational frequency ratios (idele-class characters). Particles are automorphic representations carrying invariant Compton valuations. All of physics — spin, charge quantization, three generations, QFT, CPT, Higgs, dark matter, dark energy, time, quantum gravity — derives from the structure of the unit idele class group and its moduli space.

## Phases (WBS)
| Phase | WBS Code | Description |
|:------|:---------|:------------|
| P0 | QNFO.UMP.003.P0 | Init: repository, branch, PROJECT-PLAN, seed note |
| P1 | QNFO.UMP.003.P1 | Due Diligence: KG cross-ref, D1, Vectorize, external search |
| P1b | QNFO.UMP.003.P1 | Consilience Gate (KIF-29 HARD): silo-cost, cross-domain lexicon |
| P4 | QNFO.UMP.003.P4 | Deep Research: formalize note into paper.md with Forecast Protocol |
| P5 | QNFO.UMP.003.P5 | Publication: PDF build, Zenodo DOI, D1/KG seeding |
| P3.5 | QNFO.UMP.003.P3.5 | Red-team: reviewer subagent audit |

## Milestones
| Milestone | Gate Criteria |
|:----------|:-------------|
| M0: Seed | Branch created, seed note committed, PROJECT-PLAN.md approved |
| M1: Due Diligence | KG/D1/Vectorize cross-ref complete; no major overlap found |
| M2: Consilience | KIF-29 gate passed; silo-cost table + lexicon in artifacts/ |
| M3: Draft | paper.md with certainty calibration, Ostrowski-compliant formulas |
| M4: Publish | PDF built, Zenodo DOI live, D1/KG records seeded |

## Deliverable Registry
| Deliverable | Path | Format |
|:------------|:-----|:-------|
| PROJECT-PLAN.md | adelic-distinction/PROJECT-PLAN.md | Markdown |
| Seed Note | adelic-distinction/artifacts/seed-note.md | Markdown (from Obsidian) |
| paper.md | adelic-distinction/paper.md | Markdown + YAML frontmatter |
| PDF | adelic-distinction/releases/adelic-distinction-v1.0.pdf | PDF |
| Consilience Gate | adelic-distinction/artifacts/consilience-gate.md | Markdown |

## Risk Register
| Risk | Likelihood | Impact | Mitigation |
|:-----|:----------|:-------|:-----------|
| Scope explosion: note spans 15+ physics domains | HIGH | HIGH | Limit v1 to core adelic claims; defer experimental predictions to v2 |
| Prior art overlap with existing QNFO papers | MODERATE | MODERATE | Due diligence Phase 1 to map and cite prior work |
| MathJax/PDF rendering failure | MODERATE | HIGH | Pre-flight Chromium check per research v2.55 |

## Success Criteria
1. paper.md passes all QNFO publication gates (language, mojibake, Ostrowski, certainty calibration)
2. PDF built with MathJax SVG via puppeteer-core CDP
3. Zenodo DOI assigned and live
4. D1/KG records seeded with verified ownership
5. Red-team audit returns zero HARD findings
