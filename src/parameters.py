def create_legends():
    """Create descriptive labels for all model variables, constants and rates.
    
    Returns:
        tuple: (state_labels, algebraic_labels, voi_label, constant_labels, rate_labels)
    """

    sizeAlgebraic = 81
    sizeStates = 29
    sizeConstants = 58
    # Initialize all legend arrays with empty strings
    state_labels = [""] * sizeStates
    algebraic_labels = [""] * sizeAlgebraic
    constant_labels = [""] * sizeConstants
    rate_labels = [""] * sizeStates
    
    # Independent variable
    voi_label = "time in component environment (second)"
    
    # Membrane constants
    MEMBRANE_CONSTANTS = {
        "R": "R in component membrane (joule_per_kilomole_kelvin)",
        "T": "T in component membrane (kelvin)",
        "F": "F in component membrane (coulomb_per_mole)",
        "C": "C in component membrane (microF)",
        "RTONF": "RTONF in component membrane (millivolt)"
    }
    
    # Current-related constants
    CURRENT_CONSTANTS = {
        "g_f": "g_f in component hyperpolarising_activated_current (microS)",
        "g_Kr": "g_Kr in component rapid_delayed_rectifier_potassium_current (microS)",
        "g_K1": "g_K1 in component time_independent_potassium_current (microS)",
        "g_b": "g_b in component background_current (microS)",
        "g_Na": "g_Na in component fast_sodium_current (microlitre_per_second)",
        "g_CaL": "g_CaL in component L_type_calcium_current (microS)",
        "g_to": "g_to in component transient_outward_potassium_current (microS)",
        "g_st": "g_st in component sustained_outward_potassium_current (microS)",
        "g_ACh_max": "g_ACh_max in component acetylcholine_sensitive_current (microS)"
    }
    
    # Concentration constants
    CONCENTRATION_CONSTANTS = {
        "Ki": "Ki in component intracellular_potassium_concentration (millimolar)",
        "Kc": "Kc in component extracellular_potassium_concentration (millimolar)",
        "Nai": "Nai in component intracellular_sodium_concentration (millimolar)",
        "Cao": "Cao in component extracellular_calcium_concentration (millimolar)",
        "Nao": "Nao in component extracellular_sodium_concentration (millimolar)"
    }
    
    # Update constant labels using predefined mapping to indices
    CONSTANT_INDICES = {
        "R": 0, "T": 1, "F": 2, "C": 3, "RTONF": 48,
        "g_f": 4, "g_Kr": 6, "g_K1": 9, "g_b": 10,
        "g_Na": 29, "g_CaL": 31, "g_to": 37, "g_st": 39,
        "g_ACh_max": 40, "Ki": 7, "Kc": 8, "Nai": 13,
        "Cao": 27, "Nao": 28
    }
    
    for name, idx in CONSTANT_INDICES.items():
        if name in MEMBRANE_CONSTANTS:
            constant_labels[idx] = MEMBRANE_CONSTANTS[name]
        elif name in CURRENT_CONSTANTS:
            constant_labels[idx] = CURRENT_CONSTANTS[name]
        elif name in CONCENTRATION_CONSTANTS:
            constant_labels[idx] = CONCENTRATION_CONSTANTS[name]
    
    # State variables organized by component
    STATE_VARS = {
        # Membrane
        "V": (0, "V in component membrane (millivolt)"),
        
        # Ion channels
        "y": (1, "y in component hyperpolarising_activated_current_y_gate (dimensionless)"),
        "paf": (2, "paf in component rapid_delayed_rectifier_potassium_current_paf_gate (dimensionless)"),
        "pas": (3, "pas in component rapid_delayed_rectifier_potassium_current_pas_gate (dimensionless)"),
        "pik": (4, "pik in component rapid_delayed_rectifier_potassium_current_pik_gate (dimensionless)"),
        "m": (6, "m in component fast_sodium_current_m_gate (dimensionless)"),
        "h1": (7, "h1 in component fast_sodium_current_h1_gate (dimensionless)"),
        "h2": (8, "h2 in component fast_sodium_current_h2_gate (dimensionless)"),
        "d": (9, "d in component L_type_calcium_current_d_gate (dimensionless)"),
        "f": (10, "f in component L_type_calcium_current_f_gate (dimensionless)"),
        "f2": (11, "f2 in component L_type_calcium_current_f2_gate (dimensionless)"),
        "r": (12, "r in component transient_outward_potassium_current_r_gate (dimensionless)"),
        "q_fast": (13, "q_fast in component transient_outward_potassium_current_qfast_gate (dimensionless)"),
        "q_slow": (14, "q_slow in component transient_outward_potassium_current_qslow_gate (dimensionless)"),
        "qa": (15, "qa in component sustained_outward_potassium_current_qa_gate (dimensionless)"),
        "qi": (16, "qi in component sustained_outward_potassium_current_qi_gate (dimensionless)"),
        "achf": (17, "achf in component acetylcholine_sensitive_current_achf_gate (dimensionless)"),
        "achs": (18, "achs in component acetylcholine_sensitive_current_achs_gate (dimensionless)"),
        
        # Calcium handling
        "Casub": (5, "Casub in component intracellular_calcium_concentration (millimolar)"),
        "Cai": (19, "Cai in component intracellular_calcium_concentration (millimolar)"),
        "Ca_up": (20, "Ca_up in component intracellular_calcium_concentration (millimolar)"),
        "Ca_rel": (21, "Ca_rel in component intracellular_calcium_concentration (millimolar)"),
        "f_TC": (22, "f_TC in component intracellular_calcium_concentration (dimensionless)"),
        "f_TMC": (23, "f_TMC in component intracellular_calcium_concentration (dimensionless)"),
        "f_TMM": (24, "f_TMM in component intracellular_calcium_concentration (dimensionless)"),
        "f_CMi": (25, "f_CMi in component intracellular_calcium_concentration (dimensionless)"),
        "f_CMs": (26, "f_CMs in component intracellular_calcium_concentration (dimensionless)"),
        "f_CQ": (27, "f_CQ in component intracellular_calcium_concentration (dimensionless)"),
        "f_CSL": (28, "f_CSL in component intracellular_calcium_concentration (dimensionless)")
    }
    
    # Update state labels and prepare rate labels
    for var_name, (idx, label) in STATE_VARS.items():
        state_labels[idx] = label
        component = label.split("component")[1].split(")")[0].strip()
        rate_labels[idx] = f"d/dt {var_name} in component {component} (dimensionless)"
    
    # Algebraic variables
    ALGEBRAIC_VARS = {
        # Currents
        "i_Na": (65, "i_Na in component fast_sodium_current (nanoA)"),
        "i_CaL": (70, "i_CaL in component L_type_calcium_current (nanoA)"),
        "i_to": (66, "i_to in component transient_outward_potassium_current (nanoA)"),
        "i_Kr": (34, "i_Kr in component rapid_delayed_rectifier_potassium_current (nanoA)"),
        "i_f": (17, "i_f in component hyperpolarising_activated_current (nanoA)"),
        "i_st": (67, "i_st in component sustained_outward_potassium_current (nanoA)"),
        "i_K1": (49, "i_K1 in component time_independent_potassium_current (nanoA)"),
        "i_NaCa": (64, "i_NaCa in component sodium_calcium_exchange_current (nanoA)"),
        "i_p": (51, "i_p in component sodium_potassium_pump (nanoA)"),
        "i_b": (50, "i_b in component background_current (nanoA)"),
        "i_ACh": (69, "i_ACh in component acetylcholine_sensitive_current (nanoA)"),
        
        # Gate variables
        "y_inf": (0, "y_inf in component hyperpolarising_activated_current_y_gate (dimensionless)"),
        "tau_y": (19, "tau_y in component hyperpolarising_activated_current_y_gate (second)"),
        # ... (other algebraic variables)
    }
    
    for var_name, (idx, label) in ALGEBRAIC_VARS.items():
        algebraic_labels[idx] = label
    
    return (STATE_VARS, algebraic_labels, voi_label, constant_labels, rate_labels)