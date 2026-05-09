"""
gen_html.py
-----------
Generates index.html (the deployable site) from:
  - HeatmapFirstDraftSite.html  (template: all CSS, HTML structure, JS logic)
  - muscle_config.py            (muscle targets, display names, panel assignments)
  - exercise_db.py              (exercise list with activation coefficients)

WORKFLOW:
  - Change appearance or JS behavior  → edit HeatmapFirstDraftSite.html, then run this script
  - Change exercise data              → edit exercise_db.py or muscle_config.py, then run this script
  - Change muscle targets/names       → edit muscle_config.py, then run this script

RUN:
  python3 gen_hm_html.py

OUTPUT:
  index.html  (ready to push to GitHub Pages)
"""

import sys, re, json, os

# ── Locate project files ──────────────────────────────────────────────────────
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

TEMPLATE_PATH = os.path.join(SCRIPT_DIR, 'HeatmapFirstDraftSite.html')
OUTPUT_PATH   = os.path.join(SCRIPT_DIR, 'index.html')

# ── Import data from Python files ─────────────────────────────────────────────
try:
    from muscle_config import MUSCLE_TARGETS, MUSCLE_DISPLAY_NAMES, MUSCLE_PANEL
    from exercise_db import EXERCISES, CATEGORY_ORDER
except ImportError as e:
    print(f"ERROR: Could not import data files: {e}")
    print("Make sure gen_html.py is in the same folder as muscle_config.py and exercise_db.py")
    sys.exit(1)

# ── Serialize data for JS injection ──────────────────────────────────────────
# Exercises: strip 'notes' key to keep file size down, keep category + muscles
ex_clean = {
    name: {"cat": data["category"], "m": data["muscles"]}
    for name, data in EXERCISES.items()
}

js_muscle_targets = json.dumps(MUSCLE_TARGETS)
js_muscle_display = json.dumps(MUSCLE_DISPLAY_NAMES)
js_muscle_panel   = json.dumps(MUSCLE_PANEL)
js_category_order = json.dumps(CATEGORY_ORDER)
js_exercises      = json.dumps(ex_clean)

# ── Read template ─────────────────────────────────────────────────────────────
try:
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        html = f.read()
except FileNotFoundError:
    print(f"ERROR: Template not found at {TEMPLATE_PATH}")
    sys.exit(1)

# ── Replace data constants ────────────────────────────────────────────────────
# Each replacement targets the specific `const NAME = ...;` line in the script block.
# This uses a regex that matches from `const NAME  =` through the end of the JSON blob (`;`),
# handling both compact single-line JSON and any whitespace variations.

def replace_const(html_text, const_name, new_value_json):
    """Replace `const CONST_NAME = <anything>;` with fresh JSON."""
    pattern = rf'(const {const_name}\s*=\s*)(\{{.*?\}}|\[.*?\]);'
    result, count = re.subn(
        pattern,
        lambda m: m.group(1) + new_value_json + ';',
        html_text,
        flags=re.DOTALL
    )
    if count == 0:
        print(f"  WARNING: Could not find 'const {const_name}' in template — skipping.")
    return result

html = replace_const(html, 'MUSCLE_TARGETS',  js_muscle_targets)
html = replace_const(html, 'MUSCLE_DISPLAY',  js_muscle_display)
html = replace_const(html, 'MUSCLE_PANEL',    js_muscle_panel)
html = replace_const(html, 'CATEGORY_ORDER',  js_category_order)
html = replace_const(html, 'EXERCISES',       js_exercises)

# ── Write output ──────────────────────────────────────────────────────────────
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(html)

size_kb = len(html) // 1024
print(f"Generated: index.html ({size_kb} KB)")
print(f"  Exercises: {len(EXERCISES)}")
print(f"  Muscles:   {len(MUSCLE_TARGETS)}")
print(f"  Template:  {TEMPLATE_PATH}")