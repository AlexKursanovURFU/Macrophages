from scipy.integrate import odeint

def solver(model, x, time, param):
    return odeint(func =model, y0=x, t=time, args = (param,))