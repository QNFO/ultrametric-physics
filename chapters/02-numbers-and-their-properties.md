# Chapter 2: Numbers and Their Properties

*In which we journey through the landscape of numbers — from counting to fractions — and learn that every number carries a hidden "prime fingerprint" that will unlock a radical new way of measuring distance.*

---

## 2.1 Natural Numbers: The Ur-Numbers

The first numbers humanity ever used were the **natural numbers**: 1, 2, 3, 4, 5, ... These are the counting numbers, the numbers that answer the question "How many?" How many sheep in the flock? How many days until the full moon? How many children in the family?

We denote the set of natural numbers by ℕ:

```
ℕ = {1, 2, 3, 4, 5, ...}
```

(Some definitions include 0 in ℕ. We will use ℕ = {1, 2, 3, ...} for now, and introduce 0 with the integers.)

The natural numbers come equipped with two fundamental operations: **addition** and **multiplication**. If you have a flock of 3 sheep and you acquire 2 more, you have 3 + 2 = 5 sheep. If you have 3 rows of crops with 4 plants in each row, you have 3 × 4 = 12 plants. These operations feel inevitable, grounded in physical acts of combining and arranging.

But the natural numbers have a limitation: subtraction is not always possible. You cannot take 5 sheep from a flock of 3 and end up with a natural number of sheep. The equation `3 - 5 = ?` has no answer in ℕ. To solve it, we must expand our number system.

The natural numbers also have a deep internal structure revealed by multiplication. Some natural numbers can be "broken down" into smaller factors: 12 = 3 × 4 = 2 × 2 × 3. Others cannot be broken down at all: 2, 3, 5, 7, 11, 13, ... These indecomposable numbers are the **prime numbers** — the atoms of multiplication. Every natural number greater than 1 is either prime or can be expressed as a unique product of primes. But we are getting ahead of ourselves. First, let us complete our number system to allow subtraction.

---

## 2.2 Integers: Debt, Credit, and Symmetry

To make subtraction always possible, we introduce **negative numbers**. The integer `−3` represents a deficit — owing 3 sheep rather than owning them. The set of **integers**, denoted ℤ (from the German *Zahlen*, meaning "numbers"), is:

```
ℤ = {..., -3, -2, -1, 0, 1, 2, 3, ...}
```

The integer 0 represents the absence of quantity — neither credit nor debt, the neutral element. With integers, every subtraction problem has a solution: `3 − 5 = −2`, `a − b` is always an integer for any integers `a` and `b`.

The integers form an **abelian group** under addition, as we discussed in Chapter 1. Every integer `a` has an additive inverse `−a` such that `a + (−a) = 0`. This symmetry — the pairing of every number with its negation — is a profound structural feature. It means that the integers are "balanced" around zero. For every transaction that increases a quantity, there is a transaction that decreases it.

The integers also support multiplication, making them a **ring**: you can add, subtract, and multiply integers and always get an integer. But division is still problematic. The equation `3 × x = 7` has no integer solution — there is no integer `x` whose product with 3 gives 7. To handle division, we must expand our number system once more.

**Physical Intuition.** Think of the integers as positions on an infinite ruler, with zero at the center, positive numbers extending to the right, negative numbers to the left. The gaps between integers are empty — there are no positions like "one and a half." In physics, integer-valued quantities appear frequently: the number of particles, the quantized charge (in units of the electron charge), the winding number of a field configuration. The integers capture discrete, countable aspects of reality.

---

## 2.3 Rational Numbers: Sharing and Dividing

To allow division (except by zero), we introduce **fractions**. A **rational number** is any number that can be expressed as the ratio of two integers:

```
ℚ = {a/b : a, b ∈ ℤ, b ≠ 0}
```

(The symbol ℚ stands for "quotient.")

The rationals include the integers (since any integer `n` can be written as `n/1`) and fill in all the gaps between them. There are rational numbers everywhere: between any two distinct rationals, there is another rational. For example, between 0 and 1 lies 1/2; between 0 and 1/2 lies 1/4; between 0 and 1/4 lies 1/8; and so on infinitely. This property is called **density**. The rationals are dense in themselves — they have no "next" rational number.

Despite this density, we will discover that the rationals still have "holes" — numbers that *should* exist but cannot be expressed as fractions. √2 is the most famous example. But before we confront the incompleteness of ℚ, let us appreciate what it can do.

**The Rationals as a Field.** The rational numbers, with addition and multiplication, form a **field**. This means:

1. `(ℚ, +)` is an abelian group: you can add any two rationals and get a rational, addition is associative and commutative, 0 is the identity, and every rational `a/b` has an additive inverse `−a/b`.

2. `(ℚ \ {0}, ·)` is an abelian group: you can multiply any two non-zero rationals and get a non-zero rational, multiplication is associative and commutative, 1 is the identity, and every non-zero rational `a/b` has a multiplicative inverse `b/a`.

3. Multiplication distributes over addition: `p · (q + r) = p·q + p·r`.

The fact that every non-zero rational has a reciprocal is what makes ℚ a field. This is the property that ℤ lacks, and it is why ℚ is the natural setting for equations involving division.

**Physical Intuition.** Rational numbers model any quantity that can be measured in units and subdivisions of units. If your ruler is marked in millimeters, any measurement you make is a rational multiple of the millimeter. In classical physics, all measured quantities were assumed to be rational (or, more precisely, real numbers approximated by rationals). In quantum mechanics, however, certain quantities — the energy levels of a bound electron, the spin of a particle — are constrained to discrete (integer or half-integer) values. The tension between continuous (rational/real) and discrete (integer) descriptions is a recurring theme in physics, and it will become central when we encounter p-adic numbers, which are the ultimate discrete-but-complete number system.

---

## 2.4 The Standard Absolute Value: How Far from Zero?

Before we can talk about distance, we must first talk about **size**. How "big" is a number? The most familiar notion is the distance from zero on the number line. We call this the **absolute value** (or **standard absolute value**) and denote it `|x|`. For a real number `x`:

```
|x| = { x  if x ≥ 0
      { -x if x < 0
```

For rational numbers, the absolute value is defined the same way: `|a/b|` is the non-negative rational representing the distance of `a/b` from zero. For example, `|3/4| = 3/4`, `|−7/2| = 7/2`, `|0| = 0`.

The absolute value on ℚ satisfies three fundamental properties that make it what mathematicians call an **absolute value** (or **norm**, or **valuation**):

1. **Positive Definiteness:** `|x| ≥ 0` for all `x`, and `|x| = 0` if and only if `x = 0`. Distance from zero is never negative, and only zero is at zero distance from itself.

2. **Multiplicativity:** `|x · y| = |x| · |y|` for all `x, y`. The size of a product is the product of the sizes. `|2 · (−3)| = |−6| = 6 = |2| · |−3| = 2 · 3 = 6`. ✓

3. **Triangle Inequality:** `|x + y| ≤ |x| + |y|` for all `x, y`. The size of a sum is never more than the sum of the sizes. In geometric terms: the direct distance `|x + y|` is never longer than going from 0 to `x` and then from `x` to `x + y` (which has length `|y|`). `|3 + 4| = 7 ≤ 3 + 4 = 7`. `|3 + (−4)| = |−1| = 1 ≤ 3 + 4 = 7`.

These three properties are the axioms that define an absolute value on any field. They capture our deepest intuitions about what "size" means, and any function on a field that satisfies them deserves to be called an absolute value.

The triangle inequality, in particular, encodes the familiar geometry of the number line. It says that the shortest path between two points is a straight line — there are no shortcuts. This is the **Archimedean** property in its geometric form, and it seems so obvious that it is hard to imagine any alternative. But as we will see in Chapters 4 and 5, there exists a different kind of absolute value — the **p-adic absolute value** — that satisfies properties 1 and 2, but replaces the triangle inequality with a stronger condition that produces a radically different geometry.

---

## 2.5 The Fundamental Theorem of Arithmetic: The Prime Fingerprint

Every natural number greater than 1 has a unique "identity" expressed in terms of primes. This is the **Fundamental Theorem of Arithmetic**, one of the most important and beautiful theorems in all of mathematics.

**Theorem (Fundamental Theorem of Arithmetic).** Every integer `n > 1` can be expressed as a product of prime numbers, and this expression is unique except for the order of the factors.

For example:

```
60 = 2 × 2 × 3 × 5 = 2² · 3¹ · 5¹
84 = 2 × 2 × 3 × 7 = 2² · 3¹ · 7¹
```

There is no other way to factor 60 or 84 into primes. The prime factorization is like the **DNA** of a number — it uniquely identifies that number among all integers. Two numbers are equal if and only if they have exactly the same prime factorization.

This theorem extends to rational numbers as well. Any non-zero rational number can be uniquely expressed as:

```
x = ± p₁^e₁ · p₂^e₂ · ... · p_k^e_k
```

where the `p_i` are distinct primes and the `e_i` are integers (which may now be negative). For example:

```
3/4 = 3¹ · 2⁻² = 2⁻² · 3¹
12/5 = 2² · 3¹ · 5⁻¹
```

The exponents in this factorization are the complete description of the number's multiplicative structure. Two non-zero rationals are equal if and only if they have the same sign and the same exponents for every prime.

**Why This Matters.** The Fundamental Theorem tells us that the set of prime numbers is the complete "alphabet" for multiplication. Any multiplicative question about integers or rationals can be reduced to questions about the exponents in their prime factorizations. This insight will be crucial when we define the p-adic valuation: we will isolate a single prime `p` and ask, "How many times does `p` divide this number?" The answer — the exponent of `p` in the prime factorization — will become our new measure of size.

---

## 2.6 The p-Adic Valuation: Measuring Divisibility

Choose a prime number `p`. For any non-zero rational number `x`, we can ask: "What is the highest power of `p` that divides `x`?" More precisely, we want the exponent of `p` in the prime factorization of `x`.

**Definition (p-Adic Valuation).** For a non-zero rational number `x`, write `x` in its unique prime factorization as `x = p^k · (a/b)`, where `a` and `b` are integers not divisible by `p`. Then the **p-adic valuation** of `x` is:

```
v_p(x) = k
```

In words: `v_p(x)` is the exponent of `p` in the prime factorization of `x`. It tells us how many times `p` divides `x` (if `k > 0`), or how many times `p` divides the denominator (if `k < 0`). For completeness, we define `v_p(0) = ∞` (zero is divisible by `p` infinitely many times).

Let us work through specific examples with `p = 2` (the 2-adic valuation):

**Example 1: v₂(8) = 3.**
```
8 = 2³
The exponent of 2 is 3, so v₂(8) = 3.
```
Interpretation: 8 is divisible by 2 three times (8 → 4 → 2 → 1).

**Example 2: v₂(12) = 2.**
```
12 = 2² · 3
The exponent of 2 is 2, so v₂(12) = 2.
```
Interpretation: 12 is divisible by 2 twice (12 → 6 → 3). The remaining factor 3 is odd.

**Example 3: v₂(3/4) = −2.**
```
3/4 = 3 · 2⁻²
The exponent of 2 is −2, so v₂(3/4) = −2.
```
Interpretation: 4 is in the denominator. 4 = 2², so the denominator is divisible by 2 twice. Since the 2's are in the denominator, the exponent is negative.

**Example 4: v₂(7) = 0.**
```
7 is not divisible by 2 at all. Its prime factorization contains no factor 2.
So v₂(7) = 0.
```

**Example 5: v₅(250) = 3.**
```
250 = 2 · 5³
v₅(250) = 3.
```

**Example 6: v₃(1/9) = −2.**
```
1/9 = 3⁻²
v₃(1/9) = −2.
```

**Example 7: v₇(10) = 0.**
```
10 = 2 · 5. No factor of 7 appears.
v₇(10) = 0.
```

The p-adic valuation has a beautiful set of properties:

1. **Logarithmic Property:** `v_p(x · y) = v_p(x) + v_p(y)`. Proof: When you multiply two numbers, the exponents of `p` in their factorizations add. `v₂(8 · 12) = v₂(96) = 5` (since 96 = 2⁵ · 3), and indeed `v₂(8) + v₂(12) = 3 + 2 = 5`. ✓

2. **Ultrametric Addition Rule:** `v_p(x + y) ≥ min(v_p(x), v_p(y))`. The valuation of a sum is at least the smaller of the two valuations. In fact, if `v_p(x) ≠ v_p(y)`, then equality holds: `v_p(x + y) = min(v_p(x), v_p(y))`. If the valuations are equal, the valuation of the sum may be larger.

Let us verify this second property with examples:

- `v₂(8 + 4) = v₂(12) = 2`. Here `v₂(8) = 3`, `v₂(4) = 2`. The minimum is 2. The sum has valuation 2. ✓
- `v₂(8 + 8) = v₂(16) = 4`. Here both have valuation 3. The sum's valuation (4) is *larger* than the minimum (3). This is the "carry" effect: adding two even numbers can produce a number divisible by an even higher power of 2.
- `v₂(3 + 5) = v₂(8) = 3`. Here `v₂(3) = 0`, `v₂(5) = 0`. The minimum is 0. The sum has valuation 3 > 0. Adding two odd numbers gives an even number — sometimes a very even number!

This ultrametric addition rule is the key to everything that follows. It says that when you add two numbers, the sum cannot have *less* divisibility by `p` than the *more divisible* of the two summands. Divisibility by `p` is "contagious upward" but never "decays downward." This property, when translated into a distance function, will produce the ultrametric inequality that defines the p-adic geometry.

---

## 2.7 Prime Factorization as the DNA of Numbers

Let us pause to appreciate the extraordinary power of the prime factorization perspective. Every rational number carries a **complete prime signature** — an infinite list of integers, one for each prime, giving that prime's exponent in the factorization:

```
x = ∏_{p prime} p^{v_p(x)}
```

For example:

- The number `12` has the signature: v₂ = 2, v₃ = 1, all other v_p = 0.
- The number `1/6` has the signature: v₂ = −1, v₃ = −1, all other v_p = 0.
- The number `1` has all-zero signature: v_p = 0 for every prime `p`.

This representation is **complete**: you can reconstruct the number (up to sign) from its prime exponents. It is **unique**: no two different rational numbers have the same prime signature. And it is **local**: each prime `p` contributes independently to the structure of the number.

The "local" nature of prime factorization is a deep insight. To understand the number 12 fully, you need to know about all its prime factors. But much of the behavior of 12 *with respect to the prime 2* can be understood just by looking at v₂(12) = 2 — the fact that 12 is divisible by 4 but not by 8. Similarly, its behavior with respect to 3 is governed by v₃(12) = 1. The different primes operate independently, like independent "channels" of information about the number.

This local-global principle — the idea that the properties of a number can be understood by analyzing it "one prime at a time" and then combining the results — is a central theme in modern number theory. It is the motivation behind the construction of the p-adic numbers: we complete the rationals "at each prime p" to get a local field ℚₚ that captures all the p-adic information, and the original rationals can be recovered (in a suitable sense) from the collection of all these local completions together with the real numbers.

**Physical Analogy.** Think of a number as a particle, and the primes as different detectors. Each detector measures one "charge" of the particle — how it couples to that particular prime. The real absolute value `|·|` is the "Archimedean detector" that measures the particle's overall magnitude. The p-adic valuation `v_p` is a "non-Archimedean detector" that measures the particle's p-divisibility. Just as a complete description of an elementary particle requires specifying all its charges (electric, weak, strong), a complete description of a rational number requires specifying its real absolute value AND all its p-adic valuations. This analogy is more than poetic — it points toward a deep structural unity between number theory and physics that we will explore throughout this monograph.

---

## 2.8 What If We Measured Size Differently?

We have now seen two different ways to extract information about a rational number:

1. The **standard absolute value** `|x|`, which measures how far `x` is from zero on the familiar number line. It satisfies positive definiteness, multiplicativity, and the triangle inequality.

2. The **p-adic valuation** `v_p(x)`, which measures how divisible `x` is by the prime `p`. It satisfies `v_p(xy) = v_p(x) + v_p(y)` and `v_p(x + y) ≥ min(v_p(x), v_p(y))`.

These two ways of looking at numbers seem fundamentally different — one is about magnitude, the other about divisibility. But they share a common algebraic structure. And here is the crucial observation:

**We can turn the p-adic valuation into an absolute value.** Define:

```
|x|_p = p^{-v_p(x)}
```

for `x ≠ 0`, and `|0|_p = 0`.

Let us compute some examples with `p = 2`:

- `|8|_2 = 2^{-3} = 1/8`
- `|12|_2 = 2^{-2} = 1/4`
- `|3/4|_2 = 2^{-(−2)} = 2^2 = 4`
- `|7|_2 = 2^{-0} = 1`

This definition inverts our intuition: numbers that are highly divisible by `p` become **small** in the p-adic sense. The number 8, which is large in the usual sense (|8| = 8), is tiny in the 2-adic sense (|8|₂ = 1/8). The number 1024 = 2¹⁰ is enormous in the usual sense but vanishingly small in the 2-adic sense: |1024|₂ = 2⁻¹⁰ = 1/1024. Meanwhile, numbers that are not divisible by 2 at all — like 7, 11, or any odd number — have the same modest 2-adic size: |odd|₂ = 1.

This inversion is not a bug; it is the feature that makes p-adic numbers interesting. By measuring "size" as "closeness in terms of divisibility by p," we obtain a geometry in which powers of p are "small" and numbers that are "close" share many factors of p. Two integers are p-adically close if their difference is highly divisible by p. For example:

- `3` and `7` are 2-adically close because `7 − 3 = 4 = 2²`, so `|7 − 3|_2 = 1/4` (small).
- `3` and `4` are 2-adically far apart because `4 − 3 = 1`, so `|4 − 3|_2 = 1` (not small).
- `1000000` and `1000008` are 2-adically close because their difference is 8 = 2³, so `|8|_2 = 1/8`.

The p-adic absolute value satisfies positive definiteness and multiplicativity (as you will verify in the exercises). Most importantly, it satisfies a **strengthened** version of the triangle inequality — the **strong triangle inequality** or **ultrametric inequality**:

```
|x + y|_p ≤ max(|x|_p, |y|_p)
```

This is much stronger than the ordinary triangle inequality `|x + y| ≤ |x| + |y|`. The sum of two p-adic numbers is never larger (in the p-adic sense) than the larger of the two summands. This property, which follows directly from the ultrametric addition rule for `v_p`, will have profound geometric consequences.

We have now glimpsed the existence of an alternative way to measure size, one that is perfectly consistent mathematically but radically different from our everyday intuition. The natural next question is: can we construct a complete number system using this new absolute value, just as we construct the real numbers ℝ by completing ℚ with respect to the standard absolute value? The answer is yes — and the result is the field of **p-adic numbers** ℚₚ.

But before we can construct ℚₚ, we must understand the general theory of distance and metric spaces — the framework within which "completeness" makes sense. That is the subject of the next chapter.

---

*Next: [Chapter 3: Distance and Metric Spaces](03-distance-and-metric-spaces.md) — where we formalize the concept of distance, explore the strange world of open and closed sets, and learn what it means for a space to be "complete" — and why ℚ is not.*
