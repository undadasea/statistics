import numpy as np
import math
from tabulate import tabulate


def get_expected_value(N, p):
    return N * p


def get_variance(N, p):
    return N*p*(1 - p)


def get_p_binom(N, p, r):

    #Pprint(r)
    if r == 0:
        return (1 - p)**N
    else:
        return get_p_binom(N, p, r-1)*(((N-r)/(r+1))*(p/(1-p)))
        # why this one dsnt work

def get_p(N, p, r):
    return math.factorial(N)/(math.factorial(r) * math.factorial(N-r)) * p**r * (1-p)**(N-r)



# возможные значения случ величины от 0 до N
N = 10
# данная вероятность, одинаковая для всех испытаний
p = 0.5


array_binom_manual = np.zeros(10**4)
# standard should be done by normal distribution from 3rd lab
array_binom_standard = np.zeros(10**4)

for i in range(10**4):

    alpha = np.random.uniform()
    r = 0
    while alpha > 0:
        alpha -= get_p(N, p, r)
        r += 1
        #print(get_p_binom(N, p, r))

    array_binom_manual[i] = r-1

    array_binom_standard[i] = np.random.binomial(N, p)


D_m = np.var(array_binom_manual)
M_m = np.mean(array_binom_manual)

D_s = np.var(array_binom_standard)
M_s = np.mean(array_binom_standard)

print(tabulate([["M", M_m, M_s, get_expected_value(N, p)],
               ["D", D_m, D_s, get_variance(N, p)]],
               headers=["Characteristics", "Manual", "Standard", "Theoretical"]))



# test get_p_binom
array_test = np.zeros(N)
for i in range(N):
    array_test[i] = get_p_binom(N, p, i)
    print(array_test[i])

print("test sum = ", sum(array_test))
