# H1 External Benchmark Design — QNFO.UMP.014 P3

> **Date:** 2026-08-28 · **Status:** design + pre-registration content + implementation smoke suite (P3-exec = dataset acquisition and full runs)
> Companion artifacts: `scripts/sim-statistical-signatures-smoke.py` (implementation check, stdlib, seeded), `artifacts/verification/`.

## 1. Objective

Execute the surviving empirical claim — H1 (component iii) — with the failure-mode-corrected
methodology prescribed by the 2026-08-28 notes (_26240202016, _26240201803, _26240195905):
**asymptotic statistical distributions in large-N systems, not exact finite geometry.**
The question is no longer "is this matrix ultrametric?" but "do physical spectral
distributions carry arithmetic information beyond universal random-matrix statistics?"

## 2. The five observables (H-DIST-3a..3e)

| # | Observable | Definition | Null (universal) | Arithmetic signature |
|---|---|---|---|---|
| 3a | Pair correlation | R₂(s) = density of normalized level pairs at spacing s after unfolding | GUE: 1 − (sin πs/πs)² | zeta-type corrections beyond the universal term (Bogomolny–Keating) |
| 3b | Spectral form factor | K(τ) = ⟨\|Σₙ e^{iτλₙ}\|²⟩ | GUE: linear ramp → plateau; Poisson: flat | arithmetic-modified ramp (modular-surface features) |
| 3c | Number variance / rigidity | Σ²(L) = Var of level count in windows of length L; Δ₃(L) integrated | GUE: (1/π²)log L; Poisson: L | arithmetic intermediate statistics |
| 3d | Partition thermodynamics | Bost–Connes: Z(β) = ∏ₚ(1−p⁻ᵝ)⁻¹ = ζ(β) | smooth ideal-gas C_V | phase transition at β = 1 (ζ pole), Galois symmetry breaking, zeta specific-heat singularity |
| 3e | Log-periodic corrections | f(x) = x^α(1 + ε·cos(2π log x/log λ) + O(ε²)) | ε = 0 (pure scaling) | subleading periodic corrections; the robust quantity is the period log λ, not the amplitude ε |

## 3. Null models

1. **Pure GUE** (random-matrix): unitary Gaussian ensemble statistics for the unfolded spectrum.
2. **Poisson**: uncorrelated levels (integrable-system reference).
3. **Random hierarchy**: a null hierarchy fitted to the same data (guards against finding
   hierarchy where any clustering would do) — the toolbox's H-DIST-4 component.

The falsification criterion (fixed at P5 OSF pre-registration): **pure GUE statistics with no
arithmetic corrections in N ≳ 10³ systems falsifies the program at the statistical-distribution
level** — this is the H1 leg of the 2028 decision point. A certified null here is a result.

## 4. Candidate large-N systems (N ≳ 10³ levels)

| System | N | Access | Notes |
|---|---|---|---|
| Heavy-nuclei level sequences | 10³–10⁴ | ENSDF/NuDat public data | the canonical RMT testbed; unfolding protocol well established |
| Molecular rovibrational spectra | 10³–10⁵ | public spectral databases | low noise |
| Graphene electronic spectra | 10⁴+ | published ARPES/spectroscopy data | 2D; Dirac spectrum arithmetic structure (graphene is the notes' featured candidate) |
| Quantum-billiard experiments | 10²–10³ | published microwave-billiard spectra | experimental RMT gold standard |

The ML corpora from P1 (20 Newsgroups, RCV1, MNIST, Arcene, Covertype, Golub/TCGA) remain as
the *compression-prior* variant of H1 (H-DIST-3's original framing, now a secondary leg): the
statistical-signatures design is primary, the compression test is retained as a robustness arm
(the two are complementary: distributional signatures vs. clustering advantage).

## 5. Unfolding protocol

1. Estimate the local level density ρ(E) (polynomial/nearest-neighbor smoothing on the
   integrated density N(E)).
2. Map to unfolded positions ξₙ = N(Eₙ); the unfolded spectrum has unit mean spacing.
3. Exclude edges and known degenerate/collective bands; document every cut.
4. The same unfolding is applied to real data and to the GUE/Poisson synthetic references —
   estimator bias cancels in the comparison.

## 6. Statistical power and multiple-comparison control

- Minimum N = 10³ levels per system (below this the correlation functions lack power — FMO's 7
  sites are excluded by design, per the notes).
- Look-elsewhere correction across the five observables × the λ-grid of 3e (Bonferroni–Holm on
  the primary tests; the corrected pair-correlation deviation is the single primary test).
- Effect sizes pre-registered per observable; the placeholder global threshold is p ≥ 0.01 after
  correction.

## 7. Pre-registration content (drafted; fixed at P5)

- H-DIST-3a: the unfolded pair correlation deviates from pure GUE by zeta-type corrections of
  pre-registered magnitude in ≥ 1 large-N system.
- H-DIST-3b: the form factor ramp deviates from the pure GUE ramp in the same systems.
- H-DIST-3c: number variance growth lies between GUE (1/π²)log L and Poisson L with the
  arithmetic coefficient class.
- H-DIST-3d: a Bost–Connes-type phase transition is identifiable in an engineered or natural
  prime-indexed thermodynamic system.
- H-DIST-3e: log-periodic subleading corrections with period log λ in the pre-registered window.
- Decision rule: if 3a–3e all return null at the pre-registered thresholds in all candidate
  systems, the H1 leg is certified null → feeds the 2028 decision point as a published result.

## 8. Implementation smoke suite (this phase)

`scripts/sim-statistical-signatures-smoke.py` verifies the ESTIMATOR IMPLEMENTATIONS on known
answers (stdlib-only, seeded): Bost–Connes critical behavior — the ζ-pole amplitude
β²/(β−1)² and the finite-β Bose/Fermi channel contrast (3d); number-variance rigidity vs
Poisson separation (3c); the log-periodic period detector recovering a known λ (3e); the
pair-correlation estimator recovering the flat R₂ = 1 of a Poisson spectrum (3a). The GUE
synthetic arm (needs matrix diagonalization) is deferred to P3-exec with numpy — the
analytic GUE curves are used as references in the smoke suite.

## 9. P3-exec execution plan

1. Acquire ≥ 2 large-N datasets (ENSDF nuclear levels; one molecular/rovibrational database).
2. Implement the GUE synthetic reference (numpy Hermitian ensemble) + full estimators.
3. Run the five observables on real + synthetic spectra; report corrected p-values per §6.
4. Freeze results → OSF pre-registration of the H-DIST-3 disconfirmation criterion (P5).
