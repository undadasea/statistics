import numpy as np
import plots_functions
from tabulate import tabulate
from lab3.normal import get_num_CentralTh as get_norm
from lab3.chi_squared import get_random_num as get_chi


def get_expected_value():
    return 0


def get_variance(N):
    return N/(N-2)


def get_random_num(N):
    return get_norm()/np.sqrt(get_chi(N)/N)


def run_alg(num_loop, N):
    variables = np.zeros(num_loop)
    for i in range(num_loop):
        variables[i] = get_random_num(N)
    return variables


N = 10

variables_ = run_alg(10**5, N)

plots_functions.draw_hist(variables_)

D = np.var(variables_)
M = np.mean(variables_)

print(tabulate([["M", M, get_expected_value()],
                ["D", D, get_variance(N)]],
               headers=["", "Experimental", "Theoretical"]))

