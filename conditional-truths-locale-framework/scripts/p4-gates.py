#!/usr/bin/env python3
"""P4 gates for QNFO.UMP.011 — scripted checks per research skill:
PANDOC-SAFE, INTERNAL-REF-1, TITLE-DUPLICATION-1, mojibake, MAP-TERRITORY.
Exit 1 on any FAIL. Usage: python scripts/p4-gates.py [path-to-paper.md]
"""
import sys, re, pathlib

PAPER = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else
    r"C:\Users\LENOVO\source\repos\QNFO\ultrametric-physics\conditional-truths-locale-framework\conditional-truths-locale-framework.md")
t = PAPER.read_text(encoding="utf-8")
failures, warnings = [], []

# --- 1. PANDOC-SAFE ---
# (a) Unicode math glyphs in prose (outside $...$)
math_glyphs = {"\u03b1", "\u03b2", "\u03b3", "\u03bb", "\u03bc", "\u03c9", "\u03bd", "\u03c0",
               "\u03c3", "\u03a3", "\u03a0", "\u0393", "\u0394", "\u0398", "\u221e", "\u22a2",
               "\u2192", "\u21a6", "\u2264", "\u2265", "\u2260", "\u2202", "\u2207", "\u2208",
               "\u2209", "\u2282", "\u2283", "\u2286", "\u2287", "\u00d7", "\u00b7", "\u221a",
               "\u2248", "\u2261", "\u2295", "\u2297", "\u2211", "\u220f", "\u2113", "\u211c",
               "\u211d", "\u2124", "\u211a", "\u2190", "\u2191", "\u2193", "\u21d2", "\u21d4",
               "\u22a5", "\u22c0", "\u22c1", "\u00ac", "\u2227", "\u2228", "\u2229", "\u222a",
               "\u2205", "\u230a", "\u230b", "\u22c5", "\u226a", "\u226b", "\u2044"}
# strip math spans, then scan residue for glyphs
residue = re.sub(r"\$\$.*?\$\$", "", t, flags=re.S)
residue = re.sub(r"\$[^$]*\$", "", residue)
for i, line in enumerate(residue.splitlines(), 1):
    for ch in line:
        if ch in math_glyphs:
            failures.append(f"PANDOC-SAFE: unicode math glyph {ch!r} (U+{ord(ch):04X}) at line {i}: {line.strip()[:80]}")
            break
# (b) bare pipes in table rows
for i, line in enumerate(t.splitlines(), 1):
    if line.strip().startswith("|"):
        failures.append(f"PANDOC-SAFE: bare-pipe table row at line {i} (pipe tables forbidden)")
        break
# (c) unbalanced $
if t.count("$") % 2 != 0:
    failures.append(f"PANDOC-SAFE: unbalanced $ count ({t.count('$')})")

# --- 2. INTERNAL-REF-1 ---
internal_patterns = [
    (r"QNFO\.UMP", "WBS code in paper"),
    (r"QNFO/", "repo path in paper"),
    (r"res/paper/|ump/paper/", "branch path in paper"),
    (r"\bWBS\b", "WBS token in paper"),
    (r"\.deepchat|deepchat", "deepchat path/tool in paper"),
    (r"\bskill\b", "skill token in paper"),
    (r"\bkaizen\b", "kaizen token in paper"),
    (r"CMD (RESEARCH|CONTINUE|EXECUTE|PUBLISH)", "CMD directive in paper"),
    (r"\bQNFO\b", "QNFO possessive/organization mention in paper (INTERNAL-REF-1)"),
    (r"artifacts/|docs/|scripts/", "internal path in paper"),
    (r"program_registry|portfolio-state|living-paper", "internal DB name in paper"),
]
for pat, label in internal_patterns:
    for m in re.finditer(pat, t):
        line_no = t[:m.start()].count("\n") + 1
        ln = t.splitlines()[line_no - 1].strip()[:90]
        failures.append(f"INTERNAL-REF-1: {label} at line {line_no}: {ln}")
        break  # one per pattern is enough to flag

# --- 3. TITLE-DUPLICATION-1 ---
m = re.search(r"^title:\s*[\"']?(.+?)[\"']?\s*$", t, re.M)
if m:
    title = m.group(1).strip()
    for i, line in enumerate(t.splitlines(), 1):
        if line.startswith("# ") and title in line:
            failures.append(f"TITLE-DUPLICATION-1: body H1 duplicates YAML title at line {i}")
            break
else:
    failures.append("TITLE-DUPLICATION-1: no YAML title found")

# --- 4. Mojibake ---
if "\ufffd" in t:
    failures.append("MOJIBAKE: U+FFFD replacement char present")
for bad in ["Ã©", "Ã¨", "â€™", "â€œ", "â€\u009d", "Ã¼", "Ã¶", "Ã¤"]:
    if bad in t:
        failures.append(f"MOJIBAKE: mojibake sequence {bad!r} present")

# --- 5. MAP-TERRITORY: TERRITORY claims need falsification conditions in same doc ---
has_register = "Falsifiability register" in t and ("F1" in t and "F3" in t)
if not has_register:
    failures.append("MAP-TERRITORY: no falsifiability register (F1-F4) found")

# --- 6. SO-WHAT-GATE-1 ---
if "reader should care" not in t.lower():
    failures.append("SO-WHAT-GATE-1: no reader-care statement in abstract")

print(f"P4 gates: {'PASS' if not failures else 'FAIL'}  ({len(failures)} failures)")
for f in failures:
    print("  [FAIL]", f)
for w in warnings:
    print("  [WARN]", w)
sys.exit(1 if failures else 0)
