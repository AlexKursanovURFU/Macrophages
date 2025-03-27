# Size of variable arrays:
sizeAlgebraic = 81
sizeStates = 29
sizeConstants = 58
from math import *
from numpy import *

def createLegends():
    legend_states = [""] * sizeStates
    legend_rates = [""] * sizeStates
    legend_algebraic = [""] * sizeAlgebraic
    legend_voi = ""
    legend_constants = [""] * sizeConstants
    legend_voi = "time in component environment (second)"
    legend_states[0] = "V in component membrane (millivolt)"
    legend_constants[0] = "R in component membrane (joule_per_kilomole_kelvin)"
    legend_constants[1] = "T in component membrane (kelvin)"
    legend_constants[2] = "F in component membrane (coulomb_per_mole)"
    legend_constants[3] = "C in component membrane (microF)"
    legend_constants[48] = "RTONF in component membrane (millivolt)"
    legend_algebraic[65] = "i_Na in component fast_sodium_current (nanoA)"
    legend_algebraic[70] = "i_CaL in component L_type_calcium_current (nanoA)"
    legend_algebraic[66] = "i_to in component transient_outward_potassium_current (nanoA)"
    legend_algebraic[34] = "i_Kr in component rapid_delayed_rectifier_potassium_current (nanoA)"
    legend_algebraic[17] = "i_f in component hyperpolarising_activated_current (nanoA)"
    legend_algebraic[67] = "i_st in component sustained_outward_potassium_current (nanoA)"
    legend_algebraic[49] = "i_K1 in component time_independent_potassium_current (nanoA)"
    legend_algebraic[64] = "i_NaCa in component sodium_calcium_exchange_current (nanoA)"
    legend_algebraic[51] = "i_p in component sodium_potassium_pump (nanoA)"
    legend_algebraic[50] = "i_b in component background_current (nanoA)"
    legend_algebraic[69] = "i_ACh in component acetylcholine_sensitive_current (nanoA)"
    legend_constants[4] = "g_f in component hyperpolarising_activated_current (microS)"
    legend_constants[5] = "ACh in component acetylcholine_sensitive_current (millimolar)"
    legend_states[1] = "y in component hyperpolarising_activated_current_y_gate (dimensionless)"
    legend_algebraic[0] = "y_inf in component hyperpolarising_activated_current_y_gate (dimensionless)"
    legend_algebraic[19] = "tau_y in component hyperpolarising_activated_current_y_gate (second)"
    legend_constants[6] = "g_Kr in component rapid_delayed_rectifier_potassium_current (microS)"
    legend_constants[50] = "E_K in component rapid_delayed_rectifier_potassium_current (millivolt)"
    legend_constants[7] = "Ki in component intracellular_potassium_concentration (millimolar)"
    legend_constants[8] = "Kc in component extracellular_potassium_concentration (millimolar)"
    legend_states[2] = "paf in component rapid_delayed_rectifier_potassium_current_paf_gate (dimensionless)"
    legend_states[3] = "pas in component rapid_delayed_rectifier_potassium_current_pas_gate (dimensionless)"
    legend_states[4] = "pik in component rapid_delayed_rectifier_potassium_current_pik_gate (dimensionless)"
    legend_algebraic[1] = "paf_infinity in component rapid_delayed_rectifier_potassium_current_paf_gate (dimensionless)"
    legend_algebraic[20] = "tau_paf in component rapid_delayed_rectifier_potassium_current_paf_gate (second)"
    legend_algebraic[2] = "pas_infinity in component rapid_delayed_rectifier_potassium_current_pas_gate (dimensionless)"
    legend_algebraic[21] = "tau_pas in component rapid_delayed_rectifier_potassium_current_pas_gate (second)"
    legend_algebraic[3] = "pik_infinity in component rapid_delayed_rectifier_potassium_current_pik_gate (dimensionless)"
    legend_algebraic[22] = "alpha_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (per_second)"
    legend_algebraic[35] = "beta_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (per_second)"
    legend_algebraic[43] = "tau_pik in component rapid_delayed_rectifier_potassium_current_pik_gate (second)"
    legend_constants[9] = "g_K1 in component time_independent_potassium_current (microS)"
    legend_algebraic[42] = "g_K1_prime in component time_independent_potassium_current (microS)"
    legend_constants[10] = "g_b in component background_current (microS)"
    legend_constants[11] = "E_b in component background_current (millivolt)"
    legend_constants[12] = "I_p in component sodium_potassium_pump (nanoA)"
    legend_constants[13] = "Nai in component intracellular_sodium_concentration (millimolar)"
    legend_constants[14] = "kNaCa in component sodium_calcium_exchange_current (nanoA)"
    legend_algebraic[60] = "x1 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[61] = "x2 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[62] = "x3 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[63] = "x4 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[57] = "k41 in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[49] = "k34 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[54] = "k23 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[55] = "k21 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[53] = "k32 in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[53] = "k43 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[59] = "k12 in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[58] = "k14 in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[15] = "Qci in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[16] = "Qn in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[17] = "Qco in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[18] = "Kci in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[19] = "K1ni in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[20] = "K2ni in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[21] = "K3ni in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[22] = "Kcni in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[23] = "K3no in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[24] = "K1no in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[25] = "K2no in component sodium_calcium_exchange_current (millimolar)"
    legend_constants[26] = "Kco in component sodium_calcium_exchange_current (millimolar)"
    legend_algebraic[52] = "do in component sodium_calcium_exchange_current (dimensionless)"
    legend_algebraic[56] = "di in component sodium_calcium_exchange_current (dimensionless)"
    legend_constants[27] = "Cao in component extracellular_calcium_concentration (millimolar)"
    legend_constants[28] = "Nao in component extracellular_sodium_concentration (millimolar)"
    legend_states[5] = "Casub in component intracellular_calcium_concentration (millimolar)"
    legend_constants[29] = "g_Na in component fast_sodium_current (microlitre_per_second)"
    legend_constants[51] = "E_Na in component fast_sodium_current (millivolt)"
    legend_states[6] = "m in component fast_sodium_current_m_gate (dimensionless)"
    legend_states[7] = "h1 in component fast_sodium_current_h1_gate (dimensionless)"
    legend_states[8] = "h2 in component fast_sodium_current_h2_gate (dimensionless)"
    legend_algebraic[23] = "alpha_m in component fast_sodium_current_m_gate (per_second)"
    legend_algebraic[36] = "beta_m in component fast_sodium_current_m_gate (per_second)"
    legend_constants[30] = "delta_m in component fast_sodium_current_m_gate (millivolt)"
    legend_algebraic[4] = "E0_m in component fast_sodium_current_m_gate (millivolt)"
    legend_algebraic[5] = "alpha_h1 in component fast_sodium_current_h1_gate (per_second)"
    legend_algebraic[24] = "beta_h1 in component fast_sodium_current_h1_gate (per_second)"
    legend_algebraic[37] = "h1_inf in component fast_sodium_current_h1_gate (dimensionless)"
    legend_algebraic[44] = "tau_h1 in component fast_sodium_current_h1_gate (second)"
    legend_algebraic[6] = "alpha_h2 in component fast_sodium_current_h2_gate (per_second)"
    legend_algebraic[25] = "beta_h2 in component fast_sodium_current_h2_gate (per_second)"
    legend_algebraic[38] = "h2_inf in component fast_sodium_current_h2_gate (dimensionless)"
    legend_algebraic[45] = "tau_h2 in component fast_sodium_current_h2_gate (second)"
    legend_constants[31] = "g_CaL in component L_type_calcium_current (microS)"
    legend_constants[32] = "E_CaL in component L_type_calcium_current (millivolt)"
    legend_states[9] = "d in component L_type_calcium_current_d_gate (dimensionless)"
    legend_states[10] = "f in component L_type_calcium_current_f_gate (dimensionless)"
    legend_states[11] = "f2 in component L_type_calcium_current_f2_gate (dimensionless)"
    legend_algebraic[7] = "alpha_d in component L_type_calcium_current_d_gate (per_second)"
    legend_algebraic[26] = "beta_d in component L_type_calcium_current_d_gate (per_second)"
    legend_algebraic[39] = "d_inf in component L_type_calcium_current_d_gate (dimensionless)"
    legend_algebraic[46] = "tau_d in component L_type_calcium_current_d_gate (second)"
    legend_constants[33] = "act_shift in component L_type_calcium_current_d_gate (millivolt)"
    legend_constants[34] = "slope_factor_act in component L_type_calcium_current_d_gate (millivolt)"
    legend_algebraic[8] = "f_inf in component L_type_calcium_current_f_gate (dimensionless)"
    legend_algebraic[27] = "tau_f in component L_type_calcium_current_f_gate (second)"
    legend_constants[35] = "inact_shift in component L_type_calcium_current_f_gate (millivolt)"
    legend_algebraic[9] = "f2_inf in component L_type_calcium_current_f2_gate (dimensionless)"
    legend_algebraic[28] = "tau_f2 in component L_type_calcium_current_f2_gate (second)"
    legend_constants[36] = "inact_shift in component L_type_calcium_current_f2_gate (millivolt)"
    legend_constants[52] = "E_K in component transient_outward_potassium_current (millivolt)"
    legend_constants[37] = "g_to in component transient_outward_potassium_current (microS)"
    legend_states[12] = "r in component transient_outward_potassium_current_r_gate (dimensionless)"
    legend_states[13] = "q_fast in component transient_outward_potassium_current_qfast_gate (dimensionless)"
    legend_states[14] = "q_slow in component transient_outward_potassium_current_qslow_gate (dimensionless)"
    legend_algebraic[29] = "tau_r in component transient_outward_potassium_current_r_gate (second)"
    legend_algebraic[10] = "r_infinity in component transient_outward_potassium_current_r_gate (dimensionless)"
    legend_algebraic[30] = "tau_qfast in component transient_outward_potassium_current_qfast_gate (second)"
    legend_algebraic[11] = "qfast_infinity in component transient_outward_potassium_current_qfast_gate (dimensionless)"
    legend_algebraic[31] = "tau_qslow in component transient_outward_potassium_current_qslow_gate (second)"
    legend_algebraic[12] = "qslow_infinity in component transient_outward_potassium_current_qslow_gate (dimensionless)"
    legend_constants[38] = "E_st in component sustained_outward_potassium_current (millivolt)"
    legend_constants[39] = "g_st in component sustained_outward_potassium_current (microS)"
    legend_states[15] = "qa in component sustained_outward_potassium_current_qa_gate (dimensionless)"
    legend_states[16] = "qi in component sustained_outward_potassium_current_qi_gate (dimensionless)"
    legend_algebraic[47] = "tau_qa in component sustained_outward_potassium_current_qa_gate (second)"
    legend_algebraic[13] = "qa_infinity in component sustained_outward_potassium_current_qa_gate (dimensionless)"
    legend_algebraic[32] = "alpha_qa in component sustained_outward_potassium_current_qa_gate (per_second)"
    legend_algebraic[40] = "beta_qa in component sustained_outward_potassium_current_qa_gate (per_second)"
    legend_algebraic[48] = "tau_qi in component sustained_outward_potassium_current_qi_gate (second)"
    legend_algebraic[14] = "alpha_qi in component sustained_outward_potassium_current_qi_gate (per_second)"
    legend_algebraic[33] = "beta_qi in component sustained_outward_potassium_current_qi_gate (per_second)"
    legend_algebraic[41] = "qi_infinity in component sustained_outward_potassium_current_qi_gate (dimensionless)"
    legend_algebraic[68] = "g_ACh in component acetylcholine_sensitive_current (microS)"
    legend_constants[40] = "g_ACh_max in component acetylcholine_sensitive_current (microS)"
    legend_constants[41] = "K_ACh in component acetylcholine_sensitive_current (millimolar)"
    legend_states[17] = "achf in component acetylcholine_sensitive_current_achf_gate (dimensionless)"
    legend_states[18] = "achs in component acetylcholine_sensitive_current_achs_gate (dimensionless)"
    legend_constants[42] = "alpha_achf in component acetylcholine_sensitive_current_achf_gate (per_second)"
    legend_algebraic[15] = "beta_achf in component acetylcholine_sensitive_current_achf_gate (per_second)"
    legend_constants[43] = "alpha_achs in component acetylcholine_sensitive_current_achs_gate (per_second)"
    legend_algebraic[16] = "beta_achs in component acetylcholine_sensitive_current_achs_gate (per_second)"
    legend_states[19] = "Cai in component intracellular_calcium_concentration (millimolar)"
    legend_constants[54] = "V_up in component intracellular_calcium_concentration (micrometre3)"
    legend_constants[55] = "V_rel in component intracellular_calcium_concentration (micrometre3)"
    legend_constants[56] = "V_sub in component intracellular_calcium_concentration (micrometre3)"
    legend_constants[57] = "Vi in component intracellular_calcium_concentration (micrometre3)"
    legend_constants[44] = "V_cell in component intracellular_calcium_concentration (micrometre3)"
    legend_algebraic[72] = "i_up in component intracellular_calcium_concentration (millimolar_per_second)"
    legend_algebraic[73] = "i_tr in component intracellular_calcium_concentration (millimolar_per_second)"
    legend_algebraic[75] = "i_rel in component intracellular_calcium_concentration (millimolar_per_second)"
    legend_algebraic[71] = "i_diff in component intracellular_calcium_concentration (millimolar_per_second)"
    legend_states[20] = "Ca_up in component intracellular_calcium_concentration (millimolar)"
    legend_states[21] = "Ca_rel in component intracellular_calcium_concentration (millimolar)"
    legend_constants[45] = "P_rel in component intracellular_calcium_concentration (per_second)"
    legend_constants[46] = "K_up in component intracellular_calcium_concentration (millimolar)"
    legend_constants[47] = "tau_tr in component intracellular_calcium_concentration (second)"
    legend_states[22] = "f_TC in component intracellular_calcium_concentration (dimensionless)"
    legend_states[23] = "f_TMC in component intracellular_calcium_concentration (dimensionless)"
    legend_states[24] = "f_TMM in component intracellular_calcium_concentration (dimensionless)"
    legend_states[25] = "f_CMi in component intracellular_calcium_concentration (dimensionless)"
    legend_states[26] = "f_CMs in component intracellular_calcium_concentration (dimensionless)"
    legend_states[27] = "f_CQ in component intracellular_calcium_concentration (dimensionless)"
    legend_states[28] = "f_CSL in component intracellular_calcium_concentration (dimensionless)"
    legend_algebraic[74] = "diff_f_TC in component intracellular_calcium_concentration (per_second)"
    legend_algebraic[76] = "diff_f_TMC in component intracellular_calcium_concentration (per_second)"
    legend_algebraic[18] = "diff_f_TMM in component intracellular_calcium_concentration (per_second)"
    legend_algebraic[77] = "diff_f_CMi in component intracellular_calcium_concentration (per_second)"
    legend_algebraic[78] = "diff_f_CMs in component intracellular_calcium_concentration (per_second)"
    legend_algebraic[79] = "diff_f_CQ in component intracellular_calcium_concentration (per_second)"
    legend_algebraic[80] = "diff_f_CSL in component intracellular_calcium_concentration (per_second)"
    legend_rates[0] = "d/dt V in component membrane (millivolt)"
    legend_rates[1] = "d/dt y in component hyperpolarising_activated_current_y_gate (dimensionless)"
    legend_rates[2] = "d/dt paf in component rapid_delayed_rectifier_potassium_current_paf_gate (dimensionless)"
    legend_rates[3] = "d/dt pas in component rapid_delayed_rectifier_potassium_current_pas_gate (dimensionless)"
    legend_rates[4] = "d/dt pik in component rapid_delayed_rectifier_potassium_current_pik_gate (dimensionless)"
    legend_rates[6] = "d/dt m in component fast_sodium_current_m_gate (dimensionless)"
    legend_rates[7] = "d/dt h1 in component fast_sodium_current_h1_gate (dimensionless)"
    legend_rates[8] = "d/dt h2 in component fast_sodium_current_h2_gate (dimensionless)"
    legend_rates[9] = "d/dt d in component L_type_calcium_current_d_gate (dimensionless)"
    legend_rates[10] = "d/dt f in component L_type_calcium_current_f_gate (dimensionless)"
    legend_rates[11] = "d/dt f2 in component L_type_calcium_current_f2_gate (dimensionless)"
    legend_rates[12] = "d/dt r in component transient_outward_potassium_current_r_gate (dimensionless)"
    legend_rates[13] = "d/dt q_fast in component transient_outward_potassium_current_qfast_gate (dimensionless)"
    legend_rates[14] = "d/dt q_slow in component transient_outward_potassium_current_qslow_gate (dimensionless)"
    legend_rates[15] = "d/dt qa in component sustained_outward_potassium_current_qa_gate (dimensionless)"
    legend_rates[16] = "d/dt qi in component sustained_outward_potassium_current_qi_gate (dimensionless)"
    legend_rates[17] = "d/dt achf in component acetylcholine_sensitive_current_achf_gate (dimensionless)"
    legend_rates[18] = "d/dt achs in component acetylcholine_sensitive_current_achs_gate (dimensionless)"
    legend_rates[20] = "d/dt Ca_up in component intracellular_calcium_concentration (millimolar)"
    legend_rates[21] = "d/dt Ca_rel in component intracellular_calcium_concentration (millimolar)"
    legend_rates[19] = "d/dt Cai in component intracellular_calcium_concentration (millimolar)"
    legend_rates[5] = "d/dt Casub in component intracellular_calcium_concentration (millimolar)"
    legend_rates[22] = "d/dt f_TC in component intracellular_calcium_concentration (dimensionless)"
    legend_rates[23] = "d/dt f_TMC in component intracellular_calcium_concentration (dimensionless)"
    legend_rates[24] = "d/dt f_TMM in component intracellular_calcium_concentration (dimensionless)"
    legend_rates[25] = "d/dt f_CMi in component intracellular_calcium_concentration (dimensionless)"
    legend_rates[26] = "d/dt f_CMs in component intracellular_calcium_concentration (dimensionless)"
    legend_rates[27] = "d/dt f_CQ in component intracellular_calcium_concentration (dimensionless)"
    legend_rates[28] = "d/dt f_CSL in component intracellular_calcium_concentration (dimensionless)"
    return (legend_states, legend_algebraic, legend_voi, legend_constants)

def initConsts():
    constants = [0.0] * sizeConstants; states = [0.0] * sizeStates;
    states[0] = -49.7094187908202
    constants[0] = 8314.472
    constants[1] = 310
    constants[2] = 96485.3415
    constants[3] = 4e-5
    constants[4] = 0.001
    constants[5] = 0
    states[1] = 0.0462303183096481
    constants[6] = 0.0035
    constants[7] = 140
    constants[8] = 5.4
    states[2] = 0.192515363116553
    states[3] = 0.0797182955833868
    states[4] = 0.949023698965401
    constants[9] = 0
    constants[10] = 0.0012
    constants[11] = -22.5
    constants[12] = 0.14268
    constants[13] = 8
    constants[14] = 2.14455
    constants[15] = 0.1369
    constants[16] = 0.4315
    constants[17] = 0
    constants[18] = 0.0207
    constants[19] = 395.3
    constants[20] = 2.289
    constants[21] = 26.44
    constants[22] = 26.44
    constants[23] = 4.663
    constants[24] = 1628
    constants[25] = 561.4
    constants[26] = 3.663
    constants[27] = 2
    constants[28] = 140
    states[5] = 0.000160310601192365
    constants[29] = 0
    states[6] = 0.143642247226618
    states[7] = 0.0243210273637729
    states[8] = 0.0157156121147801
    constants[30] = 1e-5
    constants[31] = 0.009
    constants[32] = 62
    states[9] = 0.00179250298710316
    states[10] = 0.975550840189597
    states[11] = 0.774394220125623
    constants[33] = -15
    constants[34] = -5
    constants[35] = -5
    constants[36] = -5
    constants[37] = 0
    states[12] = 0.0296516611999521
    states[13] = 0.899732315818241
    states[14] = 0.190111737767474
    constants[38] = -37.4
    constants[39] = 0.0001
    states[15] = 0.476404610622697
    states[16] = 0.542303657353244
    constants[40] = 0.0198
    constants[41] = 0.00035
    states[17] = 0.550559577208797
    states[18] = 0.567277036232041
    constants[42] = 73.1
    constants[43] = 3.7
    states[19] = 0.000184969821581882
    constants[44] = 3.18872e-6
    states[20] = 1.11092514657408
    states[21] = 0.296249516481577
    constants[45] = 1500
    constants[46] = 0.0006
    constants[47] = 0.06
    states[22] = 0.0356473236675985
    states[23] = 0.443317425115817
    states[24] = 0.491718960234865
    states[25] = 0.0723007987059414
    states[26] = 0.0630771339141488
    states[27] = 0.261430602900137
    states[28] = 4.1497704886823e-5
    constants[48] = (constants[0]*constants[1])/constants[2]
    constants[49] = constants[28]/(constants[23]+constants[28])
    constants[50] = constants[48]*log(constants[8]/constants[7])
    constants[51] = constants[48]*log(constants[28]/constants[13])
    constants[52] = constants[48]*log(constants[8]/constants[7])
    constants[53] = constants[13]/(constants[21]+constants[13])
    constants[54] = 0.0116000*constants[44]
    constants[55] = 0.00120000*constants[44]
    constants[56] = 0.0100000*constants[44]
    constants[57] = 0.460000*constants[44]-constants[56]
    return (states, constants)

def computeRates(states, voi, constants):
    rates = [0.0] * sizeStates; algebraic = [0.0] * sizeAlgebraic
    algebraic[15] = 120.000/(1.00000+exp(-(states[0]+50.0000)/15.0000))
    rates[17] = constants[42]*(1.00000-states[17])-algebraic[15]*states[17]
    algebraic[16] = 5.82000/(1.00000+exp(-(states[0]+50.0000)/15.0000))
    rates[18] = constants[43]*(1.00000-states[18])-algebraic[16]*states[18]
    algebraic[18] = 2277.00*2.50000*((1.00000-states[23])-states[24])-751.000*states[24]
    rates[24] = algebraic[18]
    algebraic[0] = 1.00000/(1.00000+exp(((states[0]+83.1900)-(-7.20000*(power(constants[5], 0.690000)))/(power(1.26000e-05, 0.690000)+power(constants[5], 0.690000)))/13.5600))
    algebraic[19] = 0.250000+2.00000*exp(-(power(states[0]+70.0000, 2.00000))/500.000)
    rates[1] = (algebraic[0]-states[1])/algebraic[19]
    algebraic[1] = 1.00000/(1.00000+exp((states[0]+10.2200)/-8.50000))
    algebraic[20] = 1.00000/(17.0000*exp(0.0398000*states[0])+0.211000*exp(-0.0510000*states[0]))
    rates[2] = (algebraic[1]-states[2])/algebraic[20]
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+10.2200)/-8.50000))
    algebraic[21] = 0.335810+0.906730*exp(-(power(states[0]+10.0000, 2.00000))/988.050)
    rates[3] = (algebraic[2]-states[3])/algebraic[21]
    algebraic[8] = 1.00000/(1.00000+exp((states[0]-(-24.0000+constants[35]))/6.31000))
    algebraic[27] = 0.0100000+0.153900*exp(-(power(states[0]+40.0000, 2.00000))/185.670)
    rates[10] = (algebraic[8]-states[10])/algebraic[27]
    algebraic[9] = 1.00000/(1.00000+exp((states[0]-(-24.0000+constants[36]))/6.31000))
    algebraic[28] = 0.0600000+0.480760*2.25000*exp(-(power(states[0]--40.0000, 2.00000))/138.040)
    rates[11] = (algebraic[9]-states[11])/algebraic[28]
    algebraic[29] = 0.000596000+0.00311800/(1.03700*exp(0.0900000*(states[0]+30.6100))+0.396000*exp(-0.120000*(states[0]+23.8400)))
    algebraic[10] = 1.00000/(1.00000+exp((states[0]-7.44000)/-16.4000))
    rates[12] = (algebraic[10]-states[12])/algebraic[29]
    algebraic[30] = 0.0126600+4.72716/(1.00000+exp((states[0]+154.500)/23.9600))
    algebraic[11] = 1.00000/(1.00000+exp((states[0]+33.8000)/6.12000))
    rates[13] = (algebraic[11]-states[13])/algebraic[30]
    algebraic[31] = 0.100000+4.00000*exp(-(power(states[0]+65.0000, 2.00000))/500.000)
    algebraic[12] = 1.00000/(1.00000+exp((states[0]+33.8000)/6.12000))
    rates[14] = (algebraic[12]-states[14])/algebraic[31]
    algebraic[4] = states[0]+44.4000
    algebraic[23] = custom_piecewise([less(fabs(algebraic[4]) , constants[30]), (-460.000*-12.6730)/exp(algebraic[4]/-12.6730) , True, (-460.000*algebraic[4])/(exp(algebraic[4]/-12.6730)-1.00000)])
    algebraic[36] = 18400.0*exp(algebraic[4]/-12.6730)
    rates[6] = algebraic[23]*(1.00000-states[6])-algebraic[36]*states[6]
    algebraic[3] = (1.00000/(1.00000+exp((states[0]+4.90000)/15.1400)))*(1.00000-0.300000*exp(-(power(states[0], 2.00000))/500.000))
    algebraic[22] = 92.0100*exp(-0.0183000*states[0])
    algebraic[35] = 603.600*exp(0.00942000*states[0])
    algebraic[43] = 1.00000/(algebraic[22]+algebraic[35])
    rates[4] = (algebraic[3]-states[4])/algebraic[43]
    algebraic[5] = 44.9000*exp((states[0]+66.9000)/-5.57000)
    algebraic[24] = 1491.00/(1.00000+323.300*exp((states[0]+94.6000)/-12.9000))
    algebraic[37] = algebraic[5]/(algebraic[5]+algebraic[24])
    algebraic[44] = 0.0300000/(1.00000+exp((states[0]+40.0000)/6.00000))+0.000350000
    rates[7] = (algebraic[37]-states[7])/algebraic[44]
    algebraic[6] = 44.9000*exp((states[0]+66.9000)/-5.57000)
    algebraic[25] = 1491.00/(1.00000+323.300*exp((states[0]+94.6000)/-12.9000))
    algebraic[38] = algebraic[6]/(algebraic[6]+algebraic[25])
    algebraic[45] = 0.120000/(1.00000+exp((states[0]+60.0000)/2.00000))+0.00295000
    rates[8] = (algebraic[38]-states[8])/algebraic[45]
    algebraic[39] = 1.00000/(1.00000+exp((states[0]-(-3.20000+constants[33]))/constants[34]))
    algebraic[7] = (-26.1200*(states[0]+35.0000))/(exp((states[0]+35.0000)/-2.50000)-1.00000)+(-78.1100*states[0])/(exp(-0.208000*states[0])-1.00000)
    algebraic[26] = (10.5200*(states[0]-5.00000))/(exp(0.400000*(states[0]-5.00000))-1.00000)
    algebraic[46] = 1.00000/(algebraic[7]+algebraic[26])
    rates[9] = (algebraic[39]-states[9])/algebraic[46]
    algebraic[32] = 1.00000/(0.150000*exp(-states[0]/11.0000)+0.200000*exp(-states[0]/700.000))
    algebraic[40] = 1.00000/(16.0000*exp(states[0]/8.00000)+15.0000*exp(states[0]/50.0000))
    algebraic[47] = 0.00100000/(algebraic[32]+algebraic[40])
    algebraic[13] = 1.00000/(1.00000+exp((states[0]--49.1000)/-8.98000))
    rates[15] = (algebraic[13]-states[15])/algebraic[47]
    algebraic[14] = 0.150400/(3100.00*exp(states[0]/13.0000)+700.000*exp(states[0]/70.0000))
    algebraic[33] = 0.150400/(95.0000*exp(-states[0]/10.0000)+50.0000*exp(-states[0]/700.000))+0.000229000/(1.00000+exp(-states[0]/5.00000))
    algebraic[48] = 0.00100000/(algebraic[14]+algebraic[33])
    algebraic[41] = algebraic[14]/(algebraic[14]+algebraic[33])
    rates[16] = (algebraic[41]-states[16])/algebraic[48]
    algebraic[65] = (((constants[29]*(power(states[6], 3.00000))*(0.635000*states[7]+0.365000*states[8])*constants[28]*states[0]*constants[2])/constants[48])*(exp((states[0]-constants[51])/constants[48])-1.00000))/(exp(states[0]/constants[48])-1.00000)
    algebraic[68] = (constants[40]*states[17]*states[18]*(power(constants[5], 1.50000)))/(power(constants[41], 1.50000)+power(constants[5], 1.50000))
    algebraic[69] = (((algebraic[68]*constants[8])/(10.0000+constants[8]))*(states[0]-constants[50]))/(1.00000+exp(((states[0]-constants[50])-140.000)/(2.50000*constants[48])))
    algebraic[70] = constants[31]*states[9]*(0.675000*states[10]+0.325000*states[11])*(states[0]-constants[32])*(1.00000-((algebraic[69]*constants[5])/(9.00000e-05+constants[5]))/1.00000)
    algebraic[66] = constants[37]*states[12]*(0.450000*states[13]+0.550000*states[14])*(states[0]-constants[52])
    algebraic[34] = constants[6]*(0.900000*states[2]+0.100000*states[3])*states[4]*(states[0]-constants[50])
    algebraic[17] = states[1]*constants[4]*(states[0]--30.0000)
    algebraic[67] = constants[39]*states[15]*states[16]*(states[0]-constants[38])
    algebraic[42] = constants[9]*(0.500000+0.500000/(1.00000+exp((states[0]+30.0000)/5.00000)))
    algebraic[49] = (algebraic[42]*(power(constants[8]/(constants[8]+0.590000), 3.00000))*(states[0]+81.9000))/(1.00000+exp((1.39300*(states[0]+81.9000+3.60000))/constants[48]))
    algebraic[57] = exp((-constants[16]*states[0])/(2.00000*constants[48]))
    algebraic[52] = 1.00000+(constants[27]/constants[26])*(1.00000+exp((constants[17]*states[0])/constants[48]))+constants[28]/constants[24]+(power(constants[28], 2.00000))/(constants[24]*constants[25])+(power(constants[28], 3.00000))/(constants[24]*constants[25]*constants[23])
    algebraic[54] = (((power(constants[28], 2.00000))/(constants[24]*constants[25])+(power(constants[28], 3.00000))/(constants[24]*constants[25]*constants[23]))*exp((-constants[16]*states[0])/(2.00000*constants[48])))/algebraic[52]
    algebraic[55] = ((constants[27]/constants[26])*exp((-constants[17]*states[0])/constants[48]))/algebraic[52]
    algebraic[53] = exp((constants[16]*states[0])/(2.00000*constants[48]))
    algebraic[60] = algebraic[57]*constants[49]*(algebraic[54]+algebraic[55])+algebraic[55]*algebraic[53]*(constants[53]+algebraic[57])
    algebraic[56] = 1.00000+(states[5]/constants[18])*(1.00000+exp((-constants[15]*states[0])/constants[48])+constants[13]/constants[22])+constants[13]/constants[19]+(power(constants[13], 2.00000))/(constants[19]*constants[20])+(power(constants[13], 3.00000))/(constants[19]*constants[20]*constants[21])
    algebraic[59] = ((states[5]/constants[18])*exp((-constants[15]*states[0])/constants[48]))/algebraic[56]
    algebraic[58] = (((power(constants[13], 2.00000))/(constants[19]*constants[20])+(power(constants[13], 3.00000))/(constants[19]*constants[20]*constants[21]))*exp((constants[16]*states[0])/(2.00000*constants[48])))/algebraic[56]
    algebraic[61] = algebraic[53]*constants[53]*(algebraic[58]+algebraic[59])+algebraic[57]*algebraic[59]*(constants[49]+algebraic[53])
    algebraic[62] = algebraic[58]*constants[53]*(algebraic[54]+algebraic[55])+algebraic[59]*algebraic[54]*(constants[53]+algebraic[57])
    algebraic[63] = algebraic[54]*constants[49]*(algebraic[58]+algebraic[59])+algebraic[58]*algebraic[55]*(constants[49]+algebraic[53])
    algebraic[64] = (constants[14]*(algebraic[61]*algebraic[55]-algebraic[60]*algebraic[59]))/(algebraic[60]+algebraic[61]+algebraic[62]+algebraic[63])
    algebraic[51] = (constants[12]*(power(constants[13]/(5.64000+constants[13]), 3.00000))*(power(constants[8]/(0.621000+constants[8]), 2.00000))*1.60000)/(1.50000+exp(-(states[0]+60.0000)/40.0000))
    algebraic[50] = constants[10]*(states[0]-constants[11])
    rates[0] = -(algebraic[65]+algebraic[70]+algebraic[66]+algebraic[34]+algebraic[17]+algebraic[67]+algebraic[49]+algebraic[64]+algebraic[51]+algebraic[50]+algebraic[69])/constants[3]
    algebraic[72] = 5.00000/(1.00000+constants[46]/states[19])
    algebraic[73] = (states[20]-states[21])/constants[47]
    rates[20] = algebraic[72]-(algebraic[73]*constants[55])/constants[54]
    algebraic[74] = 88800.0*states[19]*(1.00000-states[22])-446.000*states[22]
    rates[22] = algebraic[74]
    algebraic[76] = 227700.*states[19]*((1.00000-states[23])-states[24])-7.51000*states[23]
    rates[23] = algebraic[76]
    algebraic[75] = (constants[45]*(states[21]-states[5]))/(1.00000+power(0.00120000/states[5], 2.00000))
    algebraic[79] = 534.000*states[21]*(1.00000-states[27])-445.000*states[27]
    rates[21] = (algebraic[73]-algebraic[75])-10.0000*algebraic[79]
    algebraic[71] = (states[5]-states[19])/4.00000e-05
    algebraic[77] = 227700.*states[19]*(1.00000-states[25])-542.000*states[25]
    rates[19] = (algebraic[71]*constants[56]-algebraic[72]*constants[54])/constants[57]-(0.0450000*algebraic[77]+0.0310000*algebraic[74]+0.0620000*algebraic[76])
    rates[25] = algebraic[77]
    algebraic[78] = 227700.*states[5]*(1.00000-states[26])-542.000*states[26]
    rates[26] = algebraic[78]
    rates[27] = algebraic[79]
    algebraic[80] = 0.00100000*(115.000*states[5]*(1.00000-states[28])-1000.00*states[28])
    rates[5] = (((-(algebraic[70]-2.00000*algebraic[64])/(2.00000*constants[2])+algebraic[75]*constants[55])/constants[56]-algebraic[71])-0.0450000*algebraic[78])-(0.0310000/1.20000)*algebraic[80]
    rates[28] = algebraic[80]
    return(rates)

def computeAlgebraic(constants, states, voi):
    algebraic = array([[0.0] * len(voi)] * sizeAlgebraic)
    states = array(states)
    voi = array(voi)
    algebraic[15] = 120.000/(1.00000+exp(-(states[0]+50.0000)/15.0000))
    algebraic[16] = 5.82000/(1.00000+exp(-(states[0]+50.0000)/15.0000))
    algebraic[18] = 2277.00*2.50000*((1.00000-states[23])-states[24])-751.000*states[24]
    algebraic[0] = 1.00000/(1.00000+exp(((states[0]+83.1900)-(-7.20000*(power(constants[5], 0.690000)))/(power(1.26000e-05, 0.690000)+power(constants[5], 0.690000)))/13.5600))
    algebraic[19] = 0.250000+2.00000*exp(-(power(states[0]+70.0000, 2.00000))/500.000)
    algebraic[1] = 1.00000/(1.00000+exp((states[0]+10.2200)/-8.50000))
    algebraic[20] = 1.00000/(17.0000*exp(0.0398000*states[0])+0.211000*exp(-0.0510000*states[0]))
    algebraic[2] = 1.00000/(1.00000+exp((states[0]+10.2200)/-8.50000))
    algebraic[21] = 0.335810+0.906730*exp(-(power(states[0]+10.0000, 2.00000))/988.050)
    algebraic[8] = 1.00000/(1.00000+exp((states[0]-(-24.0000+constants[35]))/6.31000))
    algebraic[27] = 0.0100000+0.153900*exp(-(power(states[0]+40.0000, 2.00000))/185.670)
    algebraic[9] = 1.00000/(1.00000+exp((states[0]-(-24.0000+constants[36]))/6.31000))
    algebraic[28] = 0.0600000+0.480760*2.25000*exp(-(power(states[0]--40.0000, 2.00000))/138.040)
    algebraic[29] = 0.000596000+0.00311800/(1.03700*exp(0.0900000*(states[0]+30.6100))+0.396000*exp(-0.120000*(states[0]+23.8400)))
    algebraic[10] = 1.00000/(1.00000+exp((states[0]-7.44000)/-16.4000))
    algebraic[30] = 0.0126600+4.72716/(1.00000+exp((states[0]+154.500)/23.9600))
    algebraic[11] = 1.00000/(1.00000+exp((states[0]+33.8000)/6.12000))
    algebraic[31] = 0.100000+4.00000*exp(-(power(states[0]+65.0000, 2.00000))/500.000)
    algebraic[12] = 1.00000/(1.00000+exp((states[0]+33.8000)/6.12000))
    algebraic[4] = states[0]+44.4000
    algebraic[23] = custom_piecewise([less(fabs(algebraic[4]) , constants[30]), (-460.000*-12.6730)/exp(algebraic[4]/-12.6730) , True, (-460.000*algebraic[4])/(exp(algebraic[4]/-12.6730)-1.00000)])
    algebraic[36] = 18400.0*exp(algebraic[4]/-12.6730)
    algebraic[3] = (1.00000/(1.00000+exp((states[0]+4.90000)/15.1400)))*(1.00000-0.300000*exp(-(power(states[0], 2.00000))/500.000))
    algebraic[22] = 92.0100*exp(-0.0183000*states[0])
    algebraic[35] = 603.600*exp(0.00942000*states[0])
    algebraic[43] = 1.00000/(algebraic[22]+algebraic[35])
    algebraic[5] = 44.9000*exp((states[0]+66.9000)/-5.57000)
    algebraic[24] = 1491.00/(1.00000+323.300*exp((states[0]+94.6000)/-12.9000))
    algebraic[37] = algebraic[5]/(algebraic[5]+algebraic[24])
    algebraic[44] = 0.0300000/(1.00000+exp((states[0]+40.0000)/6.00000))+0.000350000
    algebraic[6] = 44.9000*exp((states[0]+66.9000)/-5.57000)
    algebraic[25] = 1491.00/(1.00000+323.300*exp((states[0]+94.6000)/-12.9000))
    algebraic[38] = algebraic[6]/(algebraic[6]+algebraic[25])
    algebraic[45] = 0.120000/(1.00000+exp((states[0]+60.0000)/2.00000))+0.00295000
    algebraic[39] = 1.00000/(1.00000+exp((states[0]-(-3.20000+constants[33]))/constants[34]))
    algebraic[7] = (-26.1200*(states[0]+35.0000))/(exp((states[0]+35.0000)/-2.50000)-1.00000)+(-78.1100*states[0])/(exp(-0.208000*states[0])-1.00000)
    algebraic[26] = (10.5200*(states[0]-5.00000))/(exp(0.400000*(states[0]-5.00000))-1.00000)
    algebraic[46] = 1.00000/(algebraic[7]+algebraic[26])
    algebraic[32] = 1.00000/(0.150000*exp(-states[0]/11.0000)+0.200000*exp(-states[0]/700.000))
    algebraic[40] = 1.00000/(16.0000*exp(states[0]/8.00000)+15.0000*exp(states[0]/50.0000))
    algebraic[47] = 0.00100000/(algebraic[32]+algebraic[40])
    algebraic[13] = 1.00000/(1.00000+exp((states[0]--49.1000)/-8.98000))
    algebraic[14] = 0.150400/(3100.00*exp(states[0]/13.0000)+700.000*exp(states[0]/70.0000))
    algebraic[33] = 0.150400/(95.0000*exp(-states[0]/10.0000)+50.0000*exp(-states[0]/700.000))+0.000229000/(1.00000+exp(-states[0]/5.00000))
    algebraic[48] = 0.00100000/(algebraic[14]+algebraic[33])
    algebraic[41] = algebraic[14]/(algebraic[14]+algebraic[33])
    algebraic[65] = (((constants[29]*(power(states[6], 3.00000))*(0.635000*states[7]+0.365000*states[8])*constants[28]*states[0]*constants[2])/constants[48])*(exp((states[0]-constants[51])/constants[48])-1.00000))/(exp(states[0]/constants[48])-1.00000)
    algebraic[68] = (constants[40]*states[17]*states[18]*(power(constants[5], 1.50000)))/(power(constants[41], 1.50000)+power(constants[5], 1.50000))
    algebraic[69] = (((algebraic[68]*constants[8])/(10.0000+constants[8]))*(states[0]-constants[50]))/(1.00000+exp(((states[0]-constants[50])-140.000)/(2.50000*constants[48])))
    algebraic[70] = constants[31]*states[9]*(0.675000*states[10]+0.325000*states[11])*(states[0]-constants[32])*(1.00000-((algebraic[69]*constants[5])/(9.00000e-05+constants[5]))/1.00000)
    algebraic[66] = constants[37]*states[12]*(0.450000*states[13]+0.550000*states[14])*(states[0]-constants[52])
    algebraic[34] = constants[6]*(0.900000*states[2]+0.100000*states[3])*states[4]*(states[0]-constants[50])
    algebraic[17] = states[1]*constants[4]*(states[0]--30.0000)
    algebraic[67] = constants[39]*states[15]*states[16]*(states[0]-constants[38])
    algebraic[42] = constants[9]*(0.500000+0.500000/(1.00000+exp((states[0]+30.0000)/5.00000)))
    algebraic[49] = (algebraic[42]*(power(constants[8]/(constants[8]+0.590000), 3.00000))*(states[0]+81.9000))/(1.00000+exp((1.39300*(states[0]+81.9000+3.60000))/constants[48]))
    algebraic[57] = exp((-constants[16]*states[0])/(2.00000*constants[48]))
    algebraic[52] = 1.00000+(constants[27]/constants[26])*(1.00000+exp((constants[17]*states[0])/constants[48]))+constants[28]/constants[24]+(power(constants[28], 2.00000))/(constants[24]*constants[25])+(power(constants[28], 3.00000))/(constants[24]*constants[25]*constants[23])
    algebraic[54] = (((power(constants[28], 2.00000))/(constants[24]*constants[25])+(power(constants[28], 3.00000))/(constants[24]*constants[25]*constants[23]))*exp((-constants[16]*states[0])/(2.00000*constants[48])))/algebraic[52]
    algebraic[55] = ((constants[27]/constants[26])*exp((-constants[17]*states[0])/constants[48]))/algebraic[52]
    algebraic[53] = exp((constants[16]*states[0])/(2.00000*constants[48]))
    algebraic[60] = algebraic[57]*constants[49]*(algebraic[54]+algebraic[55])+algebraic[55]*algebraic[53]*(constants[53]+algebraic[57])
    algebraic[56] = 1.00000+(states[5]/constants[18])*(1.00000+exp((-constants[15]*states[0])/constants[48])+constants[13]/constants[22])+constants[13]/constants[19]+(power(constants[13], 2.00000))/(constants[19]*constants[20])+(power(constants[13], 3.00000))/(constants[19]*constants[20]*constants[21])
    algebraic[59] = ((states[5]/constants[18])*exp((-constants[15]*states[0])/constants[48]))/algebraic[56]
    algebraic[58] = (((power(constants[13], 2.00000))/(constants[19]*constants[20])+(power(constants[13], 3.00000))/(constants[19]*constants[20]*constants[21]))*exp((constants[16]*states[0])/(2.00000*constants[48])))/algebraic[56]
    algebraic[61] = algebraic[53]*constants[53]*(algebraic[58]+algebraic[59])+algebraic[57]*algebraic[59]*(constants[49]+algebraic[53])
    algebraic[62] = algebraic[58]*constants[53]*(algebraic[54]+algebraic[55])+algebraic[59]*algebraic[54]*(constants[53]+algebraic[57])
    algebraic[63] = algebraic[54]*constants[49]*(algebraic[58]+algebraic[59])+algebraic[58]*algebraic[55]*(constants[49]+algebraic[53])
    algebraic[64] = (constants[14]*(algebraic[61]*algebraic[55]-algebraic[60]*algebraic[59]))/(algebraic[60]+algebraic[61]+algebraic[62]+algebraic[63])
    algebraic[51] = (constants[12]*(power(constants[13]/(5.64000+constants[13]), 3.00000))*(power(constants[8]/(0.621000+constants[8]), 2.00000))*1.60000)/(1.50000+exp(-(states[0]+60.0000)/40.0000))
    algebraic[50] = constants[10]*(states[0]-constants[11])
    algebraic[72] = 5.00000/(1.00000+constants[46]/states[19])
    algebraic[73] = (states[20]-states[21])/constants[47]
    algebraic[74] = 88800.0*states[19]*(1.00000-states[22])-446.000*states[22]
    algebraic[76] = 227700.*states[19]*((1.00000-states[23])-states[24])-7.51000*states[23]
    algebraic[75] = (constants[45]*(states[21]-states[5]))/(1.00000+power(0.00120000/states[5], 2.00000))
    algebraic[79] = 534.000*states[21]*(1.00000-states[27])-445.000*states[27]
    algebraic[71] = (states[5]-states[19])/4.00000e-05
    algebraic[77] = 227700.*states[19]*(1.00000-states[25])-542.000*states[25]
    algebraic[78] = 227700.*states[5]*(1.00000-states[26])-542.000*states[26]
    algebraic[80] = 0.00100000*(115.000*states[5]*(1.00000-states[28])-1000.00*states[28])
    return algebraic

def custom_piecewise(cases):
    """Compute result of a piecewise function"""
    return select(cases[0::2],cases[1::2])

def solve_model():
    """Solve model with ODE solver"""
    from scipy.integrate import ode
    # Initialise constants and state variables
    (init_states, constants) = initConsts()

    # Set timespan to solve over
    voi = linspace(0, 20, 10000)

    # Construct ODE object to solve
    r = ode(computeRates)
    r.set_integrator('vode', method='bdf', atol=1e-06, rtol=1e-06, max_step=1)
    r.set_initial_value(init_states, voi[0])
    r.set_f_params(constants)

    # Solve model
    states = array([[0.0] * len(voi)] * sizeStates)
    states[:,0] = init_states
    for (i,t) in enumerate(voi[1:]):
        if r.successful():
            r.integrate(t)
            states[:,i+1] = r.y
        else:
            break

    # Compute algebraic variables
    algebraic = computeAlgebraic(constants, states, voi)
    return (voi, states, algebraic)

def plot_model(voi, states, algebraic):
    """Plot variables against variable of integration"""
    import pylab
    (legend_states, legend_algebraic, legend_voi, legend_constants) = createLegends()
    pylab.figure(1)
    pylab.plot(voi,states[0])
    pylab.xlabel(legend_voi)
    #pylab.legend(legend_states + legend_algebraic, loc='best')
    pylab.show()


#(voi, states, algebraic) = solve_model()
#plot_model(voi, states, algebraic)

def solve_model(
    simulation_time=20.0, 
    num_points=10000,
    initial_states=None,
    constants=None,
    solver='odeint',
    rtol=1.0e-7,
    atol=1.0e-7,
    verbose=True
):
    """Решает модель сердечной клетки с использованием ODE-решателя.
    
    Параметры:
        simulation_time (float): Длительность симуляции в секундах (по умолчанию 20)
        num_points (int): Количество точек для вывода (по умолчанию 10000)
        initial_states (array-like): Начальные состояния (если None, используются значения по умолчанию)
        constants (array-like): Параметры модели (если None, используются значения по умолчанию)
        solver (str): Используемый решатель ('odeint' или 'solve_ivp')
        rtol (float): Относительный допуск для решателя
        atol (float): Абсолютный допуск для решателя
        verbose (bool): Выводить информацию о ходе решения
        
    Возвращает:
        tuple: (voi, states) - массив временных точек и соответствующих состояний
    """
    try:
        from scipy.integrate import odeint, solve_ivp
        import numpy as np
        
        # Инициализация параметров модели
        if constants is None or initial_states is None:
            default_states, default_constants = initConsts()
            if constants is None:
                constants = default_constants
            if initial_states is None:
                initial_states = default_states

        # Проверка входных данных
        initial_states = np.asarray(initial_states, dtype=np.float64)
        constants = np.asarray(constants, dtype=np.float64)
        
        if len(initial_states) != sizeStates:
            raise ValueError(f"Размер initial_states должен быть {sizeStates}")
        if len(constants) != sizeConstants:
            raise ValueError(f"Размер constants должен быть {sizeConstants}")

        # Создание временной сетки
        voi = np.linspace(0, simulation_time, num_points)
        
        if verbose:
            print(f"Running simulation for {simulation_time} seconds with {num_points} points")
            print(f"Using solver: {solver}")

        # Выбор и запуск решателя
        if solver == 'odeint':
            # Использование odeint
            states = odeint(
                func=computeRates,
                y0=initial_states,
                t=voi,
                args=(constants,),
                rtol=rtol,
                atol=atol,
                tfirst=True
            )
        elif solver == 'solve_ivp':
            # Использование solve_ivp (более современный вариант)
            solution = solve_ivp(
                fun=lambda t, y: computeRates(y, t, constants),
                t_span=(0, simulation_time),
                y0=initial_states,
                t_eval=voi,
                method='LSODA',
                rtol=rtol,
                atol=atol
            )
            states = solution.y.T
        else:
            raise ValueError(f"Неизвестный решатель: {solver}. Доступные варианты: 'odeint', 'solve_ivp'")

        if verbose:
            print("Simulation completed successfully")

        return voi, states

    except ImportError as e:
        raise ImportError("Для работы solve_model требуется scipy. Установите его: pip install scipy") from e
    except Exception as e:
        raise RuntimeError(f"Ошибка при решении модели: {str(e)}") from e



# С пользовательскими настройками
time_points, states = solve_model(
    simulation_time=10.0,
    num_points=5000,
    solver='solve_ivp',
    rtol=1e-6,
    verbose=True
)

import matplotlib.pyplot as plt

plt.plot(time_points, states[:, 0])
plt.savefig('1.png')