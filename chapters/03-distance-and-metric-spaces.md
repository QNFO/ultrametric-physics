# Chapter 3: Distance and Metric Spaces

*In which we formalize what "distance" means, explore the strange topology of metric spaces, and discover that the rational numbers — for all their density — are riddled with invisible holes, awaiting completion.*

---

## 3.1 What Is Distance? Three Intuitions

Before we write down a formal definition, let us reflect on what "distance" means to us. Imagine two cities on a map. What do we mean when we say "City A is 100 kilometers from City B"?

**Intuition 1: Zero only when identical.** The distance from a place to itself is zero — you are already there. And if the distance between two places is zero, they must be the same place. There is no "infinitesimal separation"; two distinct points are always at some positive distance from each other.

**Intuition 2: Symmetry.** The distance from City A to City B is the same as the distance from City B to City A. The road goes both ways, and the odometer reading does not depend on direction. Distance does not have a "sign" — it is never negative, and it does not care about which point you start from.

**Intuition 3: The shortest path (triangle inequality).** If you travel from City A to City C via City B, the total distance traveled is the sum: `distance(A, B) + distance(B, C)`. The direct distance from A to C can never be longer than this sum — there might be a shortcut, a more direct route, but you cannot make the journey *longer* by going directly. Going straight is always at least as short as going through an intermediate point:

```
distance(A, C) ≤ distance(A, B) + distance(B, C)
```

These three intuitions seem so obvious that it is hard to imagine them failing. But as we will see, the third one — the triangle inequality — can be replaced by a stronger condition that produces an entirely different geometry. For now, however, these three properties are the foundation upon which the theory of metric spaces is built.

---

## 3.2 The Formal Definition of a Metric

A **metric space** is a set `X` together with a function `d : X × X → ℝ` (called the **metric** or **distance function**) that assigns a non-negative real number to every pair of points, satisfying the following three axioms for all `x, y, z ∈ X`:

**(M1) Positive Definiteness:** `d(x, y) ≥ 0`, and `d(x, y) = 0` if and only if `x = y`.

**(M2) Symmetry:** `d(x, y) = d(y, x)`.

**(M3) Triangle Inequality:** `d(x, z) ≤ d(x, y) + d(y, z)`.

These axioms correspond precisely to our three intuitions. Let us verify them against familiar examples.

**Example 1: Euclidean Metric on the Real Line.** Let `X = ℝ`, and define `d(x, y) = |x − y|`. This is the absolute difference — the length of the straight line segment connecting `x` and `y`.

- M1: `|x − y| ≥ 0`, and `|x − y| = 0` iff `x = y`. ✓
- M2: `|x − y| = |y − x|`. ✓
- M3: `|x − z| = |(x − y) + (y − z)| ≤ |x − y| + |y − z|` (by the triangle inequality for absolute value). This is why it is called the "triangle inequality" — it mirrors the geometric fact that any side of a triangle is shorter than the sum of the other two sides. ✓

**Example 2: Euclidean Metric on the Plane.** Let `X = ℝ²`, the set of points in the plane. For two points `P₁ = (x₁, y₁)` and `P₂ = (x₂, y₂)`, define:

```
d(P₁, P₂) = √[(x₂ − x₁)² + (y₂ − y₁)²]
```

This is the Pythagorean theorem — the straight-line distance in the plane. It satisfies all three axioms (the triangle inequality takes some work to prove — it follows from the Cauchy-Schwarz inequality). This is the metric you learned in school, the one that describes the geometry of flat tables, maps, and the pages of this book.

**Example 3: Discrete Metric.** Let `X` be any set. Define:

```
d(x, y) = { 0  if x = y
           { 1  if x ≠ y
```

This is the **discrete metric**. Every point is distance 1 from every other point. It satisfies M1 (zero only for identical points), M2 (clearly symmetric), and M3 (if `x = z`, then `d(x, z) = 0 ≤ d(x, y) + d(y, z)` automatically; if `x ≠ z`, then at least one of `x ≠ y` or `y ≠ z` must hold, so the right side is at least 1, and the inequality holds). The discrete metric models a world where all distinctions are equally significant — there are no degrees of closeness, only "same" and "different."

**Example 4: The Metric Induced by an Absolute Value.** If `F` is a field with an absolute value `|·|` (as defined in Chapter 2), then `d(x, y) = |x − y|` defines a metric on `F`. The three metric axioms follow directly from the three absolute value axioms. This is how we will construct metrics on ℚ, ℝ, ℂ, and — crucially — ℚₚ.

---

## 3.3 Open Balls: The Neighborhood of a Point

In a metric space, the fundamental geometric object is the **open ball**. It generalizes the notion of a "neighborhood" — all the points within a certain radius of a center.

**Definition (Open Ball).** Let `(X, d)` be a metric space, `x ∈ X` a point, and `r > 0` a positive real number. The **open ball** of radius `r` centered at `x` is:

```
B(x, r) = {y ∈ X : d(x, y) < r}
```

The "open" means we use strict inequality (`<`, not `≤`). The boundary of the ball (points at exactly distance `r`) is not included.

**Examples:**

1. **On the real line with the Euclidean metric:** `B(0, 1) = (−1, 1)`, the open interval from −1 to 1. All real numbers whose distance from 0 is strictly less than 1.

2. **On the plane with the Euclidean metric:** `B((0, 0), 1)` is the open unit disk — all points less than 1 unit from the origin. It is the interior of a circle, not including the circle itself.

3. **With the discrete metric:** `B(x, 0.5) = {x}` (only the center itself, since any other point is at distance 1 > 0.5). `B(x, 2) = X` (the entire set, since every other point is at distance 1 < 2). The discrete metric produces a very simple ball structure.

Open balls are the building blocks of **topology** — the mathematical study of "nearness," "continuity," and "connectedness" without reference to specific distances. The collection of all open balls in a metric space generates a **topology**, which gives meaning to words like "open set," "closed set," "convergent sequence," and "continuous function." We now explore these concepts.

---

## 3.4 Open Sets and the Meaning of "Nearby"

In the everyday world, we say two things are "nearby" if the distance between them is small. But in mathematics, we need a more precise — and more flexible — concept.

**Definition (Open Set).** A subset `U ⊆ X` of a metric space is called **open** if, for every point `x ∈ U`, there exists some positive radius `r > 0` such that the entire open ball `B(x, r)` is contained within `U`.

In words: an open set is one where every point has a little "breathing room" around it that stays inside the set. You can wiggle any point a little bit without leaving the set.

**Examples:**

- The interval `(0, 1)` is open in ℝ: for any point `x` in the interval, you can pick a radius small enough (e.g., `r = min(x, 1−x)/2`) so that the ball `(x−r, x+r)` stays within `(0, 1)`.
- The interval `[0, 1]` is NOT open: the point `0` is in the set, but any ball around `0` with any positive radius will include some negative numbers, which are not in `[0, 1]`.
- The whole space `X` is always open (trivially).
- The empty set `∅` is always open (vacuously — there are no points to check).

Open sets satisfy three key properties:

1. The whole space and the empty set are open.
2. The union of any collection of open sets is open.
3. The intersection of any *finite* collection of open sets is open.

These three properties are the axioms of a **topology**. A set equipped with a collection of subsets satisfying these axioms is called a **topological space**. Every metric space is a topological space (the open sets are those defined above), but not every topological space comes from a metric. Metric spaces have extra structure — distances — that pure topological spaces lack.

**Definition (Closed Set).** A subset `C ⊆ X` is called **closed** if its complement `X \ C` is open. Intuitively, a closed set contains all its "boundary points" — there is no way to "escape" the set by taking a limit.

Examples: `[0, 1]` is closed in ℝ; `(0, 1)` is not closed. The sets `∅` and `X` are both open AND closed in any metric space. (In a connected space like ℝ, these are the only such sets. But in ultrametric spaces, we will encounter many clopen — simultaneously closed and open — sets, a hallmark of total disconnectedness.)

---

## 3.5 Sequences and Convergence: Getting Arbitrarily Close

A **sequence** in a metric space `(X, d)` is an infinite ordered list of points: `(x₁, x₂, x₃, ...)`, which we write as `(x_n)_{n=1}^∞`. We want to say when such a sequence "approaches" a limit point.

**Definition (Convergence).** A sequence `(x_n)` **converges** to a point `L ∈ X` (written `x_n → L` or `lim_{n→∞} x_n = L`) if:

> For every `ε > 0` (no matter how small), there exists an integer `N` such that for all `n ≥ N`, we have `d(x_n, L) < ε`.

In words: The terms of the sequence eventually get — and stay — arbitrarily close to `L`. After some finite number of terms, all subsequent terms are within distance `ε` of the limit. The smaller the `ε`, the larger the `N` you may need, but some `N` must always exist.

**Example on ℝ:** The sequence `(1/n)_{n=1}^∞` = `(1, 1/2, 1/3, 1/4, ...)` converges to 0. Given any `ε > 0`, choose `N > 1/ε`. Then for all `n ≥ N`, we have `|1/n − 0| = 1/n ≤ 1/N < ε`. ✓

**Example on ℚ:** The sequence `(0.3, 0.33, 0.333, 0.3333, ...)` of rational numbers gets arbitrarily close to `1/3` (which is also rational), so it converges in ℚ.

**Non-Example:** The sequence `(1, 2, 3, 4, ...)` does not converge in ℝ — it grows without bound. No real number can serve as its limit.

**Key Point:** Convergence depends on the metric. A sequence that converges in one metric may diverge in another. We will see dramatic examples of this when we compare the standard metric on ℚ with the p-adic metric.

---

## 3.6 Cauchy Sequences: Terms Getting Close to Each Other

A sequence can "want" to converge even if the limit is not in the space. To capture this idea, we introduce Cauchy sequences, named after the French mathematician Augustin-Louis Cauchy.

**Definition (Cauchy Sequence).** A sequence `(x_n)` in a metric space is called a **Cauchy sequence** if:

> For every `ε > 0`, there exists an integer `N` such that for all `m, n ≥ N`, we have `d(x_m, x_n) < ε`.

In words: The terms of the sequence eventually get arbitrarily close **to each other** — not necessarily to any particular limit point in the space. After some finite index, all terms are bunched together within distance `ε`.

**Example:** The sequence `(1/n)` in ℝ is Cauchy: for `m, n ≥ N`, we have `|1/m − 1/n| ≤ 1/m + 1/n ≤ 2/N < ε` for sufficiently large `N`.

**Relationship Between Convergence and Cauchy:**

> **Theorem.** Every convergent sequence is Cauchy.

*Proof.* If `x_n → L`, then for large `n`, each term is close to `L`. By the triangle inequality, any two such terms are close to each other: `d(x_m, x_n) ≤ d(x_m, L) + d(L, x_n) < ε/2 + ε/2 = ε`. ∎

The converse — "every Cauchy sequence converges" — is NOT true in general. It depends on the space. This brings us to the crucial concept of completeness.

---

## 3.7 Complete Spaces: No "Holes"

A metric space is **complete** if every Cauchy sequence in the space converges to a point within the space. Completeness means there are no "missing" limit points — no "holes" where a sequence seems to be heading but finds nothing there.

**Example: ℝ is complete.** This is a fundamental theorem of real analysis. Every Cauchy sequence of real numbers converges to a real number. The real line has no holes.

**Example: ℚ is NOT complete.** This is a shock if you have never thought about it. The rational numbers are dense — between any two rationals there is another rational — and yet they are incomplete. How can this be?

Consider the sequence of rational numbers defined by the Newton-Raphson method for approximating √2:

```
x₁ = 1
x₂ = 1.5
x₃ = 1.41666...
x₄ = 1.414215...
x₅ = 1.414213562...
```

This sequence gets closer and closer to √2. It is a Cauchy sequence in ℚ (the terms get arbitrarily close to each other). But its limit — √2 — is NOT a rational number. (The proof that √2 is irrational is one of the gems of Greek mathematics: if √2 = a/b in lowest terms, then 2b² = a², so a is even, so b is even, contradiction.) The sequence "wants" to converge, but the target is missing — there is a hole at √2.

More generally, there are infinitely many holes in ℚ — at every irrational number (√2, π, e, √3, the golden ratio φ, ...) and more. ℚ is like a sieve: it catches all the rational points but lets uncountably many limit points slip through.

The remedy is **completion**: we add all the missing limit points to create a complete space.

---

## 3.8 Completion: Filling the Holes

Given any metric space `(X, d)` that is not complete, there is a standard construction that produces a complete metric space `(X̂, d̂)` — the **completion** of `X` — such that:

1. `X` is isometrically embedded in `X̂` (i.e., `X` "sits inside" `X̂` as a dense subset).
2. `X̂` is complete.
3. `X̂` is essentially unique (any two completions are isometric).

The idea: take all Cauchy sequences in `X`. Two Cauchy sequences are considered "equivalent" if the distance between their corresponding terms goes to zero. Each equivalence class represents a "missing limit point." The completion `X̂` is the set of all such equivalence classes, with a naturally defined metric. The original space `X` is identified with the set of equivalence classes of constant sequences.

**ℝ as the Completion of ℚ.** The real numbers ℝ are precisely the completion of ℚ with respect to the standard absolute value metric `d(x, y) = |x − y|`. Every real number is the limit of some Cauchy sequence of rationals (think of the decimal expansion: `π = lim(3, 3.1, 3.14, 3.141, 3.1415, ...)`). The real numbers fill all the holes in ℚ, producing a complete, connected, Archimedean field.

**This Construction Depends on the Metric!** Here is the crucial observation that drives everything that follows. The completion of ℚ depends on which metric we use. If we use the standard metric, we get ℝ. But what if we use a different metric? In particular, what if we use the **p-adic metric** `d_p(x, y) = |x − y|_p`?

The completion of ℚ with respect to `d_p` is a different field — the field of **p-adic numbers** ℚₚ. It is complete (with respect to the p-adic metric), it is a field (operations extend continuously from ℚ), and it has a radically different topology. For each prime `p`, we get a different p-adic field — `ℚ₂, ℚ₃, ℚ₅, ℚ₇, ...` — all completions of the same rational numbers, but with different geometries. And for `p = ∞` (a conventional notation), we get the real numbers ℝ.

This is the **local-global principle** made concrete: to understand a rational number completely, you need to know its behavior in ℝ AND in all the ℚₚ. The reals tell you about magnitude; the p-adics tell you about divisibility.

---

## 3.9 The Metric Induced by an Absolute Value

Before we move on to ultrametricity, let us solidify the connection between absolute values on fields and metrics.

**Theorem.** If `|·|` is an absolute value on a field `F` (satisfying the three axioms from Chapter 2: positive definiteness, multiplicativity, triangle inequality), then `d(x, y) = |x − y|` defines a metric on `F`.

*Proof.*
- M1 (Positive Definiteness): `d(x, y) = |x − y| ≥ 0` by the positive definiteness of `|·|`. And `d(x, y) = 0` iff `|x − y| = 0` iff `x − y = 0` iff `x = y`. ✓
- M2 (Symmetry): We need `|x − y| = |y − x|`. This follows from multiplicativity: `|−1|² = |(−1)²| = |1| = 1`, so `|−1| = 1` (since absolute values are non-negative). Then `|y − x| = |(−1)(x − y)| = |−1| · |x − y| = |x − y|`. ✓
- M3 (Triangle Inequality): `d(x, z) = |x − z| = |(x − y) + (y − z)| ≤ |x − y| + |y − z| = d(x, y) + d(y, z)`. ✓

Thus every absolute value gives rise to a metric. The properties of the metric space `(F, d)` are determined by the properties of the absolute value. In particular:

- If the absolute value satisfies the ordinary triangle inequality `|x + y| ≤ |x| + |y|`, the resulting metric is **Archimedean**. This is the familiar geometry of ℝ and ℂ.

- If the absolute value satisfies the **strong** triangle inequality `|x + y| ≤ max(|x|, |y|)`, the resulting metric is **non-Archimedean** or **ultrametric**. This is the geometry of the p-adic fields — a geometry where all triangles are isosceles, every point in a ball is a center, and balls cannot partially overlap.

The next chapter is devoted entirely to exploring the strange and wonderful properties of ultrametric spaces. Prepare to have your geometric intuitions systematically overturned.

---

## 3.10 But This Is Not the Only Way to Complete ℚ...

Let us end this chapter by planting a seed of wonder. We have seen that ℚ can be completed to ℝ by adding limits of Cauchy sequences with respect to the standard absolute value. We have hinted that there are other absolute values on ℚ — the p-adic absolute values — and that completing ℚ with respect to them yields other fields ℚₚ.

But this raises a profound question: are there ANY OTHER absolute values on ℚ besides the standard one and the p-adic ones? The answer, given by **Ostrowski's Theorem** (which we will state precisely in Chapter 5), is **no**. Up to a natural notion of equivalence, every non-trivial absolute value on ℚ is either:

1. The standard absolute value `|·|_∞` (the "Archimedean" one), or
2. A p-adic absolute value `|·|_p` for some prime `p` (the "non-Archimedean" ones).

This is a stunning result. It says that the field of rational numbers — the most basic infinite field — admits exactly two kinds of "geometry": the familiar continuous geometry of the real numbers, and an infinite family of hierarchical, ultrametric geometries, one for each prime. The real numbers and the p-adic numbers are the only possible completions of ℚ.

If the universe is written in the language of numbers (and our most successful physical theories suggest it is), then the choice of geometry for physical law is not arbitrary. There are only two fundamental kinds of number fields available: Archimedean and non-Archimedean. Physics has spent four centuries exploring the Archimedean option. This monograph is an exploration of the non-Archimedean alternative — an investigation into what physics looks like when built on an ultrametric foundation.

But first, we must understand what ultrametricity really means. The next chapter takes a deep dive into the ultrametric inequality and its astonishing geometric consequences.

---

*Next: [Chapter 4: The Ultrametric Inequality](04-the-ultrametric-inequality.md) — where we prove that in an ultrametric world, all triangles are isosceles, every point is the center of every ball that contains it, and continuous paths are impossible.*
