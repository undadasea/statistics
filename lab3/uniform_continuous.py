import numpy as np
from tabulate import tabulate
import plots_functions


def get_num(a, b):
    return (b - a) * np.random.uniform() + a


def get_expected_value(a, b):
    return (a+b)/2


def get_variance(a, b):
    return (b-a)**2/12


a = 1
b = 100

array_uniform = np.zeros(10**6)

for i in range(10**6):
    array_uniform[i] = get_num(a, b)

D = np.var(array_uniform)
M = np.mean(array_uniform)

print(tabulate([["M", M, abs(M - get_expected_value(a, b)), get_expected_value(a, b)],
          ["D", D, abs(D - get_variance(a, b)), get_variance(a, b)]],
         headers=["", "Experimental", "Inaccuracy", "Theoretical"]))

#plots_functions.draw_hist(array_uniform)

