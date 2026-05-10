"""
muscle_config.py
----------------
Defines every SVG muscle path ID used in the heatmap, along with:
  - Its MAV midpoint (used ONLY as a ratio weight, not an absolute target)
  - Which SVG panel it lives on (anterior / posterior)
  - A human-readable display name

CRITICAL DESIGN NOTE:
The MAV midpoints are NOT volume targets. They are ratio weights that define how
much each muscle *should* be trained relative to every other muscle. The heatmap
normalizes each muscle's weighted stimulus against the program's own mean, so the
output always reflects internal relative balance — not whether the user hit any
absolute set count. A fully balanced program at any total volume shows all-green.
"""

# ---------------------------------------------------------------------------
# MUSCLE_TARGETS
# Key   = SVG path ID (must match exactly)
# Value = Israetel MAV midpoint, used as the ratio weight denominator
#
# For muscles without an Israetel landmark, a conservative empirical estimate
# is used. These are marked with a comment.
# ---------------------------------------------------------------------------

MUSCLE_TARGETS = {
    # --- CHEST ---
    "pectoralis_major_sternocostal": 16,   # lower/sternal chest; MAV 12-20
    "pectoralis_major_clavicular":   16,   # upper/clavicular chest; same group

    # --- BACK ---
    "latissimus_dorsi":              18,   # MAV 14-22

    # --- TRAPS (combined group MAV 12-20, midpoint 16) ---
    # !!! Making slight drop, upper traps to 14 - some don't want to train
    "trapezius_upper":               14,
    "trapezius_lower":               16,
    "rhomboids_trapezius_mid":       16,

    # --- SHOULDERS ---
    # !!! Lateral delts need to come down?
    # !!! Likely rear as well - 19 to 16
    "anterior_deltoid":               7,   # front delts; MAV 6-8
    "lateral_deltoid":               16,   # rear+side delts group; MAV 16-22
    "posterior_deltoids":            16,   # same group as lateral

    # --- ARMS ---
    "biceps_brachii":                17,   # MAV 14-20
    "brachialis":                    17,   # same group as biceps
    "triceps_long_head":             12,   # MAV 10-14
    "triceps_lateral_head":          12,   # same group as triceps

    # --- QUADS (MAV 12-18, midpoint 15) ---
    "rectus_femoris":                15,
    "vastus_lateralis":              15,
    "vastus_medialis":               15,

    # --- HAMSTRINGS (MAV 10-16, midpoint 13) ---
    "hamstrings_biceps_femoris":     13,
    "hamstrings_medial":             13,

    # --- GLUTES (MAV 4-12, midpoint 8) ---
    "gluteus_maximus":                8,
    "gluteus_medius":                 8,

    # --- CALVES (MAV 12-16, midpoint 14) ---
    # !!! Dropping gastrocnemius to 12 for slight adjustment,
    # !!! Soleus to 10 as it otherwise appears very undertrained
    "gastrocnemius":                 12,
    "soleus":                        10,

    # --- ABS (MAV 16-20, midpoint 18) ---
    # !!! Lowering to 12, feel they are currently overrequired
    "rectus_abdominis":              12,
    "external_obliques":             12,

    # --- NON-ISRAETEL PATHS (empirical estimates) ---
    # Continual work in progress on these
    "spinal_erectors":               12,   # significant indirect load in most programs
    "serratus_anterior":              8,   # primarily a pressing stabilizer
    "posterior_rotator_cuff":        10,   # underappreciated; moderate direct target
    "hip_flexors":                    5,
    "hip_adductors":                  8,
    "wrist_flexors":                  8,
    "wrist_extensors":                8,
    "tibialis_anterior":              4,
}


# ---------------------------------------------------------------------------
# MUSCLE_PANEL
# Which SVG file each path belongs to.
# ---------------------------------------------------------------------------

MUSCLE_PANEL = {
    # ANTERIOR SVG
    "biceps_brachii":                 "anterior",
    "brachialis":                     "anterior",
    "lateral_deltoid":                "anterior",
    "anterior_deltoid":               "anterior",
    "pectoralis_major_sternocostal":  "anterior",
    "pectoralis_major_clavicular":    "anterior",
    "serratus_anterior":              "anterior",
    "rectus_abdominis":               "anterior",
    "external_obliques":              "anterior",
    "hip_flexors":                    "anterior",
    "hip_adductors":                  "anterior",
    "rectus_femoris":                 "anterior",
    "vastus_lateralis":               "anterior",
    "vastus_medialis":                "anterior",
    "tibialis_anterior":              "anterior",
    "wrist_flexors":                  "anterior",

    # POSTERIOR SVG
    "trapezius_upper":                "posterior",
    "trapezius_lower":                "posterior",
    "rhomboids_trapezius_mid":        "posterior",
    "posterior_deltoids":             "posterior",
    "posterior_rotator_cuff":         "posterior",
    "latissimus_dorsi":               "posterior",
    "triceps_long_head":              "posterior",
    "triceps_lateral_head":           "posterior",
    "wrist_extensors":                "posterior",
    "spinal_erectors":                "posterior",
    "gluteus_maximus":                "posterior",
    "gluteus_medius":                 "posterior",
    "hamstrings_biceps_femoris":      "posterior",
    "hamstrings_medial":              "posterior",
    "gastrocnemius":                  "posterior",
    "soleus":                         "posterior",
}


# ---------------------------------------------------------------------------
# MUSCLE_DISPLAY_NAMES
# Human-readable labels for UI tooltip / legend use.
# ---------------------------------------------------------------------------

MUSCLE_DISPLAY_NAMES = {
    "pectoralis_major_sternocostal": "Lower Chest (Sternocostal)",
    "pectoralis_major_clavicular":   "Upper Chest (Clavicular)",
    "latissimus_dorsi":              "Lats",
    "trapezius_upper":               "Upper Traps",
    "trapezius_lower":               "Lower Traps",
    "rhomboids_trapezius_mid":       "Rhomboids / Mid Traps",
    "anterior_deltoid":              "Front Delts",
    "lateral_deltoid":               "Side Delts",
    "posterior_deltoids":            "Rear Delts",
    "biceps_brachii":                "Biceps",
    "brachialis":                    "Brachialis",
    "triceps_long_head":             "Triceps (Long Head)",
    "triceps_lateral_head":          "Triceps (Lateral Head)",
    "rectus_femoris":                "Rectus Femoris",
    "vastus_lateralis":              "Vastus Lateralis",
    "vastus_medialis":               "Vastus Medialis",
    "hamstrings_biceps_femoris":     "Hamstrings (Biceps Femoris)",
    "hamstrings_medial":             "Hamstrings (Medial)",
    "gluteus_maximus":               "Glutes (Maximus)",
    "gluteus_medius":                "Glutes (Medius)",
    "gastrocnemius":                 "Calves (Gastrocnemius)",
    "soleus":                        "Calves (Soleus)",
    "rectus_abdominis":              "Rectus Abdominis",
    "external_obliques":             "Obliques",
    "spinal_erectors":               "Spinal Erectors",
    "serratus_anterior":             "Serratus Anterior",
    "posterior_rotator_cuff":        "Rotator Cuff (Posterior)",
    "hip_flexors":                   "Hip Flexors",
    "hip_adductors":                 "Hip Adductors",
    "wrist_flexors":                 "Wrist Flexors",
    "wrist_extensors":               "Wrist Extensors",
    "tibialis_anterior":             "Tibialis Anterior",
}


# ---------------------------------------------------------------------------
# ISRAETEL_GROUP_MAPPING
# Maps each path to the named Israetel group for display/legend grouping.
# Not used in computation — purely for UI organisation.
# ---------------------------------------------------------------------------

ISRAETEL_GROUP = {
    "pectoralis_major_sternocostal": "Chest",
    "pectoralis_major_clavicular":   "Chest",
    "latissimus_dorsi":              "Back",
    "trapezius_upper":               "Traps",
    "trapezius_lower":               "Traps",
    "rhomboids_trapezius_mid":       "Traps",
    "anterior_deltoid":              "Front Delts",
    "lateral_deltoid":               "Rear+Side Delts",
    "posterior_deltoids":            "Rear+Side Delts",
    "biceps_brachii":                "Biceps",
    "brachialis":                    "Biceps",
    "triceps_long_head":             "Triceps",
    "triceps_lateral_head":          "Triceps",
    "rectus_femoris":                "Quads",
    "vastus_lateralis":              "Quads",
    "vastus_medialis":               "Quads",
    "hamstrings_biceps_femoris":     "Hamstrings",
    "hamstrings_medial":             "Hamstrings",
    "gluteus_maximus":               "Glutes",
    "gluteus_medius":                "Glutes",
    "gastrocnemius":                 "Calves",
    "soleus":                        "Calves",
    "rectus_abdominis":              "Abs",
    "external_obliques":             "Abs",
    "spinal_erectors":               "Secondary",
    "serratus_anterior":             "Secondary",
    "posterior_rotator_cuff":        "Secondary",
    "hip_flexors":                   "Secondary",
    "hip_adductors":                 "Secondary",
    "wrist_flexors":                 "Secondary",
    "wrist_extensors":               "Secondary",
    "tibialis_anterior":             "Secondary",
}