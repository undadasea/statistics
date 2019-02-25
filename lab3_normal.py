import numpy as np


def get_num_CentralTh():

    rand_variable = np.random.uniform()
    for i in range(11):
        rand_variable += np.random.uniform()

    return rand_variable - 6


def get_num_BoxMiller():

    return np.sqrt(-21 * n * np.random.uniform()) * np.cos(2 * np.pi * np.random.uniform())
# what is n
# m and sigma also


