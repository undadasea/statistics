import numpy as np
import matplotlib.pyplot as plt


def draw_hist(data: np.array, name: str):
    plt.title(name+". Dense histogram, N={0}".format(len(data)))
    plt.xlabel("Random variable value")
    plt.ylabel("Frequency")
    plt.hist(data, bins=50, density=True)
    plt.show()

    plt.title(name+". Integral histogram, N={0}".format(len(data)))
    plt.xlabel("Random variable value")
    plt.ylabel("Frequency")
    plt.hist(data,  cumulative=True, rwidth=3, density=True, bins=50)
    plt.show()

