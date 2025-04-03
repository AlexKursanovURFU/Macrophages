from math import exp, power, fabs, less

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