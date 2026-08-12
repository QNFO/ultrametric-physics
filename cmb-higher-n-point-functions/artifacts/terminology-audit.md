# Terminology Audit (BP-2) — QNFO.UMP.007 (CMB Higher n-Point Functions)

**Date:** 2026-08-12 · **Phase:** P5 (BP-2) · **WBS:** `QNFO.UMP.007.P5.BP2`
**Created:** v0.2 post-audit (Completeness-audit SOFT finding; BP-2 documented)

---

## 1. Field-specific terms used in the paper vs standard definitions

| Term | Standard definition | Paper usage | Match |
|:-----|:--------------------|:------------|:------|
| **Reduced bispectrum f_NL** | Scale-invariant amplitude of the 3-point function, defined via ⟨ζζζ⟩ ∝ (6/5) f_NL P²/(k1k2k3)² | §2.1 — standard definition | ✅ |
| **Equilateral/local/orthogonal templates** | Standard CMB bispectrum shape families | §2.1 base shapes — standard | ✅ |
| **Resonant-feature family** | Oscillatory bispectrum shapes with free frequency from feature/resonance inflation | §3.3 — matches Leblond–Pajer/Barnaby–Cline usage | ✅ |
| **Log-periodic oscillations** | Periodic modulation in log-scale (discrete scale invariance) | throughout — standard DSI terminology | ✅ |
| **p-adic / ultrametric** | Valuation-based hierarchical structure; discrete scale invariance under pⁿ scaling | §1 — standard | ✅ |
| **Rayleigh frequency resolution** | 2π/log-dynamic-range — minimum separable frequency separation | §3.1 — standard signal-processing usage | ✅ |
| **Shape correlation C(S_a,S_b)** | Fergusson–Liguori–Shellard-style inner product over the tetrahedron | §3.1 — matches literature | ✅ |
| **LOOK-ELSEWHERE effect** | Trials-factor penalty when scanning multiple frequencies/radices | scope note §7 — standard | ✅ |
| **KIF-60 / RQ-013** | — | **REMOVED in v0.2** (internal identifiers scrubbed per INTERNAL-REF-1) | ✅ fixed |

## 2. Terms checked and rejected

| Term | Verdict |
|:-----|:--------|
| "cosmological constant problem" | not used |
| "non-Gaussianity" | standard, used correctly |
| "bispectrum amplitude" | standard, used correctly |
| "single-modulation model" | project-defined; explicitly defined in §4 and scope note — acceptable as it is defined in-text |

## 3. Gate status

**PASS** — all field-specific terms match standard definitions; the one project-specific
term ("single-modulation model") is explicitly defined in-text. Internal identifiers
(KIF-60, RQ-013) removed in v0.2.
