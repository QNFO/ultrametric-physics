# Chapter 5: The p-Adic Absolute Value

*In which we invert our intuition about size, prove that the p-adic absolute value is genuinely an absolute value (satisfying the strong triangle inequality), and watch as infinite series that diverge hopelessly in the real numbers converge peacefully in the p-adic world — including the unforgettable identity 1 + 2 + 4 + 8 + ... = −1.*

---

## 5.1 Recalling the p-Adic Valuation

From Chapter 2, we defined the **p-adic valuation** `v_p(x)` for a non-zero rational number `x`. It is the exponent of the prime `p` in the unique prime factorization of `x`. Formally, if `x = p^k · (a/b)` where `p ∤ a` and `p ∤ b` (neither `a` nor `b` is divisible by `p`), then:

```
v_p(x) = k
```

We also set `v_p(0) = ∞` as a convenient convention.

Recall the key properties of `v_p`:

1. **Logarithmic Property:** `v_p(xy) = v_p(x) + v_p(y)` for all `x, y ∈ ℚ`.
2. **Ultrametric Addition Rule:** `v_p(x + y) ≥ min(v_p(x), v_p(y))` for all `x, y ∈ ℚ`. Moreover, if `v_p(x) ≠ v_p(y)`, then `v_p(x + y) = min(v_p(x), v_p(y))`.

These properties make `v_p` a **non-Archimedean valuation** on the field ℚ. But `v_p` is not an absolute value — it satisfies an additive rule, not a multiplicative one, and its values are integers (and ∞), not non-negative reals. To convert `v_p` into an absolute value, we need to "exponentiate" it. The natural choice is:

```
|x|_p = p^{-v_p(x)}
```

for `x ≠ 0`, and `|0|_p = 0`.

This definition transforms the additive property of `v_p` into a multiplicative property, and the minimum rule into a maximum rule — exactly the pattern of an ultrametric absolute value. Let us verify this thoroughly.

---

## 5.2 The Definition and Worked Examples

**Definition (p-Adic Absolute Value).** Let `p` be a prime number. For any rational number `x`, the **p-adic absolute value** of `x` is:

```
|x|_p = { 0                 if x = 0
        { p^{-v_p(x)}       if x ≠ 0
```

where `v_p(x)` is the p-adic valuation of `x`.

Because `p > 1`, the function `p^{-k}` **decreases** as `k` increases. This is the crucial inversion: numbers that are highly divisible by `p` (large positive `v_p`) have **small** p-adic absolute value. Numbers with `p` in the denominator (negative `v_p`) have **large** p-adic absolute value.

Let us compute many examples to build intuition.

**Example Group 1: Integers (p = 2)**

| Number `x` | Prime Factorization | `v₂(x)` | `\lvert x\rvert_2` | Interpretation |
|:----------:|:-------------------:|:-------:|:------------------:|:---------------|
| 0 | — | ∞ | 0 | By definition |
| 1 | 1 | 0 | 2⁻⁰ = 1 | Not divisible by 2 |
| 2 | 2¹ | 1 | 2⁻¹ = 1/2 | Divisible by 2 once |
| 3 | 3 | 0 | 1 | Odd |
| 4 | 2² | 2 | 2⁻² = 1/4 | Divisible by 4 |
| 8 | 2³ | 3 | 2⁻³ = 1/8 | Divisible by 8 |
| 12 | 2²·3 | 2 | 2⁻² = 1/4 | Divisible by 4, not 8 |
| 16 | 2⁴ | 4 | 2⁻⁴ = 1/16 | Divisible by 16 |
| 1024 | 2¹⁰ | 10 | 2⁻¹⁰ = 1/1024 | Extremely divisible by 2 |
| 2^100 | 2^100 | 100 | 2^{-100} | Astonishingly small! |

**The inversion of intuition is stark:** `2^100` is an astronomically large number — it has 31 decimal digits, roughly `1.27 × 10³⁰`. In the ordinary absolute value, it is enormous. In the 2-adic absolute value, it is `2^{-100} ≈ 7.9 × 10^{-31}` — vanishingly, subatomically small. The number that dominates in the ordinary world is negligible in the 2-adic world.

**Example Group 2: Rational Numbers (p = 2)**

| Number `x` | `v₂(x)` | `\lvert x\rvert_2` | Interpretation |
|:----------:|:-------:|:------------------:|:---------------|
| 1/2 | −1 | 2¹ = 2 | Has 2 in denominator |
| 1/4 | −2 | 2² = 4 | Quarter is "large" 2-adically |
| 1/8 | −3 | 2³ = 8 | Even larger |
| 3/4 = 3·2⁻² | −2 | 4 | Denominator has 2² |
| 3/2 = 3·2⁻¹ | −1 | 2 | Half of 3 |
| 5/8 | −3 | 8 | |
| 7 | 0 | 1 | 7 is odd |
| 3/7 | 0 | 1 | Neither num nor denom has 2 |

Notice the beautiful symmetry: integers that are multiples of higher powers of `p` become smaller; fractions with higher powers of `p` in the denominator become larger. All odd integers (and all fractions with no factor of 2 in numerator or denominator) have 2-adic absolute value exactly 1. They form the "unit sphere" in the 2-adic world — numbers of intermediate size.

**Example Group 3: Different Primes**

| Number `x` | `v₂(x)` | `\lvert x\rvert_2` | `v₃(x)` | `\lvert x\rvert_3` | `v₅(x)` | `\lvert x\rvert_5` |
|:----------:|:-------:|:------------------:|:-------:|:------------------:|:-------:|:------------------:|
| 12 | 2 | 1/4 | 1 | 1/3 | 0 | 1 |
| 18 | 1 | 1/2 | 2 | 1/9 | 0 | 1 |
| 30 | 1 | 1/2 | 1 | 1/3 | 1 | 1/5 |
| 7 | 0 | 1 | 0 | 1 | 0 | 1 |

The number 12 is small 2-adically (divisible by 4), moderately small 3-adically (divisible by 3), and "unit-sized" 5-adically (not divisible by 5). Each prime gives a different perspective — a different "lens" through which to view the number. The number 7 is unremarkable from the perspective of any small prime — it is a unit in all of them.

This is the **local** nature of the p-adic absolute values: each prime `p` gives a different measurement of "size," capturing a different aspect of the number's multiplicative structure. To fully understand a rational number, you need to know its size in the ordinary sense AND its sizes in all the p-adic senses.

---

## 5.3 Proof: |·|_p Is a Non-Archimedean Absolute Value

We must verify that `|·|_p` satisfies the three axioms of an absolute value (Chapter 2) and, in fact, the stronger ultrametric inequality.

**Axiom 1: Positive Definiteness.** We must show `|x|_p ≥ 0` for all `x`, and `|x|_p = 0` iff `x = 0`.

- If `x = 0`, then `|x|_p = 0` by definition.
- If `x ≠ 0`, then `|x|_p = p^{-v_p(x)}`. Since `p > 1` and `v_p(x)` is a finite integer, `p^{-v_p(x)} > 0`. So `|x|_p > 0` for all non-zero `x`. ✓

**Axiom 2: Multiplicativity.** We must show `|xy|_p = |x|_p · |y|_p`.

- If `x = 0` or `y = 0`, both sides are `0`.
- If `x, y ≠ 0`, then `v_p(xy) = v_p(x) + v_p(y)` (logarithmic property of `v_p`). So:
  ```
  |xy|_p = p^{-v_p(xy)} = p^{-(v_p(x) + v_p(y))}
        = p^{-v_p(x)} · p^{-v_p(y)}
        = |x|_p · |y|_p. ✓
  ```

**Axiom 3: The Strong Triangle Inequality.** We must show `|x + y|_p ≤ max(|x|_p, |y|_p)`.

- If `x = 0` or `y = 0` or `x + y = 0`, it is trivial.
- Assume `x, y, x + y ≠ 0`. Then:
  ```
  |x + y|_p = p^{-v_p(x + y)}
            ≤ p^{-min(v_p(x), v_p(y))}    (since v_p(x+y) ≥ min(v_p(x), v_p(y)))
            = max(p^{-v_p(x)}, p^{-v_p(y)})   (negating flips min to max)
            = max(|x|_p, |y|_p). ✓
  ```

Wait — we need to be careful with the inequality direction. Since `v_p(x + y) ≥ min(v_p(x), v_p(y))`, the negation gives `-v_p(x + y) ≤ -min(v_p(x), v_p(y))`. And `-min(a, b) = max(-a, -b)`. The exponentiation `p^{(...)}` is monotonically increasing, so:
```
p^{-v_p(x+y)} ≤ p^{-min(v_p(x), v_p(y))} = p^{max(-v_p(x), -v_p(y))}
```
But `p^{max(A, B)} ≠ max(p^A, p^B)` in general. We need a more direct argument.

**Correct Proof of the Strong Triangle Inequality:**

Let `m = min(v_p(x), v_p(y))`. Without loss of generality, assume `m = v_p(x) ≤ v_p(y)`. Then:

- `|x|_p = p^{-v_p(x)} = p^{-m}`
- `|y|_p = p^{-v_p(y)} ≤ p^{-m} = |x|_p` (since `v_p(y) ≥ m`, so `-v_p(y) ≤ -m`)
- Thus `max(|x|_p, |y|_p) = |x|_p = p^{-m}`.

Now consider `x + y`. We have `x = p^m · x'` and `y = p^m · y'` where `x'` is an integer not divisible by `p` and `y'` is either not divisible by `p` or divisible by a higher power (if `v_p(y) > m`). Then:

```
x + y = p^m (x' + y')
```

The valuation is `v_p(x + y) = m + v_p(x' + y')`. Since `p ∤ x'`, the sum `x' + y'` may or may not be divisible by `p`. In any case, `v_p(x' + y') ≥ 0`. Therefore:

```
v_p(x + y) ≥ m
```

which gives:

```
|x + y|_p = p^{-v_p(x + y)} ≤ p^{-m} = |x|_p = max(|x|_p, |y|_p). ✓
```

The strong triangle inequality is proved. And because `max(|x|_p, |y|_p) ≤ |x|_p + |y|_p` (for non-negative quantities), the ordinary triangle inequality follows as a corollary. Thus `|·|_p` is indeed an absolute value — and a **non-Archimedean** one at that.

---

## 5.4 The p-Adic Metric

Since `|·|_p` is an absolute value, it induces a metric:

```
d_p(x, y) = |x − y|_p
```

for all `x, y ∈ ℚ`. Because `|·|_p` satisfies the strong triangle inequality, `d_p` is an **ultrametric**. Every theorem from Chapter 4 applies to the metric space `(ℚ, d_p)`:

- All triangles in `(ℚ, d_p)` are isosceles.
- Every point in a p-adic open ball is a center.
- Balls are either nested or disjoint.
- Balls are clopen (both open and closed).
- The space is totally disconnected — no continuous paths exist.

**What Does p-Adic "Closeness" Mean?** Two rational numbers are p-adically close if their difference is highly divisible by `p`. For example:

- `d₂(3, 7) = |4|_2 = |2²|_2 = 1/4`. So 3 and 7 are 2-adically close (distance 1/4).
- `d₂(3, 5) = |2|_2 = 1/2`. So 3 and 5 are slightly further apart 2-adically (distance 1/2).
- `d₂(3, 4) = |1|_2 = 1`. So 3 and 4 are 2-adically far apart (distance 1) — despite being numerically adjacent!
- `d₂(1000, 1008) = |8|_2 = 1/8`. So 1000 and 1008 are very close 2-adically — despite being numerically 8 units apart.

This is the "digital" nature of p-adic distance: it cares about the **lowest-order digits** in the base-`p` expansion, not the magnitude. Two numbers are close if they share many trailing digits in base `p`. This is analogous to how, in a computer, two floating-point numbers are "close" if they share many least significant bits — a connection that hints at the relevance of p-adic numbers to discrete computation.

---

## 5.5 The Mind-Bending Example: 1 + 2 + 4 + 8 + ... = −1

In real analysis, the geometric series `1 + 2 + 4 + 8 + 16 + ...` diverges to infinity. The terms grow without bound, and the partial sums `1, 3, 7, 15, 31, ...` also grow without bound. This series has no real sum.

But in the **2-adic** world, this series converges beautifully — and its sum is ... **−1**.

**Claim.** In the 2-adic metric on ℚ, the series `∑_{n=0}^{∞} 2^n` converges to `−1`.

**Proof.** Consider the partial sums:

```
S_0 = 1
S_1 = 1 + 2 = 3
S_2 = 1 + 2 + 4 = 7
S_3 = 1 + 2 + 4 + 8 = 15
S_4 = 1 + 2 + 4 + 8 + 16 = 31
...
S_n = 2^{n+1} − 1
```

(The formula `S_n = 2^{n+1} − 1` is easily proved by induction: `S_0 = 2^1 − 1 = 1`, and `S_{n+1} = S_n + 2^{n+1} = (2^{n+1} − 1) + 2^{n+1} = 2^{n+2} − 1`.)

Now compute the 2-adic distance from `S_n` to `−1`:

```
d₂(S_n, −1) = |S_n − (−1)|_2 = |S_n + 1|_2 = |2^{n+1}|_2 = 2^{-(n+1)}
```

This goes to 0 as `n → ∞`! In the 2-adic sense, `S_n` gets arbitrarily close to `−1`. By the definition of convergence (Chapter 3), the series converges to `−1`. ∎

**Why Does This Work?** In the 2-adic world, the number `−1` has the infinite base-2 expansion `...111111` (all 1's). Adding 1 gives `...000000 = 0` (with a carry that propagates infinitely to the left). The partial sums `S_n = 2^{n+1} − 1` correspond to truncating this infinite expansion after `n+1` digits — they are the "finite approximations" to `...111111`. As `n` grows, more and more trailing digits match `−1`, making the 2-adic distance shrink to zero.

This is NOT a trick. It is a rigorous consequence of the definition of 2-adic convergence. The series `1 + 2 + 4 + 8 + ...` truly sums to `−1` in ℚ₂. In fact, the same phenomenon occurs for any prime `p`:

```
∑_{n=0}^{∞} p^n = 1/(1 − p)   in ℚₚ
```

which gives `1/(1 − p)` as a p-adic integer. For `p = 2`, `1/(1 − 2) = −1`. For `p = 5`, the sum `1 + 5 + 25 + 125 + ...` converges to `1/(−4) = −1/4` in the 5-adic sense. This is the p-adic version of the geometric series formula, but with a crucial difference: in the real numbers, the formula `∑ r^n = 1/(1 − r)` works only for `|r| < 1`. In the p-adic numbers, it works for `|r|_p < 1` — which means `r` is a multiple of `p`, not that `r` is numerically small.

---

## 5.6 More p-Adic Convergence Examples

The p-adic metric reshapes our entire understanding of which sequences converge and which diverge.

**Example 1: Powers of p.** The sequence `(p^n)_{n=0}^∞` converges to 0 in ℚₚ because `|p^n|_p = p^{-n} → 0`. This is the opposite of the real case, where `p^n → ∞`. In a p-adic world, repeated multiplication by `p` makes numbers **smaller**.

**Example 2: Factorials.** The sequence `(n!)_{n=0}^∞` converges to 0 in every ℚₚ. For large `n`, `n!` contains many factors of `p`, so its p-adic absolute value goes to zero. In ℚ₂, for instance, `n!` is eventually divisible by arbitrarily high powers of 2, so `|n!|_2 → 0`. (In ℝ, `n! → ∞`.)

**Example 3: A Sequence That Converges in ℝ but Diverges in ℚₚ.** The sequence `(1/n)_{n=1}^∞` converges to 0 in ℝ. But in ℚₚ, it does NOT converge. For large `n` that are not divisible by `p`, `|1/n|_p = 1` (since `v_p(1/n) = 0`). The sequence oscillates between values with `|·|_p = 1` and values with `|·|_p = p^k` (when `n` contains `p` factors), so it does not approach any limit.

**Example 4: The Exponential Series.** The series `∑_{n=0}^{∞} x^n/n!` converges for all real `x` (defining `e^x`). In ℚₚ, this series converges only for `|x|_p < p^{-1/(p−1)}` — a much smaller region. The p-adic exponential has a finite radius of convergence, and its properties differ significantly from the real exponential. This has implications for p-adic quantum mechanics, where the time-evolution operator `e^{-iHt}` must be handled carefully.

---

## 5.7 Ostrowski's Theorem: The Only Absolute Values on ℚ

We have now seen two fundamentally different kinds of absolute values on ℚ: the standard Archimedean one `|·|_∞`, and the p-adic non-Archimedean ones `|·|_p` for each prime `p`. Are there any others?

**Ostrowski's Theorem (1916).** Every non-trivial absolute value on ℚ is equivalent to either:

1. The standard absolute value `|·|_∞` (the "Archimedean" case), or
2. A p-adic absolute value `|·|_p` for some prime `p` (the "non-Archimedean" case).

Two absolute values `|·|` and `|·|'` are **equivalent** if `|x|' = (|x|)^α` for some positive real constant `α`. Equivalent absolute values define the same topology and the same notion of convergence (though the specific distances are scaled).

**Intuition and Significance.** Ostrowski's Theorem is a classification result of extraordinary elegance. It says that the field ℚ of rational numbers admits exactly one Archimedean geometry (the familiar one) and a discrete infinity of non-Archimedean geometries (one for each prime). There are no other possibilities — no exotic hybrid geometries, no continuous families of intermediate geometries. The rational numbers are, in this sense, remarkably rigid: their possible "shapes" are completely determined by the primes.

**Why This Matters.** If physics is fundamentally described by a field of numbers — as quantum mechanics (built on ℂ) and general relativity (built on ℝ) suggest — then the choice of absolute value on that field determines the geometry of the physical world. Ostrowski's Theorem tells us that there are exactly two kinds of geometry available: continuous (Archimedean) and ultrametric (non-Archimedean), with the latter coming in one flavor per prime number.

Conventional physics has explored the Archimedean option exhaustively. The p-adic option — ultrametric physics — remains largely unexplored. This monograph is an investigation into that unexplored territory.

**A Proof Sketch.** (The full proof is in Appendix A.) The key idea: given an absolute value `|·|` on ℚ, consider its behavior on the integers. If `|n| > 1` for some integer `n > 1`, then the absolute value is Archimedean and equivalent to `|·|_∞`. If `|n| ≤ 1` for all integers `n`, then the absolute value is non-Archimedean, and the set `{n ∈ ℤ : |n| < 1}` is a prime ideal in ℤ, hence equal to `pℤ` for some prime `p`, making `|·|` equivalent to `|·|_p`.

---

## 5.8 Comparison Table: Archimedean vs. Non-Archimedean

Let us summarize the dramatic differences between the two kinds of geometry:

| Property | Archimedean (ℝ) | Non-Archimedean (ℚₚ) |
|:---------|:----------------|:---------------------|
| **Triangle inequality** | `\lvert x+y\rvert ≤ \lvert x\rvert + \lvert y\rvert` | `\lvert x+y\rvert ≤ \max(\lvert x\rvert, \lvert y\rvert)` |
| **Small + Small** | Can be medium (accumulation) | Never exceeds the larger (no accumulation) |
| **Triangles** | All three sides different (generically) | Always isosceles (two largest equal) |
| **Ball centers** | Unique | Every point in the ball is a center |
| **Ball intersections** | Can partially overlap | Nested or disjoint only |
| **Open balls** | Open but not closed | Both open AND closed (clopen) |
| **Connectedness** | Connected (one piece) | Totally disconnected (dust) |
| **Continuous paths** | Exist between any two points | Only constant paths exist |
| **Integers** | Unbounded (`\lvert n\rvert → ∞`) | Bounded (`\lvert n\rvert ≤ 1` for all integers) |
| **Powers of p** | Grow without bound (`p^n → ∞`) | Shrink to zero (`\lvert p^n\rvert = p^{-n} → 0`) |
| **Geometric series `∑ p^n`** | Diverges | Converges to `1/(1 − p)` |
| **Geometric model** | Continuous line, plane, sphere | Infinite tree (Bruhat-Tits) |
| **"Small" means...** | Numerically close to zero | Highly divisible by `p` |
| **"Close" means...** | Small numerical difference | Difference divisible by high power of `p` |

This table encapsulates the radical reorientation required to think in p-adic terms. Almost every intuition from everyday geometry must be inverted or abandoned. The reward for this effort is a geometry of remarkable rigidity and structure — a geometry that may be better suited than the continuous one for describing the discrete, hierarchical phenomena observed in quantum physics.

---

## 5.9 We Have Found a Second Way to Measure Size

In this chapter, we have constructed the **p-adic absolute value** `|·|_p` and verified that it satisfies all the axioms of an absolute value — including the strengthened, ultrametric form of the triangle inequality. We have seen how it inverts our ordinary intuition about size (highly divisible = small), how it generates a totally disconnected topology with clopen balls and no continuous paths, and how it causes infinite series that diverge hopelessly in ℝ to converge peacefully in ℚₚ.

We have also learned from Ostrowski's Theorem that the p-adic absolute values are not just one option among many — they are, together with the standard absolute value, the **only** absolute values on ℚ. The rational numbers have exactly two kinds of geometry: the familiar Archimedean one and the exotic non-Archimedean ones.

The stage is now set for the central construction of Part II: the completion of ℚ with respect to `|·|_p`. Just as ℝ is the completion of ℚ with respect to `|·|_∞`, we will construct ℚₚ — the field of **p-adic numbers** — as the completion of ℚ with respect to `|·|_p`. This field will inherit all the ultrametric properties we have explored, will be complete (every Cauchy sequence converges), and will serve as the foundation for a new kind of analysis, a new kind of physics, and a new kind of computation.

The journey from "what is a set?" is about to enter its most exciting phase.

---

*Next: Chapter 6 — Construction of the p-Adic Numbers — where we build ℚₚ from Cauchy sequences, prove it is a complete field, and explore its rich arithmetic and topological structure. (Forthcoming)*
