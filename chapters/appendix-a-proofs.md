---
layout: chapter
title: "Appendix A: Full Proofs of Key Theorems"
permalink: /chapters/appendix-a-proofs/
previous_chapter: /chapters/18-tabletop-experiments/
previous_title: "Chapter 18: Tabletop"
next_chapter: /chapters/appendix-b-references/
next_title: "Appendix B: References"
---

## Appendix A: Full Proofs of Key Theorems

### A.1 Boundedness Criterion

<div class="lemma">
<div class="label">Lemma A.1</div>
An absolute value $|\cdot|$ is non-Archimedean ($|x+y| \leq \max(|x|,|y|)$) iff $\{|n \cdot 1| : n \in \mathbb{Z}\}$ is bounded.
</div>

<div class="proof">
<div class="label">Proof</div>
($\Rightarrow$) If $|\cdot|$ is non-Archimedean, $|n \cdot 1| = |1+\cdots+1| \leq \max(|1|,\ldots,|1|) = 1$ for all $n \in \mathbb{N}$, so the set is bounded by 1.

($\Leftarrow$) Suppose $|n \cdot 1| \leq C$ for all $n$. For any $x,y$ and $n \geq 1$:
$$|x+y|^n = \left|\sum_{k=0}^n \binom{n}{k} x^k y^{n-k}\right| \leq C \sum_{k=0}^n |x|^k |y|^{n-k}$$
Taking $n$-th roots and $n \to \infty$: $|x+y| \leq \max(|x|,|y|)$, since the dominant term is $\max(|x|,|y|)^n$ multiplied by at most $C(n+1)$. $\square$
</div>

### A.2 Strong Triangle Inequality from Valuation

<div class="theorem">
<div class="label">Theorem A.2</div>
$|x+y|_p \leq \max(|x|_p, |y|_p)$.
</div>

<div class="proof">
<div class="label">Proof</div>
Let $m = \min(v_p(x), v_p(y))$. Write $x = p^m a$, $y = p^m b$ with at least one of $a,b$ not divisible by $p$. Then $x+y = p^m(a+b)$ and $v_p(a+b) \geq 0$ (possibly $> 0$ if cancellation). Hence $v_p(x+y) = m + v_p(a+b) \geq m$, so $|x+y|_p = p^{-v_p(x+y)} \leq p^{-m} = \max(p^{-v_p(x)}, p^{-v_p(y)}) = \max(|x|_p, |y|_p)$. Equality holds when $v_p(x) \neq v_p(y)$. $\square$
</div>

### A.3 Ostrowski's Theorem (1916)

<div class="theorem">
<div class="label">Theorem A.3 (Ostrowski)</div>
Every non-trivial absolute value on $\mathbb{Q}$ is equivalent to $|\cdot|_\infty$ or some $|\cdot|_p$.
</div>

<div class="proof">
<div class="label">Proof</div>
Let $|\cdot|$ be a non-trivial absolute value on $\mathbb{Q}$.

**Case 1:** $\exists n > 1$ with $|n| > 1$. Let $n_0$ be smallest such integer. Write any $m$ in base $n_0$: $m = a_0 + a_1 n_0 + \cdots + a_k n_0^k$ with $0 \leq a_i < n_0$. By minimality, $|a_i| \leq 1$. Using the triangle inequality: $|m| \leq (k+1)|n_0|^k \leq C |m|_\infty^\alpha$ with $\alpha = \log_{n_0}|n_0|$. Replacing $m$ by $m^r$ and $r \to \infty$ yields $|m| = |m|_\infty^\alpha$. Thus $|\cdot|$ is equivalent to $|\cdot|_\infty$.

**Case 2:** $|n| \leq 1$ for all $n \in \mathbb{Z}$. By non-triviality, $\exists a$ with $|a| \neq 0,1$. By prime factorization, $\exists$ prime $p$ with $|p| < 1$. For any $n$ with $p \nmid n$, we claim $|n| = 1$. (If $|n| < 1$, Bezout gives $xn + yp = 1$, implying $1 = |1| = |xn+yp| \leq |x||n| + |y||p|$; a more careful argument using Lemma A.1 shows $|\cdot|$ is non-Archimedean, from which it follows that $|q|=1$ for primes $q \neq p$.) Then for $x = p^k \cdot a/b$ with $p \nmid a,b$: $|x| = |p|^k = p^{-k\alpha}$ where $\alpha = -\log_p|p| > 0$, so $|\cdot|$ is equivalent to $|\cdot|_p$. $\square$
</div>

### A.4 Hensel's Lemma

<div class="theorem">
<div class="label">Theorem A.4 (Hensel's Lemma)</div>
Let $f \in \mathbb{Z}_p[x]$, $a_0 \in \mathbb{Z}_p$ with $f(a_0) \equiv 0 \pmod{p}$ and $f'(a_0) \not\equiv 0 \pmod{p}$. Then $\exists! a \in \mathbb{Z}_p$ with $f(a) = 0$ and $a \equiv a_0 \pmod{p}$.
</div>

<div class="proof">
<div class="label">Proof</div>
Newton iteration: $a_{n+1} = a_n - f(a_n)/f'(a_n)$. Inductively, $f(a_n) \equiv 0 \pmod{p^{n+1}}$ and $a_{n+1} \equiv a_n \pmod{p^{n+1}}$. The sequence converges in $\mathbb{Z}_p$ to the unique root $a$. Uniqueness follows from $f'(a) \not\equiv 0 \pmod{p}$ preventing bifurcation. $\square$
</div>

### A.5 Product Formula

<div class="theorem">
<div class="label">Theorem A.5</div>
For $x \in \mathbb{Q}^\times$: $\|x\|_\infty \cdot \prod_p \|x\|_p = 1$.
</div>

<div class="proof">
<div class="label">Proof</div>
Write $x = \pm \prod p_i^{e_i}$. Then $\|x\|_\infty = \prod p_i^{e_i}$, $\|x\|_{p_i} = p_i^{-e_i}$, and $\|x\|_p = 1$ for $p \neq p_i$. Product is $1 \cdot 1 = 1$. $\square$
</div>

### A.6 Adelic Compactness

<div class="theorem">
<div class="label">Theorem A.6</div>
$\mathbb{A}_\mathbb{Q} / \Delta(\mathbb{Q})$ is compact.
</div>

<div class="proof">
<div class="label">Proof (Sketch)</div>
The fundamental domain $\mathcal{F} = [0,1) \times \prod_p \mathbb{Z}_p \subset \mathbb{A}_\mathbb{Q}$ is compact. Strong approximation (Chinese Remainder Theorem) shows every adele can be written as $r + f$ with $r \in \mathbb{Q}$ and $f \in \mathcal{F}$. Thus $\mathcal{F}$ surjects onto the quotient, making it compact. $\square$
</div>
