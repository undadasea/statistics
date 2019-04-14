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

expected_value = np.zeros(len(testsTypes))
variance = np.zeros(len(testsTypes))
standard_deviation = np.zeros(len(testsTypes))

for k in range(len(testsTypes)):

    n = testsTypes[k]
    u = np.random.rand(n)

    expected_value[k] = sum(u)/n
    variance[k] = sum((u - expected_value[k])**2)/n
    standard_deviation[k] = math.sqrt(variance[k])

    correlation = np.zeros(n)
    x_data = np.zeros(n)
    for i in range(1, n):
        correlation[i] = sum((u[:(n-i)] - expected_value[k])*(u[i:] - expected_value[k]))/sum((u - expected_value[k])**2)
        x_data[i] = i
    draw_plot(x_data, correlation, 1)
    plt.show(block=True)

    plots_functions.draw_hist(u, "Uniform")


header = ["n", "characteristics", "experimental data", "theoretical data", "difference"]
table = [[testsTypes[0], "M", expected_value[0], 0.5, abs(0.5-expected_value[0])],
         [testsTypes[0], "D", variance[0], 0.08333, abs(0.08333-variance[0])]]
for i in range(1, len(testsTypes)):
    table.append([testsTypes[i], "M", expected_value[i], 0.5, abs(0.5-expected_value[i])])
    table.append([testsTypes[i], "D", variance[i], 0.08333, abs(0.08333-variance[i])])
print(tabulate(table, header, tablefmt="simple"))

