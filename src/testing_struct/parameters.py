from math import log
def create_legends():
    """
    Создает легенды для переменных модели электрофизиологии клетки.
    Ключи словарей соответствуют именам переменных (например, V, y, m).
    """
    # Инициализация словарей
    legend_states = {}
    legend_rates = {}
    legend_algebraic = {}
    legend_constants = {}
    legend_voi = "time in component environment (second)"

    # Определение констант
    legend_constants = {
        "R": "R in component membrane (joule_per_kilomole_kelvin)",
        "T": "T in component membrane (kelvin)",
        "F": "F in component membrane (coulomb_per_mole)",
        "C": "C in component membrane (microF)",
        "RTONF": "RTONF in component membrane (millivolt)",
        "g_f": "g_f in component hyperpolarising_activated_current (microS)",
        "ACh": "ACh in component acetylcholine_sensitive_current (millimolar)",
        "g_Kr": "g_Kr in component rapid_delayed_rectifier_potassium_current (microS)",
        "E_K": "E_K in component rapid_delayed_rectifier_potassium_current (millivolt)",
        "Ki": "Ki in component intracellular_potassium_concentration (millimolar)",
        "Kc": "Kc in component extracellular_potassium_concentration (millimolar)",
        "g_K1": "g_K1 in component time_independent_potassium_current (microS)",
        "g_b": "g_b in component background_current (microS)",
        "E_b": "E_b in component background_current (millivolt)",
        "I_p": "I_p in component sodium_potassium_pump (nanoA)",
        "Nai": "Nai in component intracellular_sodium_concentration (millimolar)",
        "kNaCa": "kNaCa in component sodium_calcium_exchange_current (nanoA)",
        "Qci": "Qci in component sodium_calcium_exchange_current (dimensionless)",
        "Qn": "Qn in component sodium_calcium_exchange_current (dimensionless)",
        "Qco": "Qco in component sodium_calcium_exchange_current (dimensionless)",
        "Kci": "Kci in component sodium_calcium_exchange_current (millimolar)",
        "K1ni": "K1ni in component sodium_calcium_exchange_current (millimolar)",
        "K2ni": "K2ni in component sodium_calcium_exchange_current (millimolar)",
        "K3ni": "K3ni in component sodium_calcium_exchange_current (millimolar)",
        "Kcni": "Kcni in component sodium_calcium_exchange_current (millimolar)",
        "K3no": "K3no in component sodium_calcium_exchange_current (millimolar)",
        "K1no": "K1no in component sodium_calcium_exchange_current (millimolar)",
        "K2no": "K2no in component sodium_calcium_exchange_current (millimolar)",
        "Kco": "Kco in component sodium_calcium_exchange_current (millimolar)",
        "Cao": "Cao in component extracellular_calcium_concentration (millimolar)",
        "Nao": "Nao in component extracellular_sodium_concentration (millimolar)",
        "g_Na": "g_Na in component fast_sodium_current (microlitre_per_second)",
        "E_Na": "E_Na in component fast_sodium_current (millivolt)",
        "delta_m": "delta_m in component fast_sodium_current_m_gate (millivolt)",
        "act_shift": "act_shift in component L_type_calcium_current_d_gate (millivolt)",
        "slope_factor_act": "slope_factor_act in component L_type_calcium_current_d_gate (millivolt)",
        "inact_shift": "inact_shift in component L_type_calcium_current_f_gate (millivolt)",
        "inact_shift_f2": "inact_shift in component L_type_calcium_current_f2_gate (millivolt)",
        "E_st": "E_st in component sustained_outward_potassium_current (millivolt)",
        "g_st": "g_st in component sustained_outward_potassium_current (microS)",
        "g_to": "g_to in component transient_outward_potassium_current (microS)",
        "g_ACh_max": "g_ACh_max in component acetylcholine_sensitive_current (microS)",
        "K_ACh": "K_ACh in component acetylcholine_sensitive_current (millimolar)",
        "alpha_achf": "alpha_achf in component acetylcholine_sensitive_current_achf_gate (per_second)",
        "alpha_achs": "alpha_achs in component acetylcholine_sensitive_current_achs_gate (per_second)",
        "V_up": "V_up in component intracellular_calcium_concentration (micrometre3)",
        "V_rel": "V_rel in component intracellular_calcium_concentration (micrometre3)",
        "V_sub": "V_sub in component intracellular_calcium_concentration (micrometre3)",
        "Vi": "Vi in component intracellular_calcium_concentration (micrometre3)",
        "V_cell": "V_cell in component intracellular_calcium_concentration (micrometre3)",
        "P_rel": "P_rel in component intracellular_calcium_concentration (per_second)",
        "K_up": "K_up in component intracellular_calcium_concentration (millimolar)",
        "tau_tr": "tau_tr in component intracellular_calcium_concentration (second)",
    }

    # Определение состояний
    legend_states = {
        "V": "V in component membrane (millivolt)",
        "y": "y in component hyperpolarising_activated_current_y_gate (dimensionless)",
        "paf": "paf in component rapid_delayed_rectifier_potassium_current_paf_gate (dimensionless)",
        "pas": "pas in component rapid_delayed_rectifier_potassium_current_pas_gate (dimensionless)",
        "pik": "pik in component rapid_delayed_rectifier_potassium_current_pik_gate (dimensionless)",
        "Casub": "Casub in component intracellular_calcium_concentration (millimolar)",
        "m": "m in component fast_sodium_current_m_gate (dimensionless)",
        "h1": "h1 in component fast_sodium_current_h1_gate (dimensionless)",
        "h2": "h2 in component fast_sodium_current_h2_gate (dimensionless)",
        "d": "d in component L_type_calcium_current_d_gate (dimensionless)",
        "f": "f in component L_type_calcium_current_f_gate (dimensionless)",
        "f2": "f2 in component L_type_calcium_current_f2_gate (dimensionless)",
        "r": "r in component transient_outward_potassium_current_r_gate (dimensionless)",
        "q_fast": "q_fast in component transient_outward_potassium_current_qfast_gate (dimensionless)",
        "q_slow": "q_slow in component transient_outward_potassium_current_qslow_gate (dimensionless)",
        "qa": "qa in component sustained_outward_potassium_current_qa_gate (dimensionless)",
        "qi": "qi in component sustained_outward_potassium_current_qi_gate (dimensionless)",
        "achf": "achf in component acetylcholine_sensitive_current_achf_gate (dimensionless)",
        "achs": "achs in component acetylcholine_sensitive_current_achs_gate (dimensionless)",
        "Cai": "Cai in component intracellular_calcium_concentration (millimolar)",
        "Ca_up": "Ca_up in component intracellular_calcium_concentration (millimolar)",
        "Ca_rel": "Ca_rel in component intracellular_calcium_concentration (millimolar)",
        "f_TC": "f_TC in component intracellular_calcium_concentration (dimensionless)",
        "f_TMC": "f_TMC in component intracellular_calcium_concentration (dimensionless)",
        "f_TMM": "f_TMM in component intracellular_calcium_concentration (dimensionless)",
        "f_CMi": "f_CMi in component intracellular_calcium_concentration (dimensionless)",
        "f_CMs": "f_CMs in component intracellular_calcium_concentration (dimensionless)",
        "f_CQ": "f_CQ in component intracellular_calcium_concentration (dimensionless)",
        "f_CSL": "f_CSL in component intracellular_calcium_concentration (dimensionless)",
    }

    # Определение скоростей изменения состояний
    legend_rates = {key: f"d/dt {description}" for key, description in legend_states.items()}

    # Определение алгебраических переменных
    legend_algebraic = {
        "i_Na": "i_Na in component fast_sodium_current (nanoA)",
        "i_CaL": "i_CaL in component L_type_calcium_current (nanoA)",
        "i_to": "i_to in component transient_outward_potassium_current (nanoA)",
        "i_Kr": "i_Kr in component rapid_delayed_rectifier_potassium_current (nanoA)",
        "i_f": "i_f in component hyperpolarising_activated_current (nanoA)",
        "i_st": "i_st in component sustained_outward_potassium_current (nanoA)",
        "i_K1": "i_K1 in component time_independent_potassium_current (nanoA)",
        "i_NaCa": "i_NaCa in component sodium_calcium_exchange_current (nanoA)",
        "i_p": "i_p in component sodium_potassium_pump (nanoA)",
        "i_b": "i_b in component background_current (nanoA)",
        "i_ACh": "i_ACh in component acetylcholine_sensitive_current (nanoA)",
        "y_inf": "y_inf in component hyperpolarising_activated_current_y_gate (dimensionless)",
        "tau_y": "tau_y in component hyperpolarising_activated_current_y_gate (second)",
        "paf_infinity": "paf_infinity in component rapid_delayed_rectifier_potassium_current_paf_gate (dimensionless)",
        "tau_paf": "tau_paf in component rapid_delayed_rectifier_potassium_current_paf_gate (second)",
        "pas_infinity": "pas_infinity in component rapid_delayed_rectifier_potassium_current_pas_gate (dimensionless)",
        "tau_pas": "tau_pas in component rapid_delayed_rectifier_potassium_current_pas_gate (second)",
        "pik_infinity": "pik_infinity in component rapid_delayed_rectifier_potassium_current_pik_gate (dimensionless)",
        "alpha_pik": "alpha_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (per_second)",
        "beta_pik": "beta_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (per_second)",
        "tau_pik": "tau_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (second)",
        "g_K1_prime": "g_K1_prime in component time_independent_potassium_current (microS)",
        "x1": "x1 in component sodium_calcium_exchange_current (dimensionless)",
        "x2": "x2 in component sodium_calcium_exchange_current (dimensionless)",
        "x3": "x3 in component sodium_calcium_exchange_current (dimensionless)",
        "x4": "x4 in component sodium_calcium_exchange_current (dimensionless)",
        "k41": "k41 in component sodium_calcium_exchange_current (dimensionless)",
        "k34": "k34 in component sodium_calcium_exchange_current (dimensionless)",
        "k23": "k23 in component sodium_calcium_exchange_current (dimensionless)",
        "k21": "k21 in component sodium_calcium_exchange_current (dimensionless)",
        "k32": "k32 in component sodium_calcium_exchange_current (dimensionless)",
        "k43": "k43 in component sodium_calcium_exchange_current (dimensionless)",
        "k12": "k12 in component sodium_calcium_exchange_current (dimensionless)",
        "k14": "k14 in component sodium_calcium_exchange_current (dimensionless)",
        "do": "do in component sodium_calcium_exchange_current (dimensionless)",
        "di": "di in component sodium_calcium_exchange_current (dimensionless)",
        "alpha_m": "alpha_m in component fast_sodium_current_m_gate (per_second)",
        "beta_m": "beta_m in component fast_sodium_current_m_gate (per_second)",
        "E0_m": "E0_m in component fast_sodium_current_m_gate (millivolt)",
        "alpha_h1": "alpha_h1 in component fast_sodium_current_h1_gate (per_second)",
        "beta_h1": "beta_h1 in component fast_sodium_current_h1_gate (per_second)",
        "h1_inf": "h1_inf in component fast_sodium_current_h1_gate (dimensionless)",
        "tau_h1": "tau_h1 in component fast_sodium_current_h1_gate (second)",
        "alpha_h2": "alpha_h2 in component fast_sodium_current_h2_gate (per_second)",
        "beta_h2": "beta_h2 in component fast_sodium_current_h2_gate (per_second)",
        "h2_inf": "h2_inf in component fast_sodium_current_h2_gate (dimensionless)",
        "tau_h2": "tau_h2 in component fast_sodium_current_h2_gate (second)",
        "alpha_d": "alpha_d in component L_type_calcium_current_d_gate (per_second)",
        "beta_d": "beta_d in component L_type_calcium_current_d_gate (per_second)",
        "d_inf": "d_inf in component L_type_calcium_current_d_gate (dimensionless)",
        "tau_d": "tau_d in component L_type_calcium_current_d_gate (second)",
        "f_inf": "f_inf in component L_type_calcium_current_f_gate (dimensionless)",
        "tau_f": "tau_f in component L_type_calcium_current_f_gate (second)",
        "f2_inf": "f2_inf in component L_type_calcium_current_f2_gate (dimensionless)",
        "tau_f2": "tau_f2 in component L_type_calcium_current_f2_gate (second)",
        "tau_r": "tau_r in component transient_outward_potassium_current_r_gate (second)",
        "r_infinity": "r_infinity in component transient_outward_potassium_current_r_gate (dimensionless)",
        "tau_qfast": "tau_qfast in component transient_outward_potassium_current_qfast_gate (second)",
        "qfast_infinity": "qfast_infinity in component transient_outward_potassium_current_qfast_gate (dimensionless)",
        "tau_qslow": "tau_qslow in component transient_outward_potassium_current_qslow_gate (second)",
        "qslow_infinity": "qslow_infinity in component transient_outward_potassium_current_qslow_gate (dimensionless)",
        "tau_qa": "tau_qa in component sustained_outward_potassium_current_qa_gate (second)",
        "qa_infinity": "qa_infinity in component sustained_outward_potassium_current_qa_gate (dimensionless)",
        "alpha_qa": "alpha_qa in component sustained_outward_potassium_current_qa_gate (per_second)",
        "beta_qa": "beta_qa in component sustained_outward_potassium_current_qa_gate (per_second)",
        "tau_qi": "tau_qi in component sustained_outward_potassium_current_qi_gate (second)",
        "alpha_qi": "alpha_qi in component sustained_outward_potassium_current_qi_gate (per_second)",
        "beta_qi": "beta_qi in component sustained_outward_potassium_current_qi_gate (per_second)",
        "qi_infinity": "qi_infinity in component sustained_outward_potassium_current_qi_gate (dimensionless)",
        "g_ACh": "g_ACh in component acetylcholine_sensitive_current (microS)",
        "beta_achf": "beta_achf in component acetylcholine_sensitive_current_achf_gate (per_second)",
        "beta_achs": "beta_achs in component acetylcholine_sensitive_current_achs_gate (per_second)",
        "i_up": "i_up in component intracellular_calcium_concentration (millimolar_per_second)",
        "i_tr": "i_tr in component intracellular_calcium_concentration (millimolar_per_second)",
        "i_rel": "i_rel in component intracellular_calcium_concentration (millimolar_per_second)",
        "i_diff": "i_diff in component intracellular_calcium_concentration (millimolar_per_second)",
        "diff_f_TC": "diff_f_TC in component intracellular_calcium_concentration (per_second)",
        "diff_f_TMC": "diff_f_TMC in component intracellular_calcium_concentration (per_second)",
        "diff_f_TMM": "diff_f_TMM in component intracellular_calcium_concentration (per_second)",
        "diff_f_CMi": "diff_f_CMi in component intracellular_calcium_concentration (per_second)",
        "diff_f_CMs": "diff_f_CMs in component intracellular_calcium_concentration (per_second)",
        "diff_f_CQ": "diff_f_CQ in component intracellular_calcium_concentration (per_second)",
        "diff_f_CSL": "diff_f_CSL in component intracellular_calcium_concentration (per_second)",
    }

    return legend_states, legend_algebraic, legend_voi, legend_constants


def init_consts():
    """
    Инициализация констант и состояний модели.
    Возвращает два словаря: states (состояния) и constants (константы).
    """
    # Инициализация констант
    constants = {
        "R": 8314.472,          # Универсальная газовая постоянная (J/(mol*K))
        "T": 310,               # Температура (K)
        "F": 96485.3415,        # Число Фарадея (C/mol)
        "Cm": 4e-5,             # Емкость мембраны (F)
        "V_cell": 0.001,        # Объем клетки (L)
        "Na_o": 140,            # Наружная концентрация Na+ (mM)
        "K_o": 5.4,             # Наружная концентрация K+ (mM)
        "Ca_o": 2,              # Наружная концентрация Ca2+ (mM)
        "Na_i": 10,             # Внутренняя концентрация Na+ (mM)
        "K_i": 140,             # Внутренняя концентрация K+ (mM)
        "Ca_i": 0.0001,         # Внутренняя концентрация Ca2+ (mM)
        "Km_Ca": 0.0005,        # Константа Михаэлиса для Ca2+ (mM)
        "P_NaC": 3.18872e-6,    # Проницаемость Na+/Ca2+ обменника
        "g_Na_factor": 0.0116,  # Коэффициент для g_NaC
        "g_K_factor": 0.0012,   # Коэффициент для g_K
        "g_Ca_factor": 0.01,    # Коэффициент для g_Ca
    }

    # Инициализация состояний
    states = {
        "V": -49.7094187908202,  # Мембранный потенциал (mV)
        "m": 0.0462303183096481, # Активация Na+ каналов
        "h": 0.192515363116553,  # Инактивация Na+ каналов
        "j": 0.0797182955833868, # Инактивация Na+ каналов
        "X_kr": 0.949023698965401, # Активация быстрых K+ каналов
        "Ca_i": 0.000160310601192365, # Внутренняя концентрация Ca2+
        "f_Ca": 0.143642247226618, # Доля активных Ca2+ каналов
        "d": 0.0243210273637729, # Активация L-типа Ca2+ каналов
        "f": 0.0157156121147801, # Инактивация L-типа Ca2+ каналов
        "X_ks": 0.00179250298710316, # Активация медленных K+ каналов
        "X_to": 0.975550840189597, # Активация транзиторных K+ каналов
        "Y_to": 0.774394220125623, # Инактивация транзиторных K+ каналов
        "R_prime": 0.0296516611999521, # Временная переменная для Na+/K+ насоса
        "s": 0.899732315818241,  # Активация Na+/K+ насоса
        "r": 0.190111737767474,  # Инактивация Na+/K+ насоса
        "Nai_m": 0.476404610622697, # Внутренняя концентрация Na+ в митохондриях
        "Ki_m": 0.542303657353244, # Внутренняя концентрация K+ в митохондриях
        "Ca_m": 0.550559577208797, # Внутренняя концентрация Ca2+ в митохондриях
        "ADP_m": 0.567277036232041, # Концентрация ADP в митохондриях
        "ATP_m": 1.11092514657408, # Концентрация ATP в митохондриях
        "Pi_m": 0.296249516481577, # Концентрация неорганического фосфата в митохондриях
        "Dpsi_m": 0.0356473236675985, # Митохондриальный мембранный потенциал
        "pH_m": 0.443317425115817, # pH в митохондриях
        "G_H": 0.491718960234865, # Проводимость H+ каналов
        "G_Na": 0.0723007987059414, # Проводимость Na+ каналов
        "G_K": 0.0630771339141488, # Проводимость K+ каналов
        "G_Ca": 0.261430602900137, # Проводимость Ca2+ каналов
        "J_ANT": 4.1497704886823e-5, # Поток через ANT (аденозин-нуклеотидный транслоказ)
    }

    # Вычисление производных констант
    constants = compute_derived_constants(constants)

    return states, constants


def compute_derived_constants(constants):
    """
    Вычисляет производные константы на основе базовых значений.
    """
    # RT/F (мВ)
    constants["RT_F"] = (constants["R"] * constants["T"]) / constants["F"]

    # Равновесные потенциалы для ионов (мВ)
    constants["E_Na"] = constants["RT_F"] * log(constants["Na_o"] / constants["Na_i"])
    constants["E_K"] = constants["RT_F"] * log(constants["K_o"] / constants["K_i"])
    constants["E_Ca"] = constants["RT_F"] * log(constants["Ca_o"] / constants["Ca_i"])

    # Доля активных Ca2+ каналов
    constants["f_Ca"] = constants["Ca_i"] / (constants["Km_Ca"] + constants["Ca_i"])

    # Проводимости каналов
    constants["g_NaC"] = constants["g_Na_factor"] * constants["P_NaC"]
    constants["g_K"] = constants["g_K_factor"] * constants["P_NaC"]
    constants["g_Ca"] = constants["g_Ca_factor"] * constants["P_NaC"]

    return constants

