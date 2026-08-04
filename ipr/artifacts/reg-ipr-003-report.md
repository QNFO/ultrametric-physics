# REG-IPR-003 Execution Report — p-adic Valuation Test

**WBS:** QNFO.UMP.003 | **Date:** 2026-08-04 | **Status:** EXECUTED — NULL RESULT

## Summary

The pre-registered quasiparticle-criterion test was executed against PDG 2024
central masses. **The criterion does not discriminate fundamental particles
from quasiparticles using real-world measured masses.**

## Findings

1. **Decimal artifact:** v2/v5 valuations are inflated by base-10 representation.
   m_P = 122091 x 10^17; measured masses are decimal strings, so denominators
   carry 2^k 5^k from 10^k. The {2,3,5} dominance is inherited from base 10,
   not from physical prime structure.

2. **Impossible criterion:** "v_p(nu) != 0 for ALL primes up to p_max" is
   mathematically impossible for any rational (finite support). Every rational
   has v_p = 0 for all but finitely many primes.

3. **No discrimination:** Real measured masses are real-valued, not exact
   rationals. nu is representation-dependent. Particle vs quasiparticle
   discrimination cannot be performed on PDG data alone.

## Data

Full table in `reg-ipr-003-results.json`. Key rows:

| particle | nu = mP/m | v2 | v3 | v5 | v7 | v11 | v13 | #nonzero/30 |
|:---------|:----------|:---|:---|:---|:---|:----|:----|:-----------:|
| electron | 2.44e22 | 25 | 1 | 24 | -2 | -1 | 0 | 6 |
| proton | 2.54e22 | 21 | -2 | 25 | 0 | -1 | 0 | 5 |
| top | 1.22e21 | 16 | 1 | 16 | -1 | 0 | 0 | 4 |

Fully 5-smooth: 0/14. Denominator 5-smooth: 1/14.

## Implications

- The 5-smooth dominance is CONSISTENT WITH LOOK-ELSEWHERE ARTIFACT (base-10),
  triggering the BP-3 density gate: no evidence for the Pythagorean semigroup.
- A meaningful test requires a theory predicting EXACT rational nu, then
  checking measured masses against it to within experimental error.
- CAL-IPR-03 (alpha period) is unaffected but the requirement for exact
  rational predictions is strengthened.

## Verdict

REG-IPR-003 = EXECUTED, NULL RESULT. Registry next-action #1 marked
COMPLETE-WITH-NULL.
