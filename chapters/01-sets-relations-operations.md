# Chapter 1: Sets, Relations, and Operations

> *"The beginning of wisdom is the definition of terms."* — Attributed to Socrates

## What Is a Set?

Physics describes the world. To describe the world, we need a language. The language of modern physics is mathematics. And the foundation of mathematics is the theory of **sets**.

A **set** is a collection of distinct objects. The objects in a set are called its **elements** or **members**. This is not a formal definition — that would require axiomatic set theory, a fascinating but separate topic. For our purposes, the intuitive idea of a collection is sufficient.

Some examples of sets:

- The set of all planets in our solar system: {Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune}
- The set of prime numbers less than 20: {2, 3, 5, 7, 11, 13, 17, 19}
- The set of all electrons in the universe
- The set containing only the number zero: {0}
- The empty set, containing nothing at all: ∅ or {}

We write $x \in A$ to mean "$x$ is an element of the set $A$." So Earth ∈ {Mercury, Venus, Earth, ...} is true, and Pluto ∈ {Mercury, Venus, Earth, ...} is false (at least since 2006). We write $x \notin A$ for non-membership.

## Subsets and Equality

If every element of set $A$ is also an element of set $B$, we say $A$ is a **subset** of $B$, written $A \subseteq B$. Think of a subset as a selection from the original set. The set of terrestrial planets {Mercury, Venus, Earth, Mars} is a subset of the set of all planets. The set of even prime numbers {2} is a subset of the set of all primes.

Two sets are **equal** if they contain exactly the same elements. Formally, $A = B$ if $A \subseteq B$ and $B \subseteq A$. This is the Principle of Extensionality: a set is determined entirely by its members. There is no additional structure, no ordering, no multiplicity — just membership.

This principle has an important consequence: the set {1, 2, 3} is the same as the set {3, 1, 2}. Order does not matter. And {1, 1, 2, 3} is the same as {1, 2, 3} — repetition is irrelevant to set membership.

## Operations on Sets

Given two sets, we can combine them in three fundamental ways:

**Union.** $A \cup B$ is the set of all elements that are in $A$ **or** in $B$ (or in both). Think of pouring the contents of two boxes into one larger box.

- {1, 2, 3} ∪ {3, 4, 5} = {1, 2, 3, 4, 5}
- {cats} ∪ {dogs} = {cats, dogs}

**Intersection.** $A \cap B$ is the set of all elements that are in $A$ **and** in $B$. Think of the overlap between two circles in a Venn diagram.

- {1, 2, 3} ∩ {3, 4, 5} = {3}
- {cats, dogs} ∩ {dogs, birds} = {dogs}
- {1, 2} ∩ {3, 4} = ∅ (no overlap — they are **disjoint**)

**Difference.** $A \setminus B$ is the set of elements in $A$ that are **not** in $B$. Think of removing from $A$ everything that also belongs to $B$.

- {1, 2, 3, 4} \ {2, 4} = {1, 3}
- {mammals} \ {humans} = {all other mammals}

## Ordered Pairs

Sets are unordered. But sometimes we need order. A point in the plane is specified by an $x$-coordinate and a $y$-coordinate, and (3, 5) is very different from (5, 3). We need a mathematical object that captures this ordered relationship.

The standard construction, due to Kazimierz Kuratowski in 1921, defines the **ordered pair** $(a, b)$ as the set:

$$(a, b) = \{\{a\}, \{a, b\}\}$$

This clever construction encodes both the elements and their order using only sets. It satisfies the essential property: $(a, b) = (c, d)$ if and only if $a = c$ **and** $b = d$.

Why does this matter for physics? Because physical quantities often come in ordered relationships. Position in space requires three coordinates. An event in spacetime requires four. The state of a particle requires both its position and its momentum. Ordered pairs — and their generalization to ordered tuples — provide the mathematical structure for representing these relationships.

## Cartesian Products

Given two sets $A$ and $B$, we can form the set of **all possible ordered pairs** whose first element comes from $A$ and second from $B$. This is the **Cartesian product**:

$$A \times B = \{(a, b) \mid a \in A \text{ and } b \in B\}$$

If $A$ has $m$ elements and $B$ has $n$ elements, then $A \times B$ has $m \times n$ elements. Think of a spreadsheet: the rows are elements of $A$, the columns are elements of $B$, and each cell is an ordered pair.

**Example.** Let $A = \{1, 2\}$ and $B = \{x, y, z\}$. Then:

$$A \times B = \{(1,x), (1,y), (1,z), (2,x), (2,y), (2,z)\}$$

The Cartesian plane $\mathbb{R}^2 = \mathbb{R} \times \mathbb{R}$ is the set of all points with two real coordinates. Spacetime $\mathbb{R}^4 = \mathbb{R} \times \mathbb{R} \times \mathbb{R} \times \mathbb{R}$ is the set of all events with four coordinates. The Cartesian product is how we build multi-dimensional spaces from one-dimensional ones.

## Relations

A **relation** between sets $A$ and $B$ is simply a subset of $A \times B$ — a selection of ordered pairs. If $(a, b)$ is in the relation, we say "$a$ is related to $b$" and sometimes write $a R b$.

Relations capture connections: "is the parent of," "is heavier than," "orbits around." Physics is built on relations: the gravitational force relates masses; the electromagnetic force relates charges; the Schrödinger equation relates a quantum state at one time to the state at a later time.

## Functions

A **function** is a special kind of relation — one that is deterministic. Formally, a function $f$ from $A$ to $B$, written $f: A \to B$, is a relation where every element of $A$ appears in **exactly one** ordered pair. For each input $a \in A$, there is a unique output $b \in B$. We write $f(a) = b$.

$A$ is called the **domain** of the function — where the inputs come from. $B$ is the **codomain** — where the outputs live.

**Examples of functions:**
- $f(x) = x^2$ maps each real number to its square. Domain: $\mathbb{R}$, codomain: $\mathbb{R}_{\geq 0}$.
- The temperature at each point in a room is a function from position to degrees.
- The Schrödinger equation defines a function from an initial quantum state $\psi(0)$ to the state at a later time $\psi(t)$.

**Not all relations are functions.** The relation "is the square root of" on the real numbers relates 4 to both 2 and -2. This violates the uniqueness requirement, so it is not a function. (We fix this by restricting the codomain or choosing a branch.)

## Properties of Functions

Functions can be classified by how they map between domain and codomain.

A function is **injective** (one-to-one) if different inputs always produce different outputs: $f(a_1) = f(a_2)$ implies $a_1 = a_2$. Think of assigning each student a unique locker — no two students share a locker. The function $f(x) = x^3$ is injective on the real numbers; $f(x) = x^2$ is not (since $2^2 = (-2)^2$).

A function is **surjective** (onto) if every element of the codomain is the output of some input: for every $b \in B$, there exists $a \in A$ with $f(a) = b$. Think of every locker being assigned to at least one student. The function $f(x) = x^3$ is surjective onto $\mathbb{R}$ (every real number has a real cube root); $f(x) = e^x$ is not surjective onto $\mathbb{R}$ (it never outputs negative numbers).

A function is **bijective** if it is both injective and surjective. A bijection establishes a perfect one-to-one correspondence between the domain and codomain — every input maps to a unique output, and every output comes from a unique input.

## Binary Operations

A **binary operation** on a set $S$ is a function that takes two elements of $S$ and produces another element of $S$:

$$\star: S \times S \to S$$

We write $a \star b$ instead of $\star(a, b)$.

**Examples:**
- Addition on natural numbers: $+(3, 5) = 8$, abbreviated $3 + 5 = 8$.
- Multiplication on integers: $\times(4, 7) = 28$, abbreviated $4 \times 7 = 28$.
- Composition of rotations: applying a $90^\circ$ rotation and then a $180^\circ$ rotation yields a $270^\circ$ rotation.

Binary operations are the algebraic building blocks. They tell us how to combine things.

## Groups: The Algebra of Symmetry

A **group** is a set equipped with a binary operation that satisfies three properties:

1. **Associativity:** $(a \star b) \star c = a \star (b \star c)$ for all $a, b, c$.
2. **Identity:** There exists an element $e$ such that $e \star a = a \star e = a$ for all $a$.
3. **Inverses:** For every $a$, there exists an element $a^{-1}$ such that $a \star a^{-1} = a^{-1} \star a = e$.

Groups capture the idea of symmetry. The set of all rotations of a square — by $0^\circ$, $90^\circ$, $180^\circ$, and $270^\circ$ — forms a group under composition. The identity is the $0^\circ$ rotation (do nothing). The inverse of a $90^\circ$ rotation is a $270^\circ$ rotation (undoing it returns to the start).

If the operation is also commutative ($a \star b = b \star a$), the group is called **abelian**, after the mathematician Niels Henrik Abel. The integers under addition form an abelian group: $3 + 5 = 5 + 3$.

Groups are fundamental to physics. The Standard Model of particle physics is built on the gauge groups $\mathrm{U}(1)$, $\mathrm{SU}(2)$, and $\mathrm{SU}(3)$. The symmetries of spacetime form the Poincaré group. Conservation laws (energy, momentum, angular momentum) arise from symmetries via Noether's theorem.

## Rings and Fields

A **ring** adds a second binary operation (usually called multiplication) to an abelian group (called addition), with the requirement that multiplication is associative and the distributive laws connect the two operations: $a \cdot (b + c) = a \cdot b + a \cdot c$.

The integers $\mathbb{Z}$ form a ring under addition and multiplication. Matrix rings, polynomial rings, and function rings are all essential to physics.

A **field** is a ring where every non-zero element has a multiplicative inverse. This allows division. The rational numbers $\mathbb{Q}$, the real numbers $\mathbb{R}$, and the complex numbers $\mathbb{C}$ are all fields. Fields are where equations can be solved and calculus can be done. Quantum mechanics is built on the complex numbers. Classical physics is built on the real numbers.

## Why This Matters for Physics

You might wonder: why start a physics document with definitions about sets and functions?

Because physics, at its core, is the attempt to map the world — to assign numbers to observations, to find relations between quantities, to express those relations as functions. Every physical theory ever proposed starts with a set (the space of states), a collection of functions on that set (observables), and rules for how those functions evolve (dynamics).

The theories we build depend on the mathematical structures we choose. If we choose the real numbers as our foundation, we get continuous physics, differential equations, and the familiar world of smooth manifolds. If we choose the p-adic numbers, we get something radically different: hierarchical physics, discrete geometry, and the world of ultrametric trees.

The choice of foundation is the most important decision in physics — and it is almost never questioned. This document questions it.

In the next chapter, we will look more closely at the numbers we use and discover that there is more than one way to measure their size.
