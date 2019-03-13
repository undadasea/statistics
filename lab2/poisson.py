import numpy as np
import plots_functions
from tabulate import tabulate


def run_alg2(mu, num_loop):
    variables = np.zeros(num_loop)
    for i in range(num_loop):
        rand_variable = np.random.uniform()
        r = 0
        while rand_variable >= np.exp(-mu):
            rand_variable *= np.random.uniform()
            r += 1
        variables[i] = r
    return variables


def get_p(mu, r):
    if r == 0:
        return np.exp(-mu)
    else:
        return get_p(mu, r-1)*mu/r


def run_alg1(mu, num_loop: int) -> np.array:
    variables = np.zeros(num_loop)
    for i in range(num_loop):
        alpha = np.random.uniform()
        r = 0
        while alpha > 0:
            alpha -= get_p(mu, r)
            r += 1
        variables[i] = r - 1
    return variables


mu = 10


variables_1 = run_alg1(mu, 10**5)
variables_2 = run_alg2(mu, 10**5)

plots_functions.draw_hist(variables_1)

print(tabulate([["M", mu, mu, "10.0"],
               ["D", mu, mu, "10.0"]],
               headers=["Characteristics", "Cumulative", "Alternative", "Theoretical"]))

