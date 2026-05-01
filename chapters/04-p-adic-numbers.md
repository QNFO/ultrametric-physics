---
layout: chapter
title: "Chapter 4: The p-adic Absolute Value and Q_p"
permalink: /chapters/04-p-adic-numbers/
previous_chapter: /chapters/03-ultrametric-inequality/
previous_title: "The Ultrametric Inequality"
next_chapter: /chapters/05-bruhat-tits-tree/
next_title: "The Bruhat-Tits Tree"
---

## Chapter 4: The p-adic Absolute Value and $$\mathbb{Q}_p$$

In the preceding chapters, we established the ultrametric inequality as a structural alternative to the Archimedean triangle inequality. We now construct the most important family of ultrametric spaces — the $$p$$-adic numbers — and discover that they are not an exotic curiosity but a *necessary* completion of the rational numbers, mandated by Ostrowski's Theorem. Along the way, we encounter a radical inversion of our intuition about size, an infinite series that converges to $$-1$$, and a version of Newton's method that lifts approximate solutions to exact ones.

---

### 4.1 The p-adic Valuation

The $$p$$-adic valuation formalizes the idea of measuring a number by "how divisible by $$p$$ it is."

<div class="definition">

**Definition 4.1 (p-adic Valuation).** Let $$p$$ be a prime. For a non-zero integer $$a$$, define $$v_p(a)$$ as the exponent of the highest power of $$p$$ dividing $$a$$. That is, write $$a = p^k \cdot m$$ with $$p \nmid m$$; then $$v_p(a) = k$$. For a non-zero rational number $$x = a/b$$ (in lowest terms), extend by:

\[
v_p(x) = v_p(a) - v_p(b).
\]

Set $$v_p(0) = +\infty$$ by convention.

</div>

The valuation satisfies three fundamental properties that mirror the behavior of logarithms:

<div class="theorem">

**Theorem 4.2 (Properties of the Valuation).** For all $$x, y \in \mathbb{Q}$$:

1. **(V1 — Multiplicativity)** $$v_p(xy) = v_p(x) + v_p(y)$$.
2. **(V2 — Ultrametric inequality)** $$v_p(x + y) \ge \min(v_p(x), v_p(y))$$, with equality whenever $$v_p(x) \ne v_p(y)$$.
3. **(V3 — Zero detection)** $$v_p(x) = +\infty$$ if and only if $$x = 0$$.

</div>

<div class="proof">

**Proof.** (V1) follows directly from the definition and the fundamental theorem of arithmetic: the exponent of $$p$$ in the product is the sum of the exponents. For (V2), write $$x = p^a \cdot r$$ and $$y = p^b \cdot s$$ with $$p \nmid rs$$, and assume without loss that $$a \le b$$. Then

\[
x + y = p^a(r + p^{b-a}s).
\]

Since $$p \nmid r$$, the term in parentheses may or may not be divisible by $$p$$. Thus $$v_p(x + y) \ge a = \min(v_p(x), v_p(y))$$. If $$a < b$$, then $$r + p^{b-a}s \equiv r \pmod{p}$$, so $$p$$ does not divide the sum in parentheses, and equality holds. ∎

</div>

The second property is the **non-Archimedean** (ultrametric) property in algebraic form. It says that the sum of two numbers cannot be *more* divisible by $$p$$ than the *less* divisible of the two — a dramatic departure from ordinary arithmetic, where sums can have entirely different divisibility properties than their summands.

---

### 4.2 The p-adic Absolute Value

From the valuation, we construct an absolute value that inverts our intuition: numbers highly divisible by $$p$$ are considered *small*.

<div class="definition">

**Definition 4.3 (p-adic Absolute Value).** For $$x \in \mathbb{Q}$$, define

\[
|x|_p = p^{-v_p(x)},
\]

with the convention $$|0|_p = 0$$.

</div>

<div class="theorem">

**Theorem 4.4 (p-adic Absolute Value Axioms).** $$|\cdot|_p$$ satisfies:

1. **(A1 — Positive definiteness)** $$|x|_p \ge 0$$, with equality iff $$x = 0$$.
2. **(A2 — Multiplicativity)** $$|xy|_p = |x|_p \, |y|_p$$.
3. **(A3 — Ultrametric inequality)** $$|x + y|_p \le \max(|x|_p, |y|_p)$$, with equality when $$|x|_p \ne |y|_p$$.

</div>

<div class="proof">

**Proof.** (A1) and (A2) follow immediately from (V1) and (V3). For (A3), using the valuation inequality:

\[
|x + y|_p = p^{-v_p(x+y)} \le p^{-\min(v_p(x), v_p(y))} = \max(p^{-v_p(x)}, p^{-v_p(y)}) = \max(|x|_p, |y|_p).
\]

Since $$\max(|x|_p, |y|_p) \le |x|_p + |y|_p$$, the ordinary triangle inequality also holds, but the ultrametric inequality is strictly stronger. ∎

</div>

<div class="insight">

**Key Insight: The Inversion of Size.** The $$p$$-adic absolute value is profoundly counter-intuitive from an Archimedean perspective:

- **Large powers become small.** $$|p^n|_p = p^{-n}$$. For $$p = 5$$: $$|5|_5 = 1/5$$, $$|25|_5 = 1/25$$, $$|125|_5 = 1/125$$. The number $$5^{100}$$ is $$p$$-adically less than $$10^{-70}$$ — practically zero.
- **Fractions become large.** $$|1/p|_p = p$$. For $$p = 2$$: $$|1/2|_2 = 2$$, $$|1/8|_2 = 8$$.
- **Numbers not divisible by $$p$$ have size 1.** For any integer $$m$$ with $$p \nmid m$$: $$|m|_p = 1$$.

This inversion is the essence of non-Archimedean geometry: "closeness" measures shared divisibility by $$p$$, not difference in magnitude.

</div>

<div class="example">

**Example 4.5 (Computing p-adic Absolute Values).** Let $$p = 2$$:

- $$|8|_2 = 2^{-3} = 1/8$$ — because $$8 = 2^3$$.
- $$|3/4|_2 = |3 \cdot 2^{-2}|_2 = 2^2 = 4$$ — because the denominator contributes negative valuation.
- $$|7|_2 = 2^0 = 1$$ — because 7 is not divisible by 2.
- $$|12|_2 = |2^2 \cdot 3|_2 = 2^{-2} = 1/4$$ — only the power of 2 matters.
- $$|5/18|_2 = |5 \cdot 2^{-1} \cdot 3^{-2}|_2 = 2^1 = 2$$.

Notice that the 3-adic absolute value of the same numbers would be entirely different: $$|12|_3 = |2^2 \cdot 3|_3 = 3^{-1} = 1/3$$, while $$|12|_2 = 1/4$$. Each prime $$p$$ provides its own distinct "lens" through which to view rational numbers.

</div>

---

### 4.3 The p-adic Metric and Strange Convergence

The $$p$$-adic absolute value induces an ultrametric:

\[
d_p(x, y) = |x - y|_p.
\]

In this metric, a sequence $$(x_n)$$ converges to $$x$$ if $$|x_n - x|_p \to 0$$, meaning the differences $$x_n - x$$ become more and more divisible by $$p$$. This leads to striking phenomena:

<div class="example">

**Example 4.6 (The Sequence $$2^n$$ in the 2-adic World).** Consider $$x_n = 2^n$$. In the ordinary real metric: $$|2^n|_\infty \to \infty$$. In the 2-adic metric:

\[
|2^n|_2 = 2^{-n} \to 0 \quad \text{as } n \to \infty.
\]

Thus $$2^n \to 0$$ in $$\mathbb{Q}_2$$! The sequence that grows without bound in the real world vanishes in the 2-adic world.

</div>

<div class="example">

**Example 4.7 (A Divergent Series that Converges p-adically).** Consider the geometric series in the 2-adic world:

\[
1 + 2 + 4 + 8 + 16 + \cdots = \sum_{n=0}^{\infty} 2^n.
\]

In the real numbers, this series diverges to infinity. But in $$\mathbb{Q}_2$$, convergence is determined by the 2-adic norm of the terms:

\[
|2^n|_2 = 2^{-n} \to 0,
\]

so the terms form a null sequence. For a geometric series, the sum is $$\frac{1}{1 - r}$$ when $$|r| < 1$$. Here $$|2|_2 = 1/2 < 1$$, so:

\[
1 + 2 + 4 + 8 + \cdots = \frac{1}{1 - 2} = -1 \quad \text{in } \mathbb{Q}_2!
\]

This is not a trick — it is a rigorous statement about convergence in the 2-adic metric. The partial sums $$S_n = 2^n - 1$$ converge to $$-1$$ since $$|S_n - (-1)|_2 = |2^n|_2 = 2^{-n} \to 0$$.

</div>

<div class="insight">

**Key Insight: Convergence Depends on the Metric.** The same sequence can converge, diverge, or converge to a different limit depending on which absolute value defines the metric. This is the lesson of Ostrowski's Theorem: there are many equally valid completions of $$\mathbb{Q}$$, each with its own notion of convergence.

</div>

---

### 4.4 The Non-Archimedean Boundedness Criterion

A powerful criterion distinguishes ultrametric absolute values from Archimedean ones.

<div class="lemma">

**Lemma 4.8 (Boundedness Criterion).** An absolute value $$|\cdot|$$ on a field $$K$$ is non-Archimedean if and only if the set $$\{\,|n \cdot 1| : n \in \mathbb{Z}\,\}$$ is bounded, where $$n \cdot 1$$ denotes the sum of the multiplicative identity with itself $$n$$ times.

</div>

<div class="proof">

**Proof.** ($$\Rightarrow$$) If $$|\cdot|$$ is non-Archimedean, then for any $$n \in \mathbb{N}$$:

\[
|n \cdot 1| = |1 + 1 + \cdots + 1| \le \max(|1|, \ldots, |1|) = |1| = 1.
\]

So the set is bounded by 1. ($$\Leftarrow$$) Conversely, suppose $$|n \cdot 1| \le C$$ for all $$n$$. Then for any $$x, y$$ and any $$n$$, the binomial theorem gives:

\[
|(x + y)^n| = \left|\sum_{k=0}^n \binom{n}{k} x^k y^{n-k}\right| \le \sum_{k=0}^n |\binom{n}{k}| \, |x|^k |y|^{n-k} \le C(n+1) \max(|x|, |y|)^n.
\]

Taking $$n$$-th roots and letting $$n \to \infty$$ yields $$|x + y| \le \max(|x|, |y|)$$, the ultrametric inequality. ∎

</div>

For the $$p$$-adic absolute value, $$|n|_p \le 1$$ for all integers $$n$$, confirming its non-Archimedean nature. In contrast, for the usual absolute value, $$|n|_\infty = n$$ is unbounded — it is Archimedean.

---

### 4.5 Ostrowski's Theorem: The Classification of Absolute Values

In 1916, Alexander Ostrowski proved a remarkable classification theorem that establishes the $$p$$-adic absolute values as the *only* non-trivial alternatives to the usual one.

<div class="theorem">

**Theorem 4.9 (Ostrowski, 1916).** Every non-trivial absolute value on $$\mathbb{Q}$$ is equivalent to either:

- the usual Archimedean absolute value $$|\cdot|_\infty$$, or
- some $$p$$-adic absolute value $$|\cdot|_p$$ for a prime $$p$$.

Two absolute values are *equivalent* if one is a positive power of the other: $$|\cdot|_1 \sim |\cdot|_2$$ iff there exists $$\alpha > 0$$ such that $$|x|_1 = |x|_2^\alpha$$ for all $$x$$.

</div>

<div class="proof">

**Proof (Sketch).** Let $$|\cdot|$$ be a non-trivial absolute value on $$\mathbb{Q}$$. Consider $$|n|$$ for integers $$n$$.

**Case 1:** There exists $$n > 1$$ with $$|n| > 1$$. Then by Lemma 4.8, $$|\cdot|$$ is Archimedean. Choose the smallest such $$n$$; one shows that $$|\cdot|$$ is equivalent to $$|\cdot|_\infty$$.

**Case 2:** $$|n| \le 1$$ for all integers $$n$$. Then by Lemma 4.8, $$|\cdot|$$ is non-Archimedean. Since it is non-trivial, there exists a smallest integer $$n > 1$$ with $$|n| < 1$$. This $$n$$ must be prime (if $$n = ab$$, then $$|a||b| = |n| < 1$$ implies $$|a| < 1$$ or $$|b| < 1$$, contradicting minimality). Let $$p$$ be this prime. One then shows that $$|\cdot|$$ is equivalent to $$|\cdot|_p$$. ∎

</div>

<div class="insight">

**Key Insight: The Necessity of $$\mathbb{Q}_p$$.** Ostrowski's Theorem has profound philosophical consequences: the $$p$$-adic numbers are not an optional mathematical curiosity but a *necessary* completion of the rational numbers. Just as the real numbers capture "geometric" completion (filling in the gaps of limits), the $$p$$-adic numbers capture "arithmetic" completion (filling in the gaps of divisibility). A complete understanding of the rational numbers requires *all* completions: $$\mathbb{R}$$ and $$\mathbb{Q}_p$$ for every prime $$p$$.

</div>

---

### 4.6 The Field $$\mathbb{Q}_p$$ as Completion

We construct $$\mathbb{Q}_p$$ by completing $$\mathbb{Q}$$ with respect to the $$p$$-adic metric $$d_p$$, exactly as $$\mathbb{R}$$ is constructed by completing $$\mathbb{Q}$$ with respect to the Euclidean metric.

<div class="definition">

**Definition 4.10 (The Field of p-adic Numbers).** The field $$\mathbb{Q}_p$$ is the completion of $$\mathbb{Q}$$ with respect to the $$p$$-adic metric $$d_p(x, y) = |x - y|_p$$. Every element of $$\mathbb{Q}_p$$ can be represented uniquely as a $$p$$-adic expansion:

\[
x = \sum_{n = v}^{\infty} a_n p^n,
\]

where $$v = v_p(x) \in \mathbb{Z}$$, each digit $$a_n \in \{0, 1, \ldots, p-1\}$$, and $$a_v \ne 0$$ (unless $$x = 0$$). The expansion extends infinitely to the *left* — opposite to the decimal expansion, which extends infinitely to the right.

</div>

<div class="insight">

**Key Insight: Leftward Expansion.** In the decimal expansion $$0.d_1 d_2 d_3 \ldots$$, each subsequent digit represents a smaller contribution (tenths, hundredths, thousandths). In the $$p$$-adic expansion $$\ldots a_3 a_2 a_1 a_0$$, each subsequent digit (reading right to left) represents a contribution multiplied by $$p$$ — the numbers "grow" to the left. This is why convergence is measured by divisibility: adding higher powers of $$p$$ makes the number *smaller*, and the infinite leftward tail converges $$p$$-adically.

</div>

The arithmetic of $$p$$-adic expansions follows the same rules as base-$$p$$ arithmetic, with carries propagating to the left. For example:

<div class="example">

**Example 4.11 (Computing 1/3 in $$\mathbb{Q}_5$$).** We seek digits $$a_n \in \{0,1,2,3,4\}$$ such that:

\[
3 \times (a_0 + a_1 \cdot 5 + a_2 \cdot 5^2 + \cdots) = 1.
\]

Working digit by digit in base 5:

- $$3a_0 \equiv 1 \pmod{5}$$: $$a_0 = 2$$ (since $$3 \times 2 = 6 \equiv 1 \pmod{5}$$), carry 1.
- $$3a_1 + 1 \equiv 0 \pmod{5}$$: $$3a_1 \equiv 4 \pmod{5}$$, so $$a_1 = 3$$ ($$3 \times 3 = 9 \equiv 4 \pmod{5}$$), carry 1.
- $$3a_2 + 1 \equiv 0 \pmod{5}$$: $$a_2 = 3$$ again, carry 1.

The pattern repeats: $$a_n = 3$$ for all $$n \ge 1$$. Thus in $$\mathbb{Q}_5$$:

\[
\frac{1}{3} = 2 + 3 \cdot 5 + 3 \cdot 5^2 + 3 \cdot 5^3 + \cdots = \ldots 33332_{(5)}.
\]

This is a perfectly valid, convergent representation in $$\mathbb{Q}_5$$.

</div>

<div class="example">

**Example 4.12 (Square Roots in $$\mathbb{Q}_p$$ — $$\sqrt{-1}$$).** A striking fact: the equation $$x^2 = -1$$ has solutions in $$\mathbb{Q}_5$$ but not in $$\mathbb{Q}_3$$.

**In $$\mathbb{Q}_5$$:** We solve $$x^2 \equiv -1 \equiv 4 \pmod{5}$$. The solutions are $$x \equiv \pm 2 \pmod{5}$$. Starting from $$x_0 = 2$$, we can iteratively lift using Hensel's Lemma (Section 4.8) to obtain a full $$5$$-adic expansion:

\[
i = 2 + 1 \cdot 5 + 2 \cdot 5^2 + 1 \cdot 5^3 + 3 \cdot 5^4 + \cdots \quad \text{in } \mathbb{Q}_5.
\]

Thus $$\mathbb{Q}_5$$ contains a square root of $$-1$$, denoted $$i_5$$.

**In $$\mathbb{Q}_3$$:** We solve $$x^2 \equiv -1 \equiv 2 \pmod{3}$$. But squares modulo 3 are $$0^2 = 0$$, $$1^2 = 1$$, $$2^2 = 1$$ — no $$x$$ satisfies $$x^2 \equiv 2 \pmod{3}$$. Thus $$\sqrt{-1} \notin \mathbb{Q}_3$$.

This illustrates that different $$p$$-adic fields have different algebraic properties. $$\mathbb{Q}_p$$ contains $$\sqrt{-1}$$ iff $$p \equiv 1 \pmod{4}$$ (and also for $$p = 2$$, with a slightly different condition).

</div>

---

### 4.7 The Ring of p-adic Integers $$\mathbb{Z}_p$$

Within $$\mathbb{Q}_p$$, a distinguished compact subring plays the role of the "unit ball."

<div class="definition">

**Definition 4.13 (p-adic Integers).** The ring of $$p$$-adic integers is:

\[
\mathbb{Z}_p = \{ x \in \mathbb{Q}_p : |x|_p \le 1 \} = \{ x \in \mathbb{Q}_p : v_p(x) \ge 0 \}.
\]

Equivalently, $$\mathbb{Z}_p$$ consists of $$p$$-adic expansions with no fractional part: $$x = \sum_{n=0}^\infty a_n p^n$$ (the valuation start index $$v \ge 0$$).

The **units** of $$\mathbb{Z}_p$$ are:

\[
\mathbb{Z}_p^\times = \{ x \in \mathbb{Z}_p : |x|_p = 1 \} = \{ x \in \mathbb{Z}_p : a_0 \ne 0 \}.
\]

</div>

<div class="theorem">

**Theorem 4.14 (Properties of $$\mathbb{Z}_p$$).**

1. $$\mathbb{Z}_p$$ is a compact topological ring.
2. Every element $$x \in \mathbb{Q}_p^\times$$ can be written uniquely as $$x = p^n \cdot u$$ with $$n \in \mathbb{Z}$$ and $$u \in \mathbb{Z}_p^\times$$.
3. $$\mathbb{Z}_p$$ is the inverse limit: $$\mathbb{Z}_p = \varprojlim_n \mathbb{Z} / p^n \mathbb{Z}$$.
4. The quotients are finite: $$\mathbb{Z}_p / p^n \mathbb{Z}_p \cong \mathbb{Z} / p^n \mathbb{Z}$$.

</div>

<div class="proof">

**Proof (Sketch).** For compactness, every sequence in $$\mathbb{Z}_p$$ has a convergent subsequence (by diagonal argument on digit sequences). The decomposition $$x = p^{v_p(x)} \cdot u$$ is immediate from the expansion. The inverse limit characterization means that a $$p$$-adic integer is equivalent to a compatible system of residues modulo $$p^n$$ for all $$n$$ — this is the essence of the expansion: knowing $$x \bmod p^n$$ for all $$n$$ determines $$x$$ uniquely. ∎

</div>

The compactness of $$\mathbb{Z}_p$$ is a crucial topological property with no Archimedean analog — the closed unit ball in $$\mathbb{R}$$ is not compact. This compactness underlies many convergence results in $$p$$-adic analysis.

---

### 4.8 Hensel's Lemma: Newton's Method in the p-adic World

Hensel's Lemma is the $$p$$-adic analog of Newton's method for finding roots. It states that an approximate root can be "lifted" to an exact root, provided a simple non-degeneracy condition holds.

<div class="theorem">

**Theorem 4.15 (Hensel's Lemma).** Let $$f(x) \in \mathbb{Z}_p[x]$$ be a polynomial with $$p$$-adic integer coefficients. Suppose there exists $$a_0 \in \mathbb{Z}_p$$ such that:

\[
f(a_0) \equiv 0 \pmod{p} \quad \text{and} \quad f'(a_0) \not\equiv 0 \pmod{p}.
\]

Then there exists a unique $$a \in \mathbb{Z}_p$$ such that $$f(a) = 0$$ and $$a \equiv a_0 \pmod{p}$$.

</div>

<div class="proof">

**Proof.** We construct $$a$$ iteratively via Newton's method. Define the sequence:

\[
a_{n+1} = a_n - \frac{f(a_n)}{f'(a_n)}.
\]

The conditions ensure that each iteration doubles the $$p$$-adic precision: $$|f(a_{n+1})|_p \le |f(a_n)|_p^2$$. Since $$|f(a_0)|_p < 1$$, we obtain $$|f(a_n)|_p \to 0$$, and the sequence converges to a root $$a = \lim a_n$$. Uniqueness follows from the non-degeneracy of the derivative. ∎

</div>

<div class="example">

**Example 4.16 (Lifting $$\sqrt{-1}$$ in $$\mathbb{Q}_5$$).** Let $$f(x) = x^2 + 1$$. The initial approximation $$a_0 = 2$$ satisfies $$f(2) = 5 \equiv 0 \pmod{5}$$ and $$f'(2) = 4 \not\equiv 0 \pmod{5}$$. Hensel's Lemma guarantees a unique $$5$$-adic integer $$i_5$$ with $$i_5^2 = -1$$ and $$i_5 \equiv 2 \pmod{5}$$. The Newton iteration:

\[
a_{n+1} = a_n - \frac{a_n^2 + 1}{2a_n} = \frac{a_n^2 - 1}{2a_n}
\]

converges quadratically in the 5-adic metric, yielding the infinite expansion given in Example 4.12.

</div>

Hensel's Lemma is a cornerstone of $$p$$-adic algebra. It underpins the fact that many polynomial equations have $$p$$-adic solutions when they have solutions modulo $$p$$, providing a bridge between modular arithmetic and exact $$p$$-adic arithmetic.

---

### 4.9 Topological Properties of $$\mathbb{Q}_p$$

The topology induced by the $$p$$-adic metric is radically different from the familiar Euclidean topology.

<div class="theorem">

**Theorem 4.17 (Topological Properties of $$\mathbb{Q}_p$$).** The field $$\mathbb{Q}_p$$ is:

1. **Complete:** Every Cauchy sequence converges.
2. **Locally compact:** Every point has a compact neighborhood (e.g., a closed ball).
3. **Totally disconnected:** The only connected subsets are singletons. The space is a Cantor-like fractal.
4. **Zero-dimensional:** The topology has a base of clopen (simultaneously closed and open) sets — every ball is both open and closed.

</div>

<div class="proof">

**Proof.** Completeness follows from the construction as a metric completion. Local compactness follows from the compactness of $$\mathbb{Z}_p$$ and translation invariance. For total disconnectedness: in an ultrametric space, all triangles are isosceles, which prohibits the existence of non-trivial paths between points. Specifically, if $$x \ne y$$, consider any point $$z$$ distinct from both. The ultrametric inequality forces $$d(x,z)$$ and $$d(y,z)$$ to both be at least $$d(x,y)$$, making it impossible to "connect" $$x$$ and $$y$$ through a continuum of intermediate points. Every ball is clopen because its complement is a union of disjoint balls of the same radius — a consequence of the nesting property of ultrametric balls. ∎

</div>

The total disconnectedness of $$\mathbb{Q}_p$$ is particularly important for physical applications. It means the state space has no continuous deformations — only discrete transitions are possible. This is the geometric origin of intrinsic fault tolerance in non-Archimedean quantum systems.

<div class="insight">

**Key Insight: Discreteness from Geometry.** The topological properties of $$\mathbb{Q}_p$$ — total disconnectedness, zero-dimensionality — are not defects but features. They provide a geometric mechanism for digitizing quantum state space without imposing artificial discretizations. The geometry itself enforces discrete behavior, which we will exploit in subsequent chapters to construct quantum systems with inherent immunity to continuous noise.

</div>

---

### 4.10 The Product Formula: A Glimpse of Unity

Before concluding, we preview a deep result that unifies all completions of $$\mathbb{Q}$$. Let $$\mathcal{P}$$ denote the set of all places (equivalence classes of absolute values): the infinite place $$\infty$$ and all finite places $$p$$.

<div class="theorem">

**Theorem 4.18 (Product Formula).** For any non-zero rational number $$x$$:

\[
|x|_\infty \cdot \prod_{p \text{ prime}} |x|_p = 1.
\]

</div>

<div class="proof">

**Proof.** Write $$x = \pm \prod_p p^{n_p}$$ by prime factorization, where only finitely many $$n_p$$ are non-zero. Then $$|x|_p = p^{-n_p}$$ and $$|x|_\infty = \prod_p p^{n_p}$$. Multiplying over all places, every prime factor appears once as $$p^{-n_p}$$ (from $$|\cdot|_p$$) and once as $$p^{n_p}$$ (from $$|\cdot|_\infty$$), yielding 1. ∎

</div>

The product formula is a conservation law: if a number is "large" in the real sense, it must be "small" in the $$p$$-adic senses to compensate, and vice versa. It hints at a unified adelic framework where all completions are treated on equal footing — a theme we will explore in later chapters.

---

### Chapter Summary

We have constructed the $$p$$-adic numbers as the completions of $$\mathbb{Q}$$ mandated by Ostrowski's Theorem. The key takeaways:

- The $$p$$-adic absolute value inverts the intuition of size by measuring divisibility.
- The induced metric is ultrametric, with all the strong geometric properties this implies.
- Strange convergence phenomena ($$2^n \to 0$$, $$1+2+4+8+\cdots = -1$$) are rigorous consequences of the metric.
- $$\mathbb{Q}_p$$ is a complete, locally compact, totally disconnected topological field.
- Hensel's Lemma provides an efficient method for solving equations $$p$$-adically.
- The product formula foreshadows a unified perspective on all completions of $$\mathbb{Q}$$.

In the next chapter, we will give a geometric face to these algebraic structures by constructing the **Bruhat-Tits tree** — the natural geometric realization of $$p$$-adic space that will serve as the arena for non-Archimedean quantum computation.
