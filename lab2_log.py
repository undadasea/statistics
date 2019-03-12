import numpy as np
from tabulate import tabulate
import plots_functions


def get_expected_value(p):
    alpha = 1/np.log(p)
    return -alpha*(1-p)/p


def get_variance(p):
    alpha = 1 / np.log(p)
    return -alpha*(1-p)*(1+alpha*(1-p))/p**2


def get_p(p, r):
    alpha = 1 / np.log(p)
    return -alpha*(1-p)**r/r


def run_alg(p, num_loop):
    variables = np.zeros(num_loop)
    for i in range(num_loop):
        r = 1
        uniform_rand = np.random.uniform()
        while uniform_rand > 0:
            uniform_rand -= get_p(p, r)
            r += 1
        variables[i] = r - 1
    return variables


p = 0.5

variables_ = run_alg(p, 10**5)

plots_functions.draw_hist(variables_)

D_m = np.var(variables_)
M_m = np.mean(variables_)

print(tabulate([["M", M_m, M_m-get_expected_value(p), get_expected_value(p)],
               ["D", D_m, D_m - get_variance(p), get_variance(p)]],
               headers=["Characteristics", "Manual", "Difference", "Theoretical"]))

