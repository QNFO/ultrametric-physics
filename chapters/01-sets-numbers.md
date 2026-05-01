---
layout: chapter
title: "Chapter 1: Sets, Relations, and Numbers"
permalink: /chapters/01-sets-numbers/
previous_chapter: /chapters/00-prologue/
previous_title: "Prologue"
next_chapter: /chapters/02-distance-metrics/
next_title: "Chapter 2: Distance & Metrics"
---

## Chapter 1: Sets, Relations, and Numbers

We begin at the logical beginning. Everything that follows is built on the concepts defined here.

### 1.1 Sets

<div class="definition">
<div class="label">Definition 1.1 (Set)</div>
A <strong>set</strong> is a collection of distinct objects, called <strong>elements</strong>. We write $x \in A$ for membership and $x \notin A$ for non-membership.
</div>

**Example.** $A = \{1, 2, 3\}$, $\mathbb{N} = \{0, 1, 2, 3, \ldots\}$.

<div class="definition">
<div class="label">Definition 1.2 (Subset, Equality)</div>
$A \subseteq B$ if every element of $A$ is also in $B$. $A = B$ iff $A \subseteq B$ and $B \subseteq A$.
</div>

### 1.2 Set Operations

<div class="definition">
<div class="label">Definition 1.3 (Union, Intersection, Difference)</div>
<ul>
<li><strong>Union:</strong> $A \cup B = \{x \mid x \in A \text{ or } x \in B\}$</li>
<li><strong>Intersection:</strong> $A \cap B = \{x \mid x \in A \text{ and } x \in B\}$</li>
<li><strong>Difference:</strong> $A \setminus B = \{x \mid x \in A \text{ and } x \notin B\}$</li>
</ul>
</div>

### 1.3 Ordered Pairs and Cartesian Products

<div class="definition">
<div class="label">Definition 1.4 (Ordered pair, Cartesian product)</div>
$(a,b) = (c,d)$ iff $a=c$ and $b=d$. $A \times B = \{(a,b) \mid a \in A, b \in B\}$.
</div>

### 1.4 Relations and Functions

<div class="definition">
<div class="label">Definition 1.5 (Relation, Function)</div>
A <strong>relation</strong> $R$ between $A$ and $B$ is any subset $R \subseteq A \times B$. A <strong>function</strong> $f: A \to B$ is a relation where each $a \in A$ appears in exactly one ordered pair. We write $f(a) = b$.
</div>

<div class="definition">
<div class="label">Definition 1.6 (Injective, Surjective, Bijective)</div>
$f$ is <strong>injective</strong> if $f(a_1)=f(a_2) \implies a_1=a_2$. <strong>Surjective</strong> if every $b \in B$ has some $a$ with $f(a)=b$. <strong>Bijective</strong> if both.
</div>

### 1.5 Binary Operations and Algebraic Structures

<div class="definition">
<div class="label">Definition 1.7 (Binary operation)</div>
A binary operation $\star$ on $S$ is a function $\star: S \times S \to S$.
</div>

<div class="definition">
<div class="label">Definition 1.8 (Group)</div>
$(G, \star)$ is a <strong>group</strong> if $\star$ is associative, has identity $e$, and every element has an inverse. If also commutative, it's <strong>abelian</strong>.
</div>

<div class="definition">
<div class="label">Definition 1.9 (Ring, Field)</div>
A <strong>ring</strong> $(R,+,\cdot)$ has $(R,+)$ abelian group and $\cdot$ associative with identity, plus distributivity. A <strong>field</strong> is a ring where every non-zero element has a multiplicative inverse.
</div>

### 1.6 Numbers

$\mathbb{N} = \{0,1,2,3,\ldots\}$ (natural numbers). $\mathbb{Z} = \{\ldots,-2,-1,0,1,2,\ldots\}$ (integers).

<div class="definition">
<div class="label">Definition 1.10 (Rational numbers)</div>
$\mathbb{Q} = \{a/b \mid a,b \in \mathbb{Z}, b \neq 0\}$ with equivalence $a/b = c/d$ iff $ad = bc$.
</div>

### 1.7 The Standard Absolute Value

<div class="definition">
<div class="label">Definition 1.11 (Absolute value)</div>
$|x|_\infty = x$ if $x \geq 0$, $-x$ if $x < 0$. Properties: positive definiteness, multiplicativity, triangle inequality $|x+y|_\infty \leq |x|_\infty + |y|_\infty$.
</div>

### 1.8 Prime Factorization

<div class="theorem">
<div class="label">Theorem 1.12 (Fundamental Theorem of Arithmetic)</div>
Every integer $n > 1$ factors uniquely into primes: $n = p_1^{e_1} p_2^{e_2} \cdots p_k^{e_k}$.
</div>

This theorem is the gateway to measuring numbers not by size, but by which primes divide them — the subject of Chapter 4.

---

**Next: [Chapter 2: Distance and Metric Spaces →]({{ '/chapters/02-distance-metrics' | relative_url }})**
