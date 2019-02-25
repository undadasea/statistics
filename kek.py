import random
import matplotlib.pyplot as plt
numbers = [random.random() for i in range(1000)]
numbers.sort()
data = [0 for i in range(10)]
print(numbers)
for numb in numbers:
    for i in range(int(numb * 10), 10):
        data[i] += 1

print(data)
plt.plot([0.1 * i for i in range(10)], data)
plt.show()
for i in range(len(data)):
    data[i] /= 1000

plt.plot([0.1 * i for i in range(10)], data)
plt.show()
print(data)