

def SIR(x, t, param):
    a, b = param
    S,I,R = x

    dSdt = -a*S*I
    dIdt = a*S*I - b*I
    dRdt = b*I

    return [dSdt, dIdt, dRdt]