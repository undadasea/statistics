import numpy as np
import plots_functions
from tabulate import tabulate


def get_expected_value(m):
    return m


def get_variance(sigma):
    return sigma**2


def get_num_CentralTh():
    rand_variable = np.random.uniform()
    for i in range(11):
        rand_variable += np.random.uniform()
    return rand_variable - 6


def run_central_alg(num_loop):
    variables = np.zeros(num_loop)
    for i in range(num_loop):
        variables[i] = get_num_CentralTh()
    return variables


def get_num_BoxMuller():
    return np.sqrt(-2*np.log(np.random.uniform())) * np.cos(2 * np.pi * np.random.uniform())


def run_bm_alg(num_loop):
    variables = np.zeros(num_loop)
    for i in range(num_loop):
        variables[i] = get_num_BoxMuller()
    return variables


variables_c = run_central_alg(10**5)
variables_bm = run_bm_alg(10**5)

plots_functions.draw_hist(variables_c)
plots_functions.draw_hist(variables_bm)

M_c = np.mean(variables_c)
D_c = np.var(variables_c)

M_bm = np.mean(variables_bm)
D_bm = np.var(variables_bm)

print(tabulate([["M", M_c, M_bm, get_expected_value(0)],
               ["D", D_c, D_bm, get_variance(1)]],
               headers=["Characteristics", "Central", "Box-Muller", "Theoretical"]))

