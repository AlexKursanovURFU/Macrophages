import numpy as np

from model import SIR
from parameters import get_param
from solver import solver

time = np.linspace(0,10,100)
x0 = [10,1,0]

params = get_param()
res = solver(SIR, x0, time, params)
print(res)