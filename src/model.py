def SIR(x,t,params):
  k1,k2=params
  S,I,R=x
  k1=0.00001
  k2=0.000001
  dSdt=-k1*S*I
  dIdt=k1*S*I-k2*I
  dRdt=k2*I
  return[dSdt,dIdt,dRdt]

