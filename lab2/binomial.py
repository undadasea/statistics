import numpy as np
import math
from tabulate import tabulate
import plots_functions


def get_expected_value(N, p):
    return N * p


def get_variance(N, p):
    return N*p*(1 - p)


def get_p(N, p, r):
    return math.factorial(N)/(math.factorial(r) * math.factorial(N-r)) * p**r * (1-p)**(N-r)


# возможные значения случ величины от 0 до N
N = 20
# данная вероятность, одинаковая для всех испытаний
p = 0.5


array_binom_manual = np.zeros(10**4)
array_binom_standard = np.zeros(10**4)

for i in range(10**4):

    alpha = np.random.uniform()
    r = 0
    while alpha > 0:
        alpha -= get_p(N, p, r)
        r += 1
    array_binom_manual[i] = r-1

    array_binom_standard[i] = np.random.binomial(N, p)


D_m = np.var(array_binom_manual)
M_m = np.mean(array_binom_manual)

D_s = np.var(array_binom_standard)
M_s = np.mean(array_binom_standard)

print(tabulate([["M", M_m, M_s, get_expected_value(N, p)],
               ["D", D_m, D_s, get_variance(N, p)]],
               headers=["Characteristics", "Manual", "Standard", "Theoretical"]))


plots_functions.draw_hist(array_binom_standard, "Binomial")

