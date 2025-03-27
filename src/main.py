from math import log
from parameters import create_legends
from parameters import init_consts
from parameters import compute_derived_constants
print(create_legends()[1])
if __name__ == "__main__":
    states, constants = init_consts()
    print("States:", states)
    print("Constants:", constants)
