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
        #return get_p(p, r-1)*(1-p)
        return p*(1-p)**(r-1)

def get_dense_p(p, r):
    return p*((1-p)**(r-1))


p = 0.5

array_geom_manual = np.zeros(10**5)

for i in range(10**5):

    alpha = np.random.uniform()
    r = 1
    while alpha > 0:
        alpha -= get_p(p, r)
        r += 1

    array_geom_manual[i] = r-1


D_m = np.var(array_geom_manual)
M_m = np.mean(array_geom_manual)

print(D_m, M_m)


y = np.zeros(10)
x = np.zeros(10)
for i in range(10):
    print(get_p(p, i+1))
    y[i] = get_p(p, i+1)
    x[i] = i
plot_ = plt.subplot()
plot_.plot(x, y)

plt.show()

