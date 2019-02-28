import numpy as np
import matplotlib.pyplot as plt


def get_expected_value(p):
    return 1/p


def get_variance(p):
    return (1-p)/p**2


def get_p(p, r):
    if r == 1:
        return p
    else:
        return get_p(p, r-1)*(1-p)


def get_dense_p(p, r):
    return p*((1-p)**(r-1))


def run_first_alg(p, num_loop):
    array_random = np.zeros(num_loop)
    for i in range(num_loop):
        alpha = np.random.uniform()
        r = 1
        while alpha > 0:
            alpha -= get_p(p, r)
            r += 1

        array_random[i] = r - 1
    return array_random


########### questionable one
def run_second_alg(p, num_loop):
    array_random = np.zeros(num_loop)
    for i in range(num_loop):
        u = np.random.uniform()
        r = 1  # since r is a number of the first success
        while u > p:
            r += 1
            u = np.random.uniform()
        array_random[i] = r
    return array_random


def run_third_alg(p, num_loop):
    array_random = np.zeros(num_loop)
    for i in range(num_loop):
        u = np.random.uniform()
        r = int(np.log(u)/np.log(1-p)) + 1
        array_random[i] = r
    return array_random


# for arrays[10**2] and bigger
# plot histogram frequency
def draw_plot_density(array):

    array.sort()

    # if not integer
    # a = array[0]
    # b = array[len(array) - 1]
    # num_intervals = 10
    # interval = (b - a)/num_intervals

    # if integer
    a = array[0]
    interval = 1
    num_intervals = int(array[len(array)-1]) - 1

    array_frequency = np.zeros(num_intervals)
    array_scalex = np.zeros(num_intervals)

    count = 0
    for j in range(num_intervals):
        while a + (interval*j) <= array[count] < a + (interval*(j+1)):
            array_frequency[j] += 1
            count += 1

    for i in range(num_intervals):
        array_frequency[i] /= len(array)
        array_scalex[i] = interval*i

    plt.plot(array_scalex, array_frequency)
    plt.show()


p = 0.5


array_geom_manual = run_first_alg(p, 10**5)
array_geom_direct = run_second_alg(p, 10**6)
array_geom_log = np.array(run_third_alg(p, 10**5))


D_m = np.var(array_geom_manual)
M_m = np.mean(array_geom_manual)

D_d = np.var(array_geom_direct)
M_d = np.mean(array_geom_direct)

D_l = np.var(array_geom_log)
M_l = np.mean(array_geom_log)

print(M_m, D_m)
print(M_d, D_d)
print(M_l, D_l)


draw_plot_density(array_geom_log)

###################################
y = np.zeros(10)
x = np.zeros(10)
for i in range(10):
    #print(get_p(p, i+1))
    y[i] = get_p(p, i+1)
    x[i] = i
plot_ = plt.subplot()
plot_.plot(x, y)

#plt.show()
##################################


# test p and dense p
array_dense = np.zeros(12)
array_p = np.zeros(12)

for k in range(len(array_dense)):
    array_dense[k] = get_dense_p(p, k+1)
    array_p[k] = get_p(p, k+1)



