# Practical Applications Extension — QNFO.UMP.013 (Stage 9, MANDATORY)

**Date:** 2026-08-19 · **Status:** COMPLETE

## Candidate A — Unified pattern table (address scheme: place, branch, node class, N_C*, phase θ)

### A1. Anyon phase spec-sheet for topological-quantum-computing platforms
- **Operational signature:** a lookup table mapping measured statistics phase θ to tree address (ramified branch prime q) — inputs: θ from interferometry; outputs: address + allowed fusion set.
- **Domain-specific falsifiable claim:** every abelian FQH anyon phase measured in any material equals e^{2πi p/q} with q prime and q = branch valuation (disconfirmation: any phase not a root of unity — F3).
- **Calibration entry:** [CHECK: 2029] ≥3 abelian FQH systems yield phases matching the table within experimental error.

### A2. Materials-informatics excitation classifier (SDK/decision tool)
- **Operational signature:** given (measured m*, θ, composition) → canonical tree address; cross-check across measurement methods (transport, interferometry, ARPES).
- **Domain-specific falsifiable claim:** addresses are method-invariant (disconfirmation: same excitation classified differently by two accepted measurement methods).
- **Calibration entry:** [CHECK: 2028] classifier reproduces the published catalog with 0 phase-address conflicts (P1).

### A3. SM ↔ condensed-matter spec-sheet dictionary (engineering reference)
- **Operational signature:** rows map SM particles to CM analogues with renormalization rules (electron ↔ quasielectron with N_C*; photon ↔ phonon/edge mode; composite Higgs ↔ Cooper-pair node) — usable in device-modeling handbooks and graduate curricula.
- **Domain-specific falsifiable claim:** every mapping carries its regime condition (holds only where premise applies); no mapping presented as unqualified identity.
- **Calibration entry:** none (translation artifact; retrodiction-labeled).

## Candidate B — Place-parameterized diagram calculus

### B1. ZX/fusion-calculus extension with tree-place parameter
- **Operational signature:** a diagram calculus whose crossing rule is parameterized by the tree place (unramified → involutive σ²=1; ramified → braid σ²≠1 with θ); a braid-phase calculator tool computes θ from (place, branch).
- **Domain-specific falsifiable claim:** reproduces Laughlin e^{2πi/3} and known abelian FQH braid outcomes WITHOUT per-system ad-hoc phase inputs (P4; disconfirmation: per-system inputs required).
- **Calibration entry:** [CHECK: 2028] P4 implementation test on ≥3 published FQH braid experiments.

### B2. Tree-branch encoding for quantum simulation of anyons
- **Operational signature:** simulator encoding where anyon states are indexed by ramified-branch addresses (primes q), not by arbitrary labels; fusion-rule verification uses the address arithmetic.
- **Domain-specific falsifiable claim:** fusion outcomes match UMTC predictions for all abelian inputs in the simulator (disconfirmation: mismatch on any abelian input).

## Candidate C — Regime dictionary as pre-registration scaffold

### C1. Moiré/FQH anyon-search scaffold
- **Operational signature:** pre-declared expected phase sets per candidate system (θ = e^{2πi p/q} with the system's symmetry-dictated q); a decision procedure for accepting/rejecting a characterization claim.
- **Domain-specific falsifiable claim:** a new anyon system's phase lands in the pre-declared set OR the framework is wrong (no absorption); **this is the KIF-60 C3 evidential-weight vehicle (REG-UMP013-001).**
- **Calibration entry:** [CHECK: 2029] P2 — first new-system characterization.

### C2. Curriculum/benchmark suite
- **Operational signature:** worked problems mapping statistics phase ↔ tree address for pedagogical use; benchmark set for classifier tools.
- **Domain-specific falsifiable claim:** students/devs using the suite make no statistics-phase assignment errors on the benchmark set (weak, internal).

## Stage 9 gate output
2-5 application domains per candidate ✓ (A:3, B:2, C:2) · operational signature per pair ✓ · domain-specific falsifiable claims ✓ · additional calibration register entries ✓ (4 added: [CHECK: 2029]×2, [CHECK: 2028], [CHECK: 2028]).
