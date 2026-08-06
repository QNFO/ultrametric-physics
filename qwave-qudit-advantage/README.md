# The Qudit Advantage: JPCUB Comparison of QWAV vs. Conventional Qubit Platforms

**WBS:** QNFO.UMP.005 | **Slug:** qwave-qudit-advantage | **Status:** Phase 0 (Initialization)

## Overview

Direct extension of **JPCUB Competitive Landscape v2.0** ([10.5281/zenodo.21821767](https://doi.org/10.5281/zenodo.21821767)) which benchmarked 17 conventional qubit-based quantum computing platforms. This paper computes the joules-per-solution (JPCUB) estimate for the **QWAV qudit architecture** — $d$-level quantum systems on Bruhat-Tits trees with p-adic stabilizer codes and hierarchical ultrametric decoding — and compares it against the qubit landscape.

## Quick Links

- [PROJECT-PLAN.md](PROJECT-PLAN.md) — Full charter, WBS, milestones, risks
- Branch: `ump/paper/qwave-qudit-advantage`
- Program: Ultrametric Physics (`QNFO/ultrametric-physics`)

## Key Distinction

| Feature | Conventional Qubits (JPCUB Landscape) | QWAV Qudits |
|:--------|:--------------------------------------|:------------|
| Hilbert space | $\mathbb{C}^2$ (qubit) | $\mathbb{C}^d$ (qudit, $d > 2$) |
| Encoding density | 1 bit per carrier | $\log_2 d$ bits per carrier |
| Error model | Active QEC (surface codes, ancillas) | Passive ultrametric resilience |
| Temperature | 10 mK (superconducting) | 300 K (room temperature) |
| Physical carriers | $\sim 10^6$ (fault-tolerant) | $\sim 10$ (low-overhead) |

## Phases

See [PROJECT-PLAN.md](PROJECT-PLAN.md) for full phase definitions and gate criteria.
