---
layout: chapter
title: "Chapter 6: Ultrametric Quantum Mechanics"
permalink: /chapters/06-ultrametric-qm/
previous_chapter: /chapters/05-bruhat-tits-tree/
previous_title: "Chapter 5: Bruhat-Tits Tree"
next_chapter: /chapters/07-ultrametric-qft/
next_title: "Chapter 7: Ultrametric QFT"
---

## Chapter 6: Ultrametric Quantum Mechanics

With p-adic numbers $\mathbb{Q}_p$ and Bruhat-Tits trees $T_p$ in hand, we now formulate quantum mechanics on ultrametric spaces.

### 6.1 Wavefunctions on $\mathbb{Q}_p$

A quantum state is a function $\psi: \mathbb{Q}_p \to \mathbb{C}$ with $\int_{\mathbb{Q}_p} |\psi(x)|^2 d\mu(x) = 1$, where $\mu$ is the Haar measure: the unique translation-invariant measure, normalized so $\mu(\mathbb{Z}_p) = 1$, satisfying $\mu(B(x, p^{-n})) = p^{-n}$.

### 6.2 Locally Constant Functions

<div class="definition">
<div class="label">Definition 6.1 (Locally constant)</div>
$f: \mathbb{Q}_p \to \mathbb{C}$ is <strong>locally constant</strong> if every point has a neighborhood where $f$ is constant. This is the p-adic analogue of smoothness. On $\mathbb{Z}_p$, such functions depend on only finitely many p-adic digits.
</div>

### 6.3 Additive Characters and Fourier Transform

<div class="definition">
<div class="label">Definition 6.2 (Additive character)</div>
$\chi(x) = e^{2\pi i \{x\}_p}$ where $\{x\}_p$ is the fractional part. $\chi(x+y) = \chi(x)\chi(y)$.
</div>

**Fourier transform:** $\hat{f}(\xi) = \int f(x) \overline{\chi(x\xi)} d\mu(x)$, with inversion $f(x) = \int \hat{f}(\xi) \chi(x\xi) d\mu(\xi)$.

### 6.4 The Vladimirov Operator

<div class="definition">
<div class="label">Definition 6.3 (Vladimirov operator)</div>
For $0 < \alpha < 2$:
$$(D_p^\alpha f)(x) = \frac{1-p^{-\alpha}}{1-p^{\alpha-1}} \int_{\mathbb{Q}_p} \frac{f(y)-f(x)}{|x-y|_p^{1+\alpha}} d\mu(y)$$
</div>

<div class="theorem">
<div class="label">Theorem 6.4 (Fourier multiplier)</div>
$\widehat{D_p^\alpha f}(\xi) = |\xi|_p^\alpha \hat{f}(\xi)$. This is the p-adic analogue of $\widehat{(-\nabla^2)f}(k) = |k|^2 \hat{f}(k)$. The spectrum $|\xi|_p^\alpha$ takes only discrete values $\{p^{-n\alpha} : n \in \mathbb{Z}\} \cup \{0\}$ — automatic quantization.
</div>

### 6.5 The p-adic Schrödinger Equation

$$i\hbar \frac{\partial}{\partial t}\psi(x,t) = \left[-\frac{\hbar^2}{2m} D_p^\alpha + V(x)\right]\psi(x,t)$$

For a free particle ($V=0$), stationary states are $\psi_\xi(x) = \chi(\xi x)$ with discrete energy $E(\xi) = \frac{\hbar^2}{2m} |\xi|_p^\alpha$.

### 6.6 State Encoding on the Tree

A quantum state on $T_p$ is $\psi: V(T_p) \to \mathbb{C}$ with $\sum_v |\psi(v)|^2 = 1$. The logical information lives at a deep interior vertex, protected by hierarchical energy barriers. Environmental noise at the boundary cannot reach the logical vertex without traversing many edges — passive geometric protection.

### 6.7 The Monna Map: Measurement

<div class="definition">
<div class="label">Definition 6.5 (Monna map)</div>
$M_p: \mathbb{Q}_p \to \mathbb{R}$ projects p-adic to real by inverting the expansion: $M_p(\sum a_n p^n) = \sum a_n p^{-n}$. This is a lossy projection; the apparent randomness of quantum measurement arises from information lost in this projection.
</div>

<div class="insight">
<strong>Ontological shift:</strong> Decoherence is not loss of information to the environment — it is <strong>misinterpretation</strong> of p-adic information by Archimedean measurement apparatus.
</div>

### 6.8 Ratio-Based Generalization

For scaling ratio $q > 1$, the Vladimirov operator generalizes: $D_q^\alpha$ with eigenvalues $\lambda_n = q^{-n\alpha}$, independent of any base representation.

### 6.9 Comparison

| Feature | Archimedean QM | Ultrametric QM |
|---|---|---|
| State space | Bloch sphere (continuous) | Bruhat-Tits tree (discrete) |
| Laplacian | $-\nabla^2$ | $D_p^\alpha$ (Vladimirov) |
| Spectrum | Continuous | Discrete |
| Measurement | Born rule (axiom) | Monna map (geometry) |
| Fault tolerance | Active correction | Passive/geometric |

---

**Next: [Chapter 7: Ultrametric QFT →]({{ '/chapters/07-ultrametric-qft' | relative_url }})**
