import numpy as np
import plots_functions
from tabulate import tabulate


def get_random_num(beta):
    return -beta*np.log(np.random.uniform())


def run_alg(num_loop, beta):
    variables = np.zeros(num_loop)
    for i in range(num_loop):
        variables[i] = get_random_num(beta)
    return variables


variables_ = run_alg(10**5, 1)

plots_functions.draw_hist(variables_)

D = np.var(variables_)
M = np.mean(variables_)

print(tabulate([["M", M, 1],
                ["D", D, 1]],
               headers=["", "Experimental", "Theoretical"]))


