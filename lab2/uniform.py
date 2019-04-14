import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import plots_functions


def get_probability_uniform(r_low, r_up):
    n = r_up - r_low + 1
    return 1/n


def get_number_uniform(r_low, r_up):
    u = np.random.uniform()
    random_variable = round((r_up - r_low + 1)*u + r_low)
    if random_variable <= (r_up - r_low + 1)*u + r_low:
        return random_variable
    else:
        return random_variable - 1


def get_expected_value(r_low, r_up):
    return (r_low + r_up)/2


def get_variance(r_low, r_up):
    n = r_up - r_low + 1
    return (n**2 - 1)/12


r_low = 1
r_up = 100

array_uniform = np.zeros(10**6)

for i in range(10**6):
    array_uniform[i] = get_number_uniform(r_low, r_up)

D = np.var(array_uniform)
M = np.mean(array_uniform)

plots_functions.draw_hist(array_uniform, "Uniform")

print(tabulate([["M", M, abs(M - get_expected_value(r_low, r_up)), get_expected_value(r_low, r_up)],
          ["D", D, abs(D - get_variance(r_low, r_up)), get_variance(r_low, r_up)]],
         headers=["", "Experimental", "Inaccuracy", "Theoretical"]))

