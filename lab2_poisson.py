import numpy as np


def get_num_algorithm2(mu):
    rand_variable = np.random.uniform()
    while rand_variable >= np.exp(-mu):
        rand_variable *= np.random.uniform()


mu = 10