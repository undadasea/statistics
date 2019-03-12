import numpy as np
import math
from tabulate import tabulate
import matplotlib.pyplot as plt
import plots_functions



def draw_plot(x_data, y_data, plot_index):
    plt.subplot(2, 2, plot_index)
    plt.title('N = {0}'.format(len(x_data)))
    marker_lines, stem_lines, base_lines = plt.stem(x_data, y_data)
    plt.hlines([1, -1], 0, len(x_data), linestyle="dashed")
    plt.setp(stem_lines, color='black')
    plt.setp(marker_lines, visible=False)
    plt.ylabel('Correlation function value')

testsTypes = np.array([10, 100, 1000, 10000])

M = np.zeros(len(testsTypes))
D = np.zeros(len(testsTypes))
S = np.zeros(len(testsTypes))
#K = np.zeros(len(testsTypes))

for k in range(len(testsTypes)):

    n = testsTypes[k]
    u = np.random.rand(n)

    M[k] = sum(u)/n

    D[k] = sum((u - M[k])**2)/n

    S[k] = math.sqrt(D[k])

    #print(M, D)

    K = np.zeros(n)
    x_data = np.zeros(n)
    for i in range(1, n):

        K[i] = sum((u[:(n-i)] - M[k])*(u[i:] - M[k]))/sum((u - M[k])**2)
        x_data[i] = i

    draw_plot(x_data, K, 1)
    plt.show(block=True)

    plots_functions.draw_hist(u)


header = ["n", "characteristics", "experimental data", "theoretical data", "difference"]
table = [[testsTypes[0], "M", M[0], 0.5, abs(0.5-M[0])],
         [testsTypes[0], "D", D[0], 0.08333, abs(0.08333-D[0])]]
for i in range(1, len(testsTypes)):
    table.append([testsTypes[i], "M", M[i], 0.5, abs(0.5-M[i])])
    table.append([testsTypes[i], "D", D[i], 0.08333, abs(0.08333-D[i])])
print(tabulate(table, header, tablefmt="simple"))

