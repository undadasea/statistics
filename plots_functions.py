import numpy as np
import matplotlib.pyplot as plt

# TODO: edit scale
def density(array: np.array, random_value_is_integer: bool):

    array.sort()
    if random_value_is_integer:
        a = array[0]
        interval = 1
        num_intervals = int(array[len(array)-1]) - 1
    else:
        a = array[0]
        b = array[len(array) - 1]
        num_intervals = 15
        interval = (b - a)/num_intervals

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


def draw_hist(data: np.array):
    plt.title("Dense histogram, N={0}".format(len(data)))
    plt.xlabel("Random variable value")
    plt.ylabel("Frequency")
    plt.hist(data, bins=50, rwidth=3)
    plt.show()

    plt.title("Integral histogram, N={0}".format(len(data)))
    plt.xlabel("Random variable value")
    plt.ylabel("Frequency")
    plt.hist(data, bins=50, cumulative=True, rwidth=3)
    plt.show()

