"""
exercise_db.py
--------------
Master database of exercises and their per-muscle activation coefficients.

Coefficient values (0.0 – 1.0) are normalized EMG proxies:
  1.0 = best known stimulus for that muscle (e.g. Nordic curl for biceps femoris)
  0.0 = no meaningful activation (omitted entirely)

Sources abbreviated in comments:
  LES  = LegEMGStudies.txt
  BES  = BackEMGStudies.txt
  AES  = ArmsEMGStudies.txt
  TES  = TorsoEMGStudies.txt
  MES  = MultiGroup_and_AssortedEMGStudies.txt

Each exercise dict has:
  "category"  : string label for UI grouping
  "muscles"   : dict of { svg_path_id: coefficient }
  "notes"     : optional string with sourcing/caveats
"""

EXERCISES = {

    # ==========================================================================
    # CHEST
    # ==========================================================================

    "Barbell Bench Press (Flat)": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 1.00,  # TES: best sternocostal activator overall
            "pectoralis_major_clavicular":   0.55,
            "anterior_deltoid":              0.45,
            "triceps_long_head":             0.60,
            "triceps_lateral_head":          0.65,
            "lateral_deltoid":               0.12,
            "serratus_anterior":             0.50,  # TES: dominant stabilizer in all press
            "biceps_brachii":                0.10,
            "rectus_abdominis":              0.08,
            "external_obliques":             0.08,
        },
        "notes": "TES-1,2,6,7,11. Best flat sternocostal. Decline is marginally superior "
                 "but impractical. Grip variations shift only minor tricep/delt balance.",
    },

    "Incline Barbell Bench Press": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_clavicular":   1.00,  # TES: clavicular peaks ~30 degrees
            "pectoralis_major_sternocostal": 0.65,
            "anterior_deltoid":              0.62,  # rises sharply above 30 degrees
            "triceps_long_head":             0.50,
            "triceps_lateral_head":          0.55,
            "lateral_deltoid":               0.15,
            "serratus_anterior":             0.45,
            "biceps_brachii":                0.08,
            "rectus_abdominis":              0.08,
            "external_obliques":             0.08,
        },
        "notes": "TES-1,5,11. Optimal angle ~30-45 deg. Above 60 deg becomes shoulder press.",
    },

    "Decline Barbell Bench Press": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 1.00,  # TES-2: slightly superior to flat
            "pectoralis_major_clavicular":   0.35,
            "anterior_deltoid":              0.40,
            "triceps_long_head":             0.75,
            "triceps_lateral_head":          0.80,  # TES-11: tricep excitation maximized
            "lateral_deltoid":               0.08,
            "rectus_abdominis":              0.08,
            "external_obliques":             0.08,
        },
        "notes": "TES-2,7,11. Most sternocostal activation of bench variants per meta-analysis.",
    },

    "Smith Machine Bench Press (Flat)": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 1.00,
            "pectoralis_major_clavicular":   0.55,
            "anterior_deltoid":              0.45,
            "triceps_long_head":             0.60,
            "triceps_lateral_head":          0.65,
            "lateral_deltoid":               0.08,
            "serratus_anterior":             0.40,
            "biceps_brachii":                0.08,
            "rectus_abdominis":              0.05,
            "external_obliques":             0.05,
        },
        "notes": "Chat sumary - smith machine gives equivalent pectoralis activation, decreased lateral deltoid/stabilizer activation."
    },

    "Smith Machine Incline Bench Press": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_clavicular":   1.00,
            "pectoralis_major_sternocostal": 0.65,
            "anterior_deltoid":              0.62,
            "triceps_long_head":             0.50,
            "triceps_lateral_head":          0.55,
            "lateral_deltoid":               0.08,
            "biceps_brachii":                0.08,
            "serratus_anterior":             0.40,
            "rectus_abdominis":              0.05,
            "external_obliques":             0.05,
        },
    },

    "Dumbbell Bench Press (Flat)": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 0.90,
            "pectoralis_major_clavicular":   0.55,
            "anterior_deltoid":              0.50,
            "triceps_long_head":             0.55,
            "triceps_lateral_head":          0.60,
            "biceps_brachii":                0.10,
            "serratus_anterior":             0.45,
            "rectus_abdominis":              0.10,
            "external_obliques":             0.10,
        },
        "notes": "TES-6: bench press superior to DB fly for all groups except biceps.",
    },

    "Incline Dumbbell Bench Press": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_clavicular":   0.95,
            "pectoralis_major_sternocostal": 0.55,
            "anterior_deltoid":              0.58,
            "triceps_long_head":             0.45,
            "triceps_lateral_head":          0.50,
            "biceps_brachii":                0.10,
            "rectus_abdominis":              0.08,
            "external_obliques":             0.08,
        },
        "notes": "TES-1,5. Greater ROM at bottom vs barbell — slightly more clavicular stretch.",
    },

    "Dumbbell Fly (Flat)": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 0.85,  # TES: pec activation comparable to bench
            "pectoralis_major_clavicular":   0.60,
            "anterior_deltoid":              0.35,
            "biceps_brachii":                0.15,
            "serratus_anterior":             0.30,
        },
        "notes": "TES-6: pec activation comparable but tricep/delt contribution minimal.",
    },

    "Incline Dumbbell Fly": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_clavicular":   0.90,
            "pectoralis_major_sternocostal": 0.50,
            "anterior_deltoid":              0.40,
            "biceps_brachii":                0.15,
        },
        "notes": "Adds clavicular stretch not achievable with barbell incline.",
    },

    "Cable Crossover (Low-to-High)": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_clavicular":   0.85,
            "pectoralis_major_sternocostal": 0.65,
            "anterior_deltoid":              0.40,
            "biceps_brachii":                0.15,
            "serratus_anterior":             0.25,
        },
        "notes": "TES-8: pec on par with bench; less tricep/delt. Low anchor = upper pec bias.",
    },

    "Cable Crossover (High-to-Low)": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 0.90,
            "pectoralis_major_clavicular":   0.40,
            "anterior_deltoid":              0.30,
            "biceps_brachii":                0.10,
        },
        "notes": "High anchor = lower/sternocostal pec bias.",
    },

    "Pec Deck / Machine Fly": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 0.85,
            "pectoralis_major_clavicular":   0.65,
            "anterior_deltoid":              0.25,
        },
        "notes": "TES-8: pec on par with cable crossover; minimal tricep/delt isolation.",
    },

    "Close-Grip Bench Press": {
        "category": "Chest",
        "muscles": {
            "triceps_lateral_head":          0.95,
            "triceps_long_head":             0.85,
            "pectoralis_major_sternocostal": 0.60,
            "anterior_deltoid":              0.45,
            "rectus_abdominis":              0.05,
            "external_obliques":             0.05,
        },
        "notes": "Primarily tricep exercise with meaningful secondary chest stimulus.",
    },

    "Push-Up (Standard)": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 0.80,
            "pectoralis_major_clavicular":   0.50,
            "anterior_deltoid":              0.70,  # TES-3,4: anterior delt rises under fatigue
            "triceps_long_head":             0.50,
            "triceps_lateral_head":          0.55,
            "serratus_anterior":             0.80,  # TES-10: dominant stabilizer in push-ups
            "biceps_brachii":                0.12,
            "rectus_abdominis":              0.08,
            "external_obliques":             0.08,
        },
        "notes": "TES-3,4: chest ~equivalent to bench at equated load; more anterior delt.",
    },

    "Diamond / Tricep Push-Up": {
        "category": "Chest",
        "muscles": {
            "triceps_long_head":             0.90,
            "triceps_lateral_head":          0.90,  # AES-4: triangle push-up most effective
            "pectoralis_major_sternocostal": 0.50,
            "anterior_deltoid":              0.45,
            "serratus_anterior":             0.55,
            "biceps_brachii":                0.10,
            "rectus_abdominis":              0.08,
            "external_obliques":             0.08,
        },
        "notes": "AES-4: triangle/diamond push-ups most effective for overall tricep activation.",
    },

    "Dip (Chest-Focused)": {
        "category": "Chest",
        "muscles": {
            "pectoralis_major_sternocostal": 0.80,
            "pectoralis_major_clavicular":   0.35,
            "triceps_long_head":             0.75,
            "triceps_lateral_head":          0.80,
            "anterior_deltoid":              0.55,
            "rectus_abdominis":              0.08,
            "external_obliques":             0.08,
        },
        "notes": "Forward lean increases chest; upright lean increases tricep. This entry "
                 "assumes a moderate forward lean.",
    },

    # ==========================================================================
    # BACK
    # ==========================================================================

    "Wide-Grip Lat Pulldown": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              1.00,  # BES-1,3: greatest lat of pulldown variants
            "rhomboids_trapezius_mid":       0.55,
            "trapezius_lower":               0.40,
            "posterior_deltoids":            0.35,
            "biceps_brachii":                0.70,
            "brachialis":                    0.60,
            "posterior_rotator_cuff":        0.45,
            "serratus_anterior":             0.18,
            "wrist_extensors":               0.15,
            "wrist_flexors":                 0.10,
            "lateral_deltoid":               0.10,
        },
        "notes": "BES-1,3,5: wide-grip superior for lats; grip variation does not significantly "
                 "alter lat activation. Narrower grips shift toward posterior delt.",
    },

    "Neutral-Grip Lat Pulldown": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.95,
            "rhomboids_trapezius_mid":       0.55,
            "trapezius_lower":               0.45,
            "posterior_deltoids":            0.30,
            "biceps_brachii":                0.75,
            "brachialis":                    0.65,
            "posterior_rotator_cuff":        0.45,
            "wrist_extensors":               0.15,
            "wrist_flexors":                 0.15,
            "serratus_anterior":             0.15,
        },
        "notes": "BES-5: no significant EMG difference between grip variations for lats.",
    },

    "Pull-Up (Pronated)": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              1.00,
            "trapezius_lower":               0.65,  # BES-12: lower trap more active than chin-up
            "rhomboids_trapezius_mid":       0.60,
            "posterior_deltoids":            0.40,
            "biceps_brachii":                0.65,
            "brachialis":                    0.55,
            "posterior_rotator_cuff":        0.55,
            "spinal_erectors":               0.35,  # BES-7: higher than pulldown
            "wrist_flexors":                 0.12,
            "wrist_extensors":               0.12,
            "serratus_anterior":             0.20,
            "lateral_deltoid":               0.10,
            "rectus_abdominis":              0.10,
            "external_obliques":             0.10,
        },
        "notes": "BES-2,7,12,14. Similar lat to chin-up; notably higher lower trap and erectors.",
    },

    "Pull-Up (Neutral Grip)": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              1.00,  # closely matched to pronated; slight advantage
            "biceps_brachii":                0.75,  # higher than pronated; approaches chin-up territory
            "brachialis":                    0.65,  # neutral grip maximizes brachialis contribution
            "trapezius_lower":               0.60,
            "rhomboids_trapezius_mid":       0.60,
            "posterior_deltoids":            0.35,
            "serratus_anterior":             0.20,
            "posterior_rotator_cuff":        0.50,
            "spinal_erectors":               0.35,
            "wrist_flexors":                 0.18,
            "rectus_abdominis":              0.10,
            "external_obliques":             0.10,
        },
        "notes": "BES-5: no significant difference in lat activation across grip orientations. "
                "Neutral grip produces higher brachialis than pronated and higher brachialis "
                "than supinated; bicep sits between pronated and supinated pull-up levels. "
                "Mid trap slightly higher than wide pronated due to scapular mechanics.",
    },            

    "Chin-Up (Supinated)": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.95,
            "biceps_brachii":                0.90,  # BES-7,12: significantly higher than pull-up
            "brachialis":                    0.75,
            "pectoralis_major_sternocostal": 0.25,  # BES-12: pec more active in chin-up
            "rhomboids_trapezius_mid":       0.45,
            "trapezius_lower":               0.45,
            "spinal_erectors":               0.45,  # BES-7
            "posterior_rotator_cuff":        0.40,
            "serratus_anterior":             0.18,
            "posterior_deltoids":            0.30,
            "lateral_deltoid":               0.05,
            "wrist_flexors":                 0.20,
            "rectus_abdominis":              0.10,
            "external_obliques":             0.10,
        },
        "notes": "BES-7,12: higher bicep and erector vs pull-up; lower trap less than pull-up.",
    },

    "Seated Cable Row (Close/Neutral Grip)": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.85,
            "rhomboids_trapezius_mid":       0.90,  # BES-8,13: best mid trap of pull exercises
            "trapezius_lower":               0.60,
            "posterior_deltoids":            0.50,
            "biceps_brachii":                0.70,
            "brachialis":                    0.60,
            "posterior_rotator_cuff":        0.50,
            "wrist_flexors":                 0.20,
            "wrist_extensors":               0.15,
        },
        "notes": "BES-8,13: rhomboid/mid trap superior to pulldowns. Wide-grip shifts more "
                 "toward posterior delt.",
    },

    "Seated Cable Row (Wide/Overhand Grip)": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.80,
            "rhomboids_trapezius_mid":       0.80,
            "trapezius_lower":               0.65,
            "posterior_deltoids":            0.60,
            "biceps_brachii":                0.55,
            "brachialis":                    0.50,
            "posterior_rotator_cuff":        0.45,
            "wrist_flexors":                 0.10,
            "wrist_extensors":               0.20,
        },
        "notes": "BES-11: shoulder abduction angle shifts activation toward posterior delt.",
    },

    "Bent-Over Barbell Row": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.90,
            "rhomboids_trapezius_mid":       0.90,
            "trapezius_upper":               0.35,
            "trapezius_lower":               0.55,
            "posterior_deltoids":            0.55,
            "spinal_erectors":               0.55,
            "biceps_brachii":                0.70,
            "brachialis":                    0.60,
            "posterior_rotator_cuff":        0.50,
            "wrist_flexors":                 0.12,
            "wrist_extensors":               0.18,
            "external_obliques":             0.25,
            "rectus_abdominis":              0.15,
        },
        "notes": "BES-8,11: greatest upper and lower back activation of any rowing exercise. "
                 "Significant spinal load — erectors strongly co-activated.",
    },

    "Chest-Supported Row (Machine / DB)": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.85,
            "rhomboids_trapezius_mid":       0.85,
            "trapezius_lower":               0.55,
            "posterior_deltoids":            0.45,
            "biceps_brachii":                0.65,
            "brachialis":                    0.55,
            "posterior_rotator_cuff":        0.50,
            "wrist_flexors":                 0.15,
            "wrist_extensors":               0.10,
        },
        "notes": "BES-11: support reduces erector demand; good lat + mid trap.",
    },

    "Single-Arm Dumbbell Row": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.90,
            "rhomboids_trapezius_mid":       0.70,
            "posterior_deltoids":            0.45,
            "biceps_brachii":                0.70,
            "brachialis":                    0.60,
            "posterior_rotator_cuff":        0.50,
            "external_obliques":             0.40,  # MES-1: unilateral row increases core
            "spinal_erectors":               0.40,
            "wrist_flexors":                 0.15,
            "wrist_extensors":               0.12,
        },
        "notes": "MES-1: unilateral rows significantly increase external oblique activation.",
    },

    "Inverted Row (Bodyweight)": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.75,
            "rhomboids_trapezius_mid":       0.85,
            "trapezius_upper":               0.35,  # BES-8: high upper trap
            "posterior_deltoids":            0.50,
            "biceps_brachii":                0.70,  # BES-9: higher than suspension row
            "brachialis":                    0.60,
            "posterior_rotator_cuff":        0.45,
            "wrist_flexors":                 0.08,
            "wrist_extensors":               0.08,
        },
        "notes": "BES-8,9: high upper trap and lat; very low erector — good for erector relief.",
    },

    "T-Bar Row": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.88,
            "rhomboids_trapezius_mid":       0.85,
            "trapezius_lower":               0.50,
            "posterior_deltoids":            0.50,
            "spinal_erectors":               0.55,
            "biceps_brachii":                0.65,
            "brachialis":                    0.55,
            "posterior_rotator_cuff":        0.45,
            "wrist_flexors":                 0.18,
            "wrist_extensors":               0.12,
            "external_obliques":             0.20,
            "rectus_abdominis":              0.15,
        },
    },

    "Straight-Arm Pulldown (Cable)": {
        "category": "Back",
        "muscles": {
            "latissimus_dorsi":              0.85,
            "triceps_long_head":             0.25,
            "serratus_anterior":             0.30,
            "posterior_rotator_cuff":        0.30,
        },
        "notes": "Near-isolation of lats; minimal bicep contribution — useful for lat-mind-muscle.",
    },

    # ==========================================================================
    # SHOULDERS
    # ==========================================================================

    "Barbell Overhead Press": {
        "category": "Shoulders",
        "muscles": {
            "anterior_deltoid":              1.00,  # MES-3,4: press dominant for front delt
            "lateral_deltoid":               0.60,
            "triceps_long_head":             0.70,
            "triceps_lateral_head":          0.80,
            "serratus_anterior":             0.65,
            "trapezius_upper":               0.50,
            "spinal_erectors":               0.40,
            "trapezius_lower":               0.30,
            "posterior_rotator_cuff":        0.35,
            "rectus_abdominis":              0.15,
            "external_obliques":             0.20,
        },
        "notes": "MES-3,4: pressing movements effective only for anterior deltoid; "
                 "other portions require additional exercises.",
    },

    "Dumbbell Overhead Press": {
        "category": "Shoulders",
        "muscles": {
            "anterior_deltoid":              0.95,
            "lateral_deltoid":               0.65,
            "triceps_long_head":             0.65,
            "serratus_anterior":             0.55,
            "triceps_lateral_head":          0.75,
            "trapezius_upper":               0.45,
            "spinal_erectors":               0.40,
            "posterior_rotator_cuff":        0.35,
            "trapezius_lower":               0.25,
            "rectus_abdominis":              0.15,
            "external_obliques":             0.15,
        },
    },

    "Arnold Press": {
        "category": "Shoulders",
        "muscles": {
            "anterior_deltoid":              0.90,
            "lateral_deltoid":               0.75,
            "triceps_long_head":             0.65,
            "triceps_lateral_head":          0.70,
            "serratus_anterior":             0.55,
            "spinal_erectors":               0.40,
            "posterior_rotator_cuff":        0.35,
            "trapezius_lower":               0.25,
            "external_obliques":             0.15,
            "rectus_abdominis":              0.15,
        },
    },

    "Lateral Raise (Dumbbell)": {
        "category": "Shoulders",
        "muscles": {
            "lateral_deltoid":               1.00,  # MES-4: lateral raise best for medial delt
            "posterior_deltoids":            0.55,  # MES-4: also best posterior outside fly
            "trapezius_upper":               0.30,
        },
        "notes": "MES-4: lateral raise and OHP produce significantly more medial delt than others. "
                 "Also produces most posterior delt activation of any non-fly exercise.",
    },

    "Cable Lateral Raise": {
        "category": "Shoulders",
        "muscles": {
            "lateral_deltoid":               0.95,
            "posterior_deltoids":            0.45,
            "trapezius_upper":               0.25,
        },
    },

    "Machine Lateral Raise": {
        "category": "Shoulders",
        "muscles": {
            "lateral_deltoid":               0.90,
            "posterior_deltoids":            0.40,
        },
    },

    "Front Raise (Dumbbell / Cable)": {
        "category": "Shoulders",
        "muscles": {
            "anterior_deltoid":              0.90,
            "pectoralis_major_clavicular":   0.20,
            "lateral_deltoid":               0.15,
            "trapezius_lower":               0.10,
        },
    },

    "Rear Delt Fly (Dumbbell, Bent-Over)": {
        "category": "Shoulders",
        "muscles": {
            "posterior_deltoids":            1.00,  # MES-3,4,5: cannot be replaced by rows
            "rhomboids_trapezius_mid":       0.40,
            "trapezius_lower":               0.30,
            "posterior_rotator_cuff":        0.50,
            "spinal_erectors":               0.20,
            "external_obliques":             0.10,
        },
        "notes": "MES-3,4,5: reverse fly patterns irreplaceable for posterior delt — pulling "
                 "exercises fall far behind.",
    },

    "Reverse Pec Deck": {
        "category": "Shoulders",
        "muscles": {
            "posterior_deltoids":            1.00,  # MES-3: best single exercise for rear delt
            "rhomboids_trapezius_mid":       0.35,
            "posterior_rotator_cuff":        0.45,
        },
        "notes": "MES-3: marginally better rear delt than bent-over fly; machine stability helps.",
    },

    "Face Pull (Cable)": {
        "category": "Shoulders",
        "muscles": {
            "posterior_deltoids":            0.90,
            "posterior_rotator_cuff":        0.75,  # Reinold: best combined posterior stimulus
            "rhomboids_trapezius_mid":       0.45,
            "trapezius_lower":               0.50,
            "lateral_deltoid":               0.20,
        },
        "notes": "MES-5/Reinold: dual purpose — rear delt + rotator cuff. Excellent prehab value.",
    },

    "Cable External Rotation (90° Abduction)": {
        "category": "Shoulders",
        "muscles": {
            "posterior_rotator_cuff":        1.00,  # MES-5/Reinold: best rotator cuff activation
            "posterior_deltoids":            0.30,
        },
        "notes": "Reinold: neutral arm with anterior resistance at 90 deg abduction is optimal.",
    },

    "External Rotation (Dumbbell, Side-Lying)": {
        "category": "Shoulders",
        "muscles": {
            "posterior_rotator_cuff":        0.85,
            "posterior_deltoids":            0.20,
        },
    },

    # ==========================================================================
    # BICEPS
    # ==========================================================================

    "Barbell Curl": {
        "category": "Biceps",
        "muscles": {
            "biceps_brachii":                1.00,  # AES-1: highest bicep brachii of curl variants
            "brachialis":                    0.65,
            "wrist_flexors":                 0.30,
        },
        "notes": "AES-1: EZ-bar and barbell outperform dumbbells for brachioradialis. "
                 "Barbell favored here slightly over EZ for supination and bicep peak.",
    },

    "EZ-Bar Curl": {
        "category": "Biceps",
        "muscles": {
            "biceps_brachii":                0.95,  # AES-1: marginally favors brachioradialis
            "brachialis":                    0.65,
            "wrist_flexors":                 0.18,
            "wrist_extensors":               0.12,
        },
        "notes": "AES-1: slight wrist comfort advantage; activation essentially equal to barbell.",
    },

    "Dumbbell Curl (Supinated)": {
        "category": "Biceps",
        "muscles": {
            "biceps_brachii":                0.90,
            "brachialis":                    0.65,
            "wrist_flexors":                 0.12,
            "wrist_extensors":               0.12,
        },
        "notes": "AES-2: traditional supinated curl has highest bicep brachii of the three "
                 "curl grip types (supinated > hammer > reverse).",
    },

    "Hammer Curl": {
        "category": "Biceps",
        "muscles": {
            "biceps_brachii":                0.65,
            "brachialis":                    0.90,  # AES-2: brachialis priority in neutral grip
            "wrist_flexors":                 0.20,
        },
        "notes": "AES-2: neutral grip shifts emphasis to brachialis; bicep brachii reduced.",
    },

    "Reverse Curl (Pronated)": {
        "category": "Biceps",
        "muscles": {
            "brachialis":                    1.00,  # AES-2: dominant in pronation
            "biceps_brachii":                0.45,
            "wrist_extensors":               0.35,
        },
        "notes": "AES-2: brachialis significantly more activated than bicep in pronated grip.",
    },

    "Preacher Curl": {
        "category": "Biceps",
        "muscles": {
            "biceps_brachii":                0.95,  # AES-5: greater distal hypertrophy
            "brachialis":                    0.75,
            "wrist_flexors":                 0.25,
        },
        "notes": "AES-5: greater volume near elbow vs incline curl (possibly brachialis). "
                 "Restricts supination arc.",
    },

    "Incline Dumbbell Curl": {
        "category": "Biceps",
        "muscles": {
            "biceps_brachii":                0.90,  # AES-5: greater proximal/shoulder-end
            "brachialis":                    0.55,
            "wrist_flexors":                 0.20,
        },
        "notes": "AES-5: greater volume near shoulder — long head stretch position.",
    },

    "Concentration Curl": {
        "category": "Biceps",
        "muscles": {
            "biceps_brachii":                0.90,
            "brachialis":                    0.60,
            "wrist_flexors":                 0.20,
        },
    },

    "Cable Curl": {
        "category": "Biceps",
        "muscles": {
            "biceps_brachii":                0.90,
            "brachialis":                    0.65,
            "wrist_flexors":                 0.20,
        },
    },

    # ==========================================================================
    # TRICEPS
    # ==========================================================================

    "Cable Pushdown (Straight Bar/V-Bar)": {
        "category": "Triceps",
        "muscles": {
            "triceps_lateral_head":          1.00,  # AES-6: best lateral/medial head activator
            "triceps_long_head":             0.60,
            "wrist_extensors":               0.15,
        },
        "notes": "AES-6 (Boeckhk-Behrens): cable pushdown top activator for lateral/medial head.",
    },

    "Rope Pushdown": {
        "category": "Triceps",
        "muscles": {
            "triceps_lateral_head":          0.90,
            "triceps_long_head":             0.70,  # AES-4,6: meaningful long head difference
            "wrist_extensors":               0.08,
        },
        "notes": "AES-4,6: significant difference between heads; rope slightly favors long head "
                 "vs straight bar.",
    },

    "Overhead Tricep Extension (Cable / Dumbbell)": {
        "category": "Triceps",
        "muscles": {
            "triceps_long_head":             1.00,  # AES-3: substantially greater long head
            "triceps_lateral_head":          0.75,
            "wrist_extensors":               0.08,
        },
        "notes": "AES-3 (Maeo 2023): overhead position produces substantially greater long head "
                 "hypertrophy vs neutral. Most effective long head exercise.",
    },

    "Skull Crusher (EZ-Bar / Barbell)": {
        "category": "Triceps",
        "muscles": {
            "triceps_long_head":             0.90,
            "triceps_lateral_head":          0.85,
            "wrist_flexors":                 0.10,
            "wrist_extensors":               0.10,
        },
        "notes": "AES-4,6: good across both heads. SZ-bar slightly favored per Boeckhk-Behrens.",
    },

    "Dumbbell Kickback": {
        "category": "Triceps",
        "muscles": {
            "triceps_long_head":             0.85,  # AES-6: surprisingly high long head
            "triceps_lateral_head":          0.80,
        },
        "notes": "AES-6: kickbacks rank high for long head; useful as isolation complement.",
    },

    "Dip (Tricep-Focused / Upright)": {
        "category": "Triceps",
        "muscles": {
            "triceps_long_head":             0.90,
            "triceps_lateral_head":          0.90,  # AES-4: dips most effective for triceps
            "pectoralis_major_sternocostal": 0.55,
            "anterior_deltoid":              0.55,
            "external_obliques":             0.10,
            "rectus_abdominis":              0.10,
        },
        "notes": "AES-4: dips and diamond push-ups among most effective overall tricep activators.",
    },

    "JM Press": {
        "category": "Triceps",
        "muscles": {
            "triceps_lateral_head":          0.90,
            "triceps_long_head":             0.85,
            "pectoralis_major_sternocostal": 0.35,
            "wrist_extensors":               0.10,
            "wrist_flexors":                 0.10,
        },
    },

    # ==========================================================================
    # QUADS
    # ==========================================================================

    "Back Squat": {
        "category": "Quads",
        "muscles": {
            "vastus_lateralis":              0.90,
            "vastus_medialis":               0.85,
            "rectus_femoris":                0.80,
            "gluteus_maximus":               0.60,
            "hamstrings_biceps_femoris":     0.30,  # LES-8: only ~27% MVIC
            "hamstrings_medial":             0.30,
            "spinal_erectors":               0.45,
            "hip_adductors":                 0.35,
            "hip_flexors":                   0.15,
            "gastrocnemius":                 0.25,
            "external_obliques":             0.25, 
            "rectus_abdominis":              0.20,
            "tibialis_anterior":             0.08,
            "soleus":                        0.08,
        },
        "notes": "LES-2,8,10,13,14: heavy loads > light loads for EMG regardless of reps "
                 "(Looney 2016). VL/VM strongest quad heads; RF slightly less. "
                 "Hamstrings minimally recruited.",
    },

    "Front Squat": {
        "category": "Quads",
        "muscles": {
            "vastus_lateralis":              1.00,  # LES-10,14: marginally more quad dominant
            "vastus_medialis":               0.95,
            "rectus_femoris":                0.90,
            "gluteus_maximus":               0.50,
            "hamstrings_biceps_femoris":     0.25,
            "hamstrings_medial":             0.25,
            "spinal_erectors":               0.45,
            "hip_flexors":                   0.15,
            "gastrocnemius":                 0.25,
            "external_obliques":             0.30, 
            "rectus_abdominis":              0.25,
            "tibialis_anterior":             0.12,
            "soleus":                        0.08,
        },
        "notes": "LES-10,14: marginal quad increase; less glute vs back squat. "
                 "No difference in hamstring activation across squat types.",
    },

    "Sumo Back Squat": {
        "category": "Quads",
        "muscles": {
            "vastus_lateralis":              0.85,
            "vastus_medialis":               0.90,
            "rectus_femoris":                0.75,
            "gluteus_maximus":               0.60,
            "hip_adductors":                 0.65,  # LES-14: sumo shifts emphasis to adductors
            "hamstrings_medial":             0.30,
            "spinal_erectors":               0.45,
            "gastrocnemius":                 0.20,
            "external_obliques":             0.20,
            "rectus_abdominis":              0.10,
            "hip_flexors":                   0.12,
            "tibialis_anterior":             0.05,
            "soleus":                        0.06,
        },
        "notes": "LES-14: sumo variations considerably shift toward adductors.",
    },

    "Leg Press (Standard Foot Placement)": {
        "category": "Quads",
        "muscles": {
            "vastus_lateralis":              1.00,  # LES-1,3: highest VL/VM of any exercise
            "vastus_medialis":               1.00,
            "rectus_femoris":                0.80,
            "gluteus_maximus":               0.55,
            "gastrocnemius":                 0.25,
            "hamstrings_biceps_femoris":     0.20,
            "hamstrings_medial":             0.20,
            "hip_flexors":                   0.15,
        },
        "notes": "LES-1,3: leg press outperforms squats for VL/VM. Hamstrings and gastroc active "
                 "only near full extension. Foot placement has inconsistent minor effects.",
    },

    "Hack Squat (Machine)": {
        "category": "Quads",
        "muscles": {
            "vastus_lateralis":              0.95,
            "vastus_medialis":               0.95,
            "rectus_femoris":                0.85,
            "gluteus_maximus":               0.45,
            "gastrocnemius":                 0.20,
            "hip_flexors":                   0.20,
            "soleus":                        0.06,
        },
    },

    "Leg Extension": {
        "category": "Quads",
        "muscles": {
            "rectus_femoris":                1.00,  # LES-3: RF priority over VL/VM
            "vastus_lateralis":              0.70,
            "vastus_medialis":               0.75,
            "tibialis_anterior":             0.05,
        },
        "notes": "LES-3: leg extension > leg press for rectus femoris; opposite for VL. "
                 "Useful for filling RF gap in programs dominated by leg press.",
    },

    "Bulgarian Split Squat (Upright Trunk)": {
        "category": "Quads",
        "muscles": {
            "rectus_femoris":                0.85,
            "vastus_lateralis":              0.85,
            "vastus_medialis":               0.85,
            "gluteus_maximus":               0.60,
            "gluteus_medius":                0.55,
            "hamstrings_medial":             0.35,
            "gastrocnemius":                 0.20,
            "hip_flexors":                   0.20,
            "external_obliques":             0.15,
            "rectus_abdominis":              0.10,
            "tibialis_anterior":             0.08,
            "soleus":                        0.10,
        },
        "notes": "LES-5/Aygün-Polat: upright trunk biases quads. Stability variation shifts "
                 "relative loading — treat as well-distributed.",
    },

    "Bulgarian Split Squat (Forward Lean)": {
        "category": "Quads",
        "muscles": {
            "gluteus_maximus":               0.80,
            "hamstrings_biceps_femoris":     0.50,
            "hamstrings_medial":             0.50,
            "rectus_femoris":                0.65,
            "vastus_lateralis":              0.65,
            "vastus_medialis":               0.65,
            "gluteus_medius":                0.50,
            "gastrocnemius":                 0.20,
            "hip_flexors":                   0.15,
            "external_obliques":             0.15,
            "rectus_abdominis":              0.10,
            "tibialis_anterior":             0.08,
            "soleus":                        0.10,
        },
        "notes": "LES-5: more forward lean shifts to posterior chain.",
    },

    "Lunge (Forward)": {
        "category": "Quads",
        "muscles": {
            "rectus_femoris":                0.70,
            "vastus_lateralis":              0.70,
            "vastus_medialis":               0.65,
            "gluteus_maximus":               0.70,
            "gluteus_medius":                0.70,  # LES-13,20: lunges good for glute med
            "hamstrings_biceps_femoris":     0.25,
            "gastrocnemius":                 0.20,
            "hip_flexors":                   0.15,
            "external_obliques":             0.10,
            "rectus_abdominis":              0.10,
            "tibialis_anterior":             0.06,
            "soleus":                        0.06,
        },
        "notes": "LES-13,20: step-ups and lunges most effective for both gluteal heads.",
    },

    "Step-Up": {
        "category": "Quads",
        "muscles": {
            "gluteus_maximus":               0.80,  # LES-13: best for glutes among compounds
            "gluteus_medius":                0.80,
            "rectus_femoris":                0.60,
            "vastus_lateralis":              0.60,
            "vastus_medialis":               0.55,
            "gastrocnemius":                 0.15,
            "hip_flexors":                   0.15,
            "external_obliques":             0.10,
            "tibialis_anterior":             0.06,
            "soleus":                        0.06,
        },
        "notes": "LES-13,20: step-ups most effective for activating both gluteal heads "
                 "of multi-joint exercises.",
    },

    "Pistol Squat / Single-Leg Squat": {
        "category": "Quads",
        "muscles": {
            "rectus_femoris":                0.90,
            "vastus_lateralis":              0.90,
            "vastus_medialis":               0.90,
            "gluteus_maximus":               0.70,
            "gluteus_medius":                0.75,
            "hip_flexors":                   0.35,
            "hamstrings_medial":             0.35,
            "tibialis_anterior":             0.20,
            "gastrocnemius":                 0.15,
            "external_obliques":             0.15,
            "rectus_abdominis":              0.10,
            "soleus":                        0.15,
        },
        "notes": "LES-20: most intense and balanced distribution of single-leg options.",
    },

    "Hip Adduction Machine": {
        "category": "Glutes",
        "muscles": {
            "hip_adductors":                 1.00,  # primary target; adductor magnus/longus/brevis
            "gluteus_medius":                0.20,  # minor medial stabilizer
        },
    },

    # ==========================================================================
    # HAMSTRINGS
    # ==========================================================================

    "Romanian Deadlift (RDL)": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_medial":             0.90,
            "hamstrings_biceps_femoris":     0.80,
            "gluteus_maximus":               0.80,
            "gluteus_medius":                0.15,
            "spinal_erectors":               0.45, 
            "hip_adductors":                 0.30,
            "gastrocnemius":                 0.15,
            "external_obliques":             0.18,
            "rectus_abdominis":              0.12,
            "tibialis_anterior":             0.04,
            "soleus":                        0.04,
        },
        "notes": "LES-12,15,16: RDL consistently high for both hamstring heads and glutes. "
                 "Medial slightly favored in hip-hinge orientation (LES-19).",
    },

    "Step-RDL": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_medial":             0.95,
            "gluteus_maximus":               0.85,
            "hamstrings_biceps_femoris":     0.80,
            "spinal_erectors":               0.45,
            "gastrocnemius":                 0.15,
            "external_obliques":             0.15,
            "tibialis_anterior":             0.08,
            "rectus_abdominis":              0.05,
            "soleus":                        0.06,
        },
        "notes": "LES-16 (Coratella 2022): step-RDL superior to standard RDL for glute and "
                 "medial hamstring activation.",
    },

    "Conventional Deadlift": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_biceps_femoris":     0.80,
            "hamstrings_medial":             0.70,
            "gluteus_maximus":               0.80,
            "gluteus_medius":                0.12,
            "spinal_erectors":               0.70,
            "rectus_femoris":                0.50,
            "vastus_lateralis":              0.55,
            "wrist_flexors":                 0.45,
            "external_obliques":             0.35, 
            "hip_adductors":                 0.30,
            "rectus_abdominis":              0.25,
            "gastrocnemius":                 0.20,
            "tibialis_anterior":             0.04,
            "soleus":                        0.04,
        },
        "notes": "LES-11,15,18: maximal erector demand; BF higher than hex bar; "
                 "higher RF than RDL.",
    },

    "Hex Bar / Trap Bar Deadlift": {
        "category": "Hamstrings",
        "muscles": {
            "vastus_lateralis":              0.80,
            "vastus_medialis":               0.75,
            "gluteus_maximus":               0.80,
            "gluteus_medius":                0.12,
            "hamstrings_biceps_femoris":     0.60,  # LES-18: less BF than straight bar
            "spinal_erectors":               0.65,
            "hip_adductors":                 0.30,
            "gastrocnemius":                 0.20,
            "external_obliques":             0.08,
            "rectus_abdominis":              0.08,
            "tibialis_anterior":             0.04,
            "soleus":                        0.04,
        },
        "notes": "LES-18: quad-dominant vs straight bar due to more upright torso. "
                 "No difference in 1RM — purely mechanical.",
    },

    "Stiff-Leg Deadlift": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_biceps_femoris":     0.75,
            "hamstrings_medial":             0.70,  # LES-16: less medial than RDL
            "spinal_erectors":               0.70,
            "gluteus_maximus":               0.70,
            "gluteus_medius":                0.10,
            "gastrocnemius":                 0.15,
            "external_obliques":             0.10,
            "soleus":                        0.06,
            "tibialis_anterior":             0.05,
        },
        "notes": "LES-16: less medial hamstring activation than RDL; more erector than RDL.",
    },

    "Nordic Curl": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_biceps_femoris":     1.00,  # LES-6: highest BF of any exercise
            "hamstrings_medial":             0.85,
            "gastrocnemius":                 0.30,
        },
        "notes": "LES-6 (Llurda-Almuzara meta, 29 studies, 500+ subjects): Nordic curl produces "
                 "near-maximal biceps femoris activation. Best single hamstring exercise.",
    },

    "Lying Leg Curl": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_biceps_femoris":     0.85,
            "hamstrings_medial":             0.90,
            "gastrocnemius":                 0.35,
        },
        "notes": "LES-6,8: very high activation; ranked below Nordic but above hip-hinge "
                 "movements for hamstring isolation.",
    },

    "Seated Leg Curl": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_medial":             0.95,  # LES-6,19: knee flexion preferentially
            "hamstrings_biceps_femoris":     0.80,  # activates semitendinosus/medial
        },
        "notes": "LES-6,8,19: seated position with hip flexion more favorable for medial "
                 "hamstrings per Llurda-Almuzara and Bourne.",
    },

    "Glute-Ham Raise (GHR)": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_medial":             0.90,
            "hamstrings_biceps_femoris":     0.90,
            "gluteus_maximus":               0.50,
            "gastrocnemius":                 0.40,
        },
        "notes": "LES-12: very high across both hamstring heads; McAllister ranks RDL and GHR "
                 "as best for overall hamstring activation.",
    },

    "Good Morning": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_medial":             0.70,
            "hamstrings_biceps_femoris":     0.60,
            "spinal_erectors":               0.80,
            "gluteus_maximus":               0.55,
            "gluteus_medius":                0.15,
            "external_obliques":             0.18,
            "gastrocnemius":                 0.15,
            "hip_flexors":                   0.10,
            "tibialis_anterior":             0.05,

        },
        "notes": "LES-8: good mornings ~50% MVIC for BF — moderate, below isolation exercises.",
    },

    "Roman Chair / Back Extension": {
        "category": "Hamstrings",
        "muscles": {
            "hamstrings_biceps_femoris":     0.85,  # LES/BES-6: highest BF of hip extensions
            "gluteus_maximus":               0.60,
            "spinal_erectors":               0.70,
            "hamstrings_medial":             0.55,
        },
        "notes": "BES-6: Roman chair produces highest biceps femoris of three hip extension "
                 "exercises (vs RDL and seated back extension).",
    },

    # ==========================================================================
    # GLUTES
    # ==========================================================================

    "Barbell Hip Thrust": {
        "category": "Glutes",
        "muscles": {
            "gluteus_maximus":               1.00,  # LES-7,11,17: greatest glute max activation
            "gluteus_medius":                0.65,
            "vastus_lateralis":              0.50,  # LES-7: notably higher VL than glute bridge
            "hip_adductors":                 0.45,
            "hamstrings_biceps_femoris":     0.40,
            "hamstrings_medial":             0.35,
            "external_obliques":             0.12,
            "rectus_abdominis":              0.08,
        },
        "notes": "LES-7,11,17: consistently best glute max exercise. Kennedy: higher VL than "
                 "glute bridge; Delgado: BHT > squat but not RDL for glutes.",
    },

    "Barbell Glute Bridge": {
        "category": "Glutes",
        "muscles": {
            "gluteus_maximus":               0.95,  # LES-7: marginally higher glute max than BHT
            "gluteus_medius":                0.70,
            "hip_adductors":                 0.40,
            "hamstrings_biceps_femoris":     0.35,
            "external_obliques":             0.10,
            "rectus_abdominis":              0.06,
        },
        "notes": "LES-7 (Kennedy): glute bridge slightly higher glute max but lower VL than BHT.",
    },

    "Hip Abduction Machine": {
        "category": "Glutes",
        "muscles": {
            "gluteus_medius":                1.00,
            "gluteus_maximus":               0.20,
        },
    },

    "Cable Kickback": {
        "category": "Glutes",
        "muscles": {
            "gluteus_maximus":               0.80,
            "hamstrings_biceps_femoris":     0.30,
            "hip_adductors":                 0.20,
        },
    },

    # ==========================================================================
    # TRAPS
    # ==========================================================================

    "Barbell Shrug": {
        "category": "Traps",
        "muscles": {
            "trapezius_upper":               1.00,
            "trapezius_lower":               0.25,
            "rhomboids_trapezius_mid":       0.30,
            "spinal_erectors":               0.20,
        },
    },

    "Dumbbell Shrug": {
        "category": "Traps",
        "muscles": {
            "trapezius_upper":               0.90,
            "rhomboids_trapezius_mid":       0.25,
            "spinal_erectors":               0.15,
        },
    },

    "Rack Pull": {
        "category": "Traps",
        "muscles": {
            "trapezius_upper":               0.80,
            "spinal_erectors":               0.65,
            "rhomboids_trapezius_mid":       0.40,
            "hamstrings_biceps_femoris":     0.50,
            "gluteus_maximus":               0.55,
            "external_obliques":             0.30,
            "rectus_abdominis":              0.10,
        },
    },

    "Prone Y Raise (Cable / Band)": {
        "category": "Traps",
        "muscles": {
            "trapezius_lower":               1.00,  # BES-10: best lower trap isolation
            "posterior_rotator_cuff":        0.50,
            "rhomboids_trapezius_mid":       0.35,
            "posterior_deltoids":            0.30,
        },
        "notes": "BES-10: IYT raises are the best exercise for lower trapezius isolation.",
    },

    "Band Pull-Apart": {
        "category": "Traps",
        "muscles": {
            "posterior_deltoids":            0.60,
            "rhomboids_trapezius_mid":       0.45,
            "trapezius_lower":               0.40,
            "posterior_rotator_cuff":        0.35,
        },
    },

    # ==========================================================================
    # CALVES
    # ==========================================================================

    "Standing Calf Raise": {
        "category": "Calves",
        "muscles": {
            "gastrocnemius":                 1.00,
            "soleus":                        0.60,
            "tibialis_anterior":             0.10,
        },
        "notes": "Gastrocnemius crosses the knee; most active when knee is extended.",
    },

    "Seated Calf Raise": {
        "category": "Calves",
        "muscles": {
            "soleus":                        1.00,
            "gastrocnemius":                 0.35,
        },
        "notes": "Knee flexion neutralizes gastrocnemius — soleus dominant. Essential complement "
                 "to standing calf raise.",
    },

    "Donkey Calf Raise": {
        "category": "Calves",
        "muscles": {
            "gastrocnemius":                 0.95,
            "soleus":                        0.55,
        },
    },

    "Leg Press Calf Raise": {
        "category": "Calves",
        "muscles": {
            "gastrocnemius":                 0.85,
            "soleus":                        0.50,
        },
    },

    "Tibialis Raise (Tib Bar / Heel)": {
        "category": "Calves",
        "muscles": {
            "tibialis_anterior":             1.00,
        },
    },

    # ==========================================================================
    # ABS / CORE
    # ==========================================================================

    "Crunch": {
        "category": "Abs",
        "muscles": {
            "rectus_abdominis":              1.00,
            "external_obliques":             0.30,
            "hip_flexors":                   0.25,
        },
    },

    "Cable Crunch": {
        "category": "Abs",
        "muscles": {
            "rectus_abdominis":              1.00,
            "external_obliques":             0.35,
            "hip_flexors":                   0.20,
        },
    },

    "Hanging Leg Raise": {
        "category": "Abs",
        "muscles": {
            "rectus_abdominis":              0.90,
            "hip_flexors":                   0.85,
            "external_obliques":             0.50,
        },
    },

    "Ab Wheel Rollout": {
        "category": "Abs",
        "muscles": {
            "rectus_abdominis":              0.90,
            "external_obliques":             0.65,
            "spinal_erectors":               0.40,
        },
    },

    "Oblique Crunch": {
        "category": "Abs",
        "muscles": {
            "external_obliques":             1.00,
            "rectus_abdominis":              0.40,
        },
    },

    "Pallof Press": {
        "category": "Abs",
        "muscles": {
            "external_obliques":             0.85,
            "rectus_abdominis":              0.40,
            "spinal_erectors":               0.30,
        },
    },

    "Plank": {
        "category": "Abs",
        "muscles": {
            "rectus_abdominis":              0.60,
            "external_obliques":             0.60,
            "spinal_erectors":               0.50,
            "serratus_anterior":             0.40,
        },
    },

    "Side Plank": {
        "category": "Abs",
        "muscles": {
            "external_obliques":             0.80,
            "hip_adductors":                 0.40,
            "gluteus_medius":                0.35,
        },
    },

    "Decline Sit-Up": {
        "category": "Abs",
        "muscles": {
            "rectus_abdominis":              0.90,
            "hip_flexors":                   0.70,
            "external_obliques":             0.30,
        },
    },

    # ==========================================================================
    # FOREARMS / WRIST
    # ==========================================================================

    "Wrist Curl": {
        "category": "Forearms",
        "muscles": {
            "wrist_flexors":                 1.00,
        },
    },

    "Reverse Wrist Curl": {
        "category": "Forearms",
        "muscles": {
            "wrist_extensors":               1.00,
        },
    },

    "Farmer's Carry": {
        "category": "Forearms",
        "muscles": {
            "wrist_flexors":                 0.50,
            "wrist_extensors":               0.40,
            "trapezius_upper":               0.60,
            "spinal_erectors":               0.50,
            "external_obliques":             0.30,
            "rectus_abdominis":              0.20,
            "tibialis_anterior":             0.15,
            "soleus":                        0.15,
        },
    },

}


# ---------------------------------------------------------------------------
# CATEGORY_ORDER — for sorted display in UI
# ---------------------------------------------------------------------------

CATEGORY_ORDER = [
    "Chest", "Back", "Shoulders", "Biceps", "Triceps",
    "Quads", "Hamstrings", "Glutes", "Traps", "Calves",
    "Abs", "Forearms",
]