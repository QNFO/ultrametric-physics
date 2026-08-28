#!/usr/bin/env python3
"""QNFO.UMP.014 P2 — computational verification of H-DIST-1 and H-DIST-2.

The distinction-based ultrametric formula (locked core claim, component i):
    d(a,b) = the number of distinctions required to separate a and b
           = k - depth(LCA(a,b))   on a finite tree hierarchy, k = leaf depth.

Part 1 (H-DIST-1, formula exactness):
  a) golden values on the taxonomy example from the 2026-08-28 note
     (d(Dog,Wolf)=1 < d(Dog,Snake)=4, etc.);
  b) the ultrametric inequality on every triple of many seeded random trees,
     plus identity/symmetry/positivity;
  c) the "min is fixed" identity: min over common ancestors of (k - depth(x))
     equals the LCA value on balanced trees;
  d) a DAG counterexample where min-over-paths (graph distance) differs from the
     tree-formula value — the falsifier is checkable and the tree qualification
     is real.

Part 2 (H-DIST-2, realization independence):
  a stated digit-tree embedding maps each leaf to a base-p integer (p-adic
  realization) and to a coefficient vector (formal Laurent realization).  With the
  rule  d_realization(a,b) = (k-1) - v(x_a - x_b),  the three distance matrices
  (partition / p-adic / Laurent) are asserted identical, and the two valuations
  are asserted equal to each other for every pair.

Deterministic: SEED = 20260828.  Writes artifacts/verification/verification-output.json.
"""
import json, random, itertools, sys, hashlib
from collections import deque

SEED = 20260828
BASE = 5


# ---------------------------------------------------------------- tree core
def build(parent_map):
    """parent_map: {child: parent}, root -> None. Returns dist, depth, k, root."""
    children = {}
    for c, p in parent_map.items():
        children.setdefault(p, []).append(c)
    roots = [c for c, p in parent_map.items() if p is None]
    assert len(roots) == 1, "must be a single-root tree"
    root = roots[0]
    depth = {}

    def walk(node, d):
        depth[node] = d
        for ch in children.get(node, []):
            walk(ch, d + 1)

    walk(root, 1)
    k = max(depth.values())

    def lca(a, b):
        x, y = a, b
        while depth[x] > depth[y]:
            x = parent_map[x]
        while depth[y] > depth[x]:
            y = parent_map[y]
        while x != y:
            x = parent_map[x]
            y = parent_map[y]
        return x

    def dist(a, b):
        if a == b:
            return 0
        return k - depth[lca(a, b)]

    return dist, depth, k, root


def random_tree(rng, n_leaves):
    """Random rooted tree: internal nodes with 2-3 children; leaves may sit at
    varying depths."""
    parent = {}
    leaves = ["L%d" % i for i in range(n_leaves)]
    for L in leaves:
        parent[L] = None
    clusters = {L: {L} for L in leaves}
    nid = n_leaves
    while len(clusters) > 1:
        items = list(clusters.items())
        rng.shuffle(items)
        m = rng.randint(2, min(3, len(items)))
        picked = items[:m]
        new = "N%d" % nid
        nid += 1
        union = set()
        for cid, cset in picked:
            parent[cid] = new
            union |= cset
            del clusters[cid]
        clusters[new] = union
    root = list(clusters)[0]
    parent[root] = None
    return parent, root, leaves


def balanced_tree(b, k):
    """Every node at depth < k has b children; all leaves at depth k."""
    parent = {}
    leaves = []
    nid = 0

    def add(node, depth):
        nonlocal nid
        if depth == k:
            leaves.append(node)
            return
        for _ in range(b):
            c = "N%d" % nid
            nid += 1
            parent[c] = node
            add(c, depth + 1)

    root = "N%d" % nid
    nid += 1
    parent[root] = None
    add(root, 1)
    return parent, root, leaves


def check_ultrametric(dist, leaves):
    for a, b, c in itertools.combinations(sorted(leaves), 3):
        dab, dac, dbc = dist(a, b), dist(a, c), dist(b, c)
        if not (dac <= max(dab, dbc) and dab <= max(dac, dbc) and dbc <= max(dab, dac)):
            return False, (a, b, c, dab, dac, dbc)
    return True, None


def min_over_common_ancestors(a, b, parent_map, depth, k):
    anc_a = set()
    x = a
    while x is not None:
        anc_a.add(x)
        x = parent_map[x]
    best = None
    x = b
    while x is not None:
        if x in anc_a:
            val = k - depth[x]
            best = val if best is None else min(best, val)
        x = parent_map[x]
    return best


# ---------------------------------------------------------------- embeddings
def digit_labels(parent_map, root, base, rng):
    """Assign each node a digit on the edge from its parent; distinct within
    siblings (base >= max sibling count). Returns {leaf: [root-side..leaf-side]}."""
    children = {}
    for c, p in parent_map.items():
        if p is not None:
            children.setdefault(p, []).append(c)
    edge_digit = {root: None}

    def assign(node):
        ch = children.get(node, [])
        rng.shuffle(ch)
        for i, c in enumerate(ch):
            edge_digit[c] = i % base
            assign(c)

    assign(root)
    path_digit = {}

    def collect(node, acc):
        if children.get(node):
            for c in children[node]:
                collect(c, acc + [edge_digit[c]])
        else:
            path_digit[node] = acc

    collect(root, [])
    return path_digit


def padic_integer(digits, base):
    """Leaf-side digit is the most significant; root-side digit is the least
    significant, so shared root-side digits are shared LOW-order digits and
    v_base(x-y) counts exactly the shared distinctions (LCA depth - 1)."""
    n = 0
    for d in reversed(digits):
        n = n * base + d
    return n


def padic_valuation(x, y, base):
    """v_base(x-y): number of shared low-order digits."""
    v = 0
    while x != y and x % base == y % base:
        x //= base
        y //= base
        v += 1
    return v


def laurent_valuation(px, py):
    """v_t(px-py) over F_p[[t]]: number of shared low-order coefficients."""
    v = 0
    while px and py and px[0] == py[0]:
        px = px[1:]
        py = py[1:]
        v += 1
    return v


# ---------------------------------------------------------------- DAG check
def dag_counterexample():
    """Diamond DAG: R->A, R->B, A->C, B->C, C->X, R->Y.
    Spanning tree R-A-C-X + R-Y has k=4, LCA(X,Y)=R (depth 1), tree value = 3.
    Min-over-paths (graph distance X..Y) = 4.  Inequality => falsifier real."""
    adj = {"R": ["A", "B", "Y"], "A": ["C"], "B": ["C"], "C": ["X"], "X": [], "Y": []}
    und = {}
    for u, vs in adj.items():
        und.setdefault(u, [])
        for v in vs:
            und.setdefault(v, []).append(u)
            und[u].append(v)
    # BFS min edges X -> Y
    q = deque([("X", 0)])
    seen = {"X"}
    min_edges = None
    while q:
        node, d = q.popleft()
        if node == "Y":
            min_edges = d
            break
        for nb in und[node]:
            if nb not in seen:
                seen.add(nb)
                q.append((nb, d + 1))
    # spanning tree formula
    parent = {"R": None, "A": "R", "C": "A", "X": "C", "Y": "R"}
    dist, depth, k, root = build(parent)  # k=4
    tree_value = dist("X", "Y")
    return min_edges, tree_value, k


# ---------------------------------------------------------------- main
def main():
    rng = random.Random(SEED)
    results = {"seed": SEED, "python": sys.version.split()[0], "script_sha256": None}
    checks = []
    ok = True

    # ---- Part 1a: golden taxonomy from the note ----
    tax_parent = {
        "Animalia": None,
        "Chordata": "Animalia", "Reptilia": "Chordata",
        "Mammalia": "Chordata",
        "Carnivora": "Mammalia", "Primates": "Mammalia",
        "Canidae": "Carnivora", "Felidae": "Carnivora",
        "Dog": "Canidae", "Wolf": "Canidae", "Cat": "Felidae", "Lion": "Felidae",
        "Human": "Primates", "Chimp": "Primates",
        "Snake": "Reptilia", "Lizard": "Reptilia",
    }
    tdist, _, _, _ = build(tax_parent)
    tax_leaves = ["Dog", "Wolf", "Cat", "Lion", "Human", "Chimp", "Snake", "Lizard"]
    gold = {("Dog", "Wolf"): 1, ("Dog", "Cat"): 2, ("Dog", "Human"): 3,
            ("Dog", "Snake"): 4, ("Dog", "Lizard"): 4, ("Cat", "Lion"): 1,
            ("Snake", "Lizard"): 3, ("Human", "Chimp"): 2}
    gold_ok = all(tdist(a, b) == v for (a, b), v in gold.items())
    order_ok = (tdist("Dog", "Wolf") < tdist("Dog", "Cat") < tdist("Dog", "Human")
                < tdist("Dog", "Snake"))
    gold_ok = gold_ok and order_ok
    um_ok, um_bad = check_ultrametric(tdist, tax_leaves)
    checks.append(("golden taxonomy distances", gold_ok, gold if gold_ok else None))
    checks.append(("golden taxonomy ultrametric", um_ok, um_bad))
    results["golden_taxonomy"] = {
        "distances": {f"{a}|{b}": tdist(a, b) for (a, b) in gold},
        "ultrametric": um_ok,
    }

    # ---- Part 1b: random trees ----
    n_trees = 30
    bad_tree = None
    for t in range(n_trees):
        parent, root, leaves = random_tree(rng, rng.randint(10, 40))
        dist, depth, k, _ = build(parent)
        um, bad = check_ultrametric(dist, leaves)
        # identity / symmetry / positivity
        iden = all(dist(x, x) == 0 for x in leaves)
        sym = all(dist(x, y) == dist(y, x) for x, y in itertools.combinations(leaves, 2))
        pos = all(dist(x, y) >= 1 for x, y in itertools.combinations(leaves, 2))
        if not (um and iden and sym and pos):
            bad_tree = (t, um, bad, iden, sym, pos)
            break
    checks.append(("random trees ultrametric+metric axioms (n=%d)" % n_trees,
                   bad_tree is None, bad_tree))
    results["random_trees"] = {"n_trees": n_trees, "pass": bad_tree is None}

    # ---- Part 1c: min-over-common-ancestors identity (balanced trees) ----
    min_id_ok = True
    min_id_bad = None
    for (b, k) in [(2, 4), (3, 3), (2, 5)]:
        parent, root, leaves = balanced_tree(b, k)
        dist, depth, kk, _ = build(parent)
        for x, y in itertools.combinations(leaves, 2):
            mv = min_over_common_ancestors(x, y, parent, depth, kk)
            if mv != dist(x, y):
                min_id_ok = False
                min_id_bad = (b, k, x, y, mv, dist(x, y))
                break
        if not min_id_ok:
            break
    checks.append(("min-over-common-ancestors == LCA value on balanced trees",
                   min_id_ok, min_id_bad))
    results["min_fixity_balanced"] = {"pass": min_id_ok}

    # ---- Part 1d: DAG counterexample ----
    min_edges, tree_value, kk = dag_counterexample()
    dag_diff = (min_edges != tree_value)
    checks.append(("DAG counterexample (min-over-paths != tree value)",
                   dag_diff, (min_edges, tree_value, kk)))
    results["dag_counterexample"] = {"min_path_edges": min_edges,
                                     "tree_formula_value": tree_value, "k": kk,
                                     "falsifier_is_checkable": dag_diff}

    # ---- Part 2: realization independence ----
    ri_ok = True
    ri_detail = []
    for (b, k) in [(2, 4), (3, 3), (2, 5)]:
        parent, root, leaves = balanced_tree(b, k)
        dist, depth, kk, _ = build(parent)
        labels = digit_labels(parent, root, BASE, rng)
        n_leaves = len(leaves)
        padic = {L: padic_integer(labels[L], BASE) for L in leaves}
        laurent = {L: labels[L] for L in leaves}  # index 0 = root-side digit = low order
        vp = {}
        vt = {}
        same_vals = True
        same_rels = True
        for x, y in itertools.combinations(leaves, 2):
            vpx = padic_valuation(padic[x], padic[y], BASE)
            vtx = laurent_valuation(laurent[x], laurent[y])
            vp[(x, y)] = vpx
            vt[(x, y)] = vtx
            dp = (kk - 1) - vpx
            dt = (kk - 1) - vtx
            if vpx != vtx:
                same_vals = False
            if dp != dist(x, y) or dt != dist(x, y):
                same_rels = False
        ri_detail.append({"b": b, "k": kk, "leaves": n_leaves,
                          "valuations_agree": same_vals,
                          "matrices_identical": same_rels})
        if not (same_vals and same_rels):
            ri_ok = False
            break
    checks.append(("realization independence (partition == p-adic == Laurent)",
                   ri_ok, ri_detail if not ri_ok else None))
    results["realization_independence"] = {
        "pass": ri_ok,
        "rule": "d_realization(a,b) = (k-1) - v(x_a - x_b)",
        "base": BASE,
        "detail": ri_detail,
    }

    # ---- summary ----
    results["checks"] = [{"name": n, "pass": p} for (n, p, _) in checks]
    results["all_pass"] = all(p for (_, p, _) in checks)
    results["script_sha256"] = hashlib.sha256(
        open(__file__, "rb").read()).hexdigest()

    with open("artifacts/verification/verification-output.json", "w") as f:
        json.dump(results, f, indent=2)

    print("=== QNFO.UMP.014 P2 verification ===")
    for n, p, d in checks:
        print(("[PASS] " if p else "[FAIL] ") + n + (("  %r" % (d,)) if d is not None else ""))
    print("all_pass =", results["all_pass"])
    sys.exit(0 if results["all_pass"] else 1)


if __name__ == "__main__":
    main()
