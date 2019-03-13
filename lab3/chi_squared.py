import numpy as np
import plots_functions
from tabulate import tabulate
import lab3.normal as norm


def get_expected_value(N):
    return N


def get_variance(N):
    return N*2


def get_random_num(N):
    variable = 0
    for i in range(N):
        variable += norm.get_num_CentralTh()**2
    return variable


def run_alg(num_loop, N):
    variables = np.zeros(num_loop)
    for i in range(num_loop):
        variables[i] = get_random_num(N)
    return variables


N = 10

variables_ = run_alg(10**5, N)

# plots_functions.draw_hist(variables_)

D = np.var(variables_)
M = np.mean(variables_)

print(tabulate([["M", M, get_expected_value(N)],
                ["D", D, get_variance(N)]],
               headers=["", "Experimental", "Theoretical"]))

