import numpy as np
import matplotlib.pyplot as plt
import plots_functions
from tabulate import tabulate


def get_expected_value(p: float) -> float:
    return 1/p


def get_variance(p: float) -> float:
    return (1-p)/p**2


def get_p(p: float, r: int) -> float:
    if r == 1:
        return p
    else:
        return get_p(p, r-1)*(1-p)


def get_dense_p(p: float, r: int) -> float:
    return p*((1-p)**(r-1))


def run_first_alg(p: float, num_loop: int) -> np.array:
    array_random = np.zeros(num_loop)
    for i in range(num_loop):
        alpha = np.random.uniform()
        r = 1
        while alpha > 0:
            alpha -= get_p(p, r)
            r += 1

        array_random[i] = r - 1
    return array_random


def run_second_alg(p: float, num_loop: int) -> np.array:
    array_random = np.zeros(num_loop)
    for i in range(num_loop):
        u = np.random.uniform()
        r = 1  # since r is a number of the first success
        while u > p:
            r += 1
            u = np.random.uniform()
        array_random[i] = r
    return array_random


def run_third_alg(p: float, num_loop: int) -> np.array:
    array_random = np.zeros(num_loop)
    for i in range(num_loop):
        u = np.random.uniform()
        r = int(np.log(u)/np.log(1-p)) + 1
        array_random[i] = r
    return array_random


p = 0.5


array_geom_manual = run_first_alg(p, 10**5)
array_geom_direct = run_second_alg(p, 10**6)
array_geom_log = run_third_alg(p, 10**5)


D_m = np.var(array_geom_manual)
M_m = np.mean(array_geom_manual)

D_d = np.var(array_geom_direct)
M_d = np.mean(array_geom_direct)

D_l = np.var(array_geom_log)
M_l = np.mean(array_geom_log)

print(M_m, D_m)
print(M_d, D_d)
print(M_l, D_l)


plots_functions.draw_hist(array_geom_manual, "Geometric, manual")
plots_functions.draw_hist(array_geom_direct, "Geometric, direct")
plots_functions.draw_hist(array_geom_log, "Geometric, log")


print(tabulate([["M", M_m, M_d, M_l, get_expected_value(p)],
               ["D", D_m, D_d, D_l, get_variance(p)]],
               headers=["Characteristics", "Cumulative", "Direct", "Log", "Theoretical"]))






