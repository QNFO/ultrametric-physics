---
layout: chapter
title: "Chapter 2: Distance and Metric Spaces"
permalink: /chapters/02-distance-metrics/
previous_chapter: /chapters/01-sets-numbers/
previous_title: "Chapter 1: Sets & Numbers"
next_chapter: /chapters/03-ultrametric-inequality/
next_title: "Chapter 3: Ultrametric Inequality"
---

## Chapter 2: Distance and Metric Spaces

Distance is the most fundamental geometric concept. In this chapter, we make it mathematically precise through the theory of **metric spaces**.

### 2.1 What Is a Metric?

<div class="definition">
<div class="label">Definition 2.1 (Metric, Metric space)</div>
A <strong>metric</strong> on a set $X$ is a function $d: X \times X \to \mathbb{R}_{\geq 0}$ satisfying, for all $x,y,z \in X$:
<ol>
<li><strong>Identity of indiscernibles:</strong> $d(x,y) = 0 \iff x = y$.</li>
<li><strong>Symmetry:</strong> $d(x,y) = d(y,x)$.</li>
<li><strong>Triangle inequality:</strong> $d(x,z) \leq d(x,y) + d(y,z)$.</li>
</ol>
$(X,d)$ is a <strong>metric space</strong>.
</div>

<div class="example">
<div class="label">Example 2.2 (Euclidean metric)</div>
On $\mathbb{R}$: $d(x,y)=|x-y|$. On $\mathbb{R}^n$: $d(\mathbf{x},\mathbf{y})=\sqrt{\sum (x_i-y_i)^2}$.
</div>

<div class="example">
<div class="label">Example 2.3 (Discrete metric)</div>
$d(x,y) = 0$ if $x=y$, $1$ otherwise. Every point is equally far from every other point.
</div>

### 2.2 Open Balls and Topology

<div class="definition">
<div class="label">Definition 2.4 (Open ball)</div>
$B(x,r) = \{y \in X \mid d(x,y) < r\}$.
</div>

In $\mathbb{R}$, $B(0,1)=(-1,1)$. In $\mathbb{R}^2$ with Manhattan metric, $B(\mathbf{0},1)$ is a diamond.

<div class="definition">
<div class="label">Definition 2.5 (Open set, Topology)</div>
$U \subseteq X$ is <strong>open</strong> if $\forall x \in U, \exists r > 0: B(x,r) \subseteq U$. The collection of all open sets is the <strong>topology</strong>.
</div>

### 2.3 Convergence and Completeness

<div class="definition">
<div class="label">Definition 2.6 (Convergent sequence)</div>
$x_n \to x$ if $\forall \varepsilon > 0, \exists N, \forall n \geq N: d(x_n,x) < \varepsilon$.
</div>

<div class="definition">
<div class="label">Definition 2.7 (Cauchy sequence)</div>
$(x_n)$ is <strong>Cauchy</strong> if $\forall \varepsilon > 0, \exists N, \forall m,n \geq N: d(x_m,x_n) < \varepsilon$.
</div>

<div class="definition">
<div class="label">Definition 2.8 (Complete metric space)</div>
A space is <strong>complete</strong> if every Cauchy sequence converges.
</div>

<div class="example">
<div class="label">Example 2.9</div>
$\mathbb{Q}$ is <strong>not</strong> complete. The sequence $1, 1.4, 1.41, 1.414, \ldots$ (converging to $\sqrt{2}$) is Cauchy in $\mathbb{Q}$ but has no rational limit.
</div>

<div class="theorem">
<div class="label">Theorem 2.10 (Metric completion)</div>
Every metric space has a unique completion. The completion of $\mathbb{Q}$ w.r.t. $d_\infty(x,y)=|x-y|_\infty$ is $\mathbb{R}$, the real numbers.
</div>

### 2.4 The Metric from Absolute Values

Any absolute value gives a metric: $d(x,y)=|x-y|$. But Ostrowski's Theorem (Chapter 4) reveals there are infinitely many absolute values on $\mathbb{Q}$ — and each gives a different geometry.

---

**Next: [Chapter 3: The Ultrametric Inequality →]({{ '/chapters/03-ultrametric-inequality' | relative_url }})**
