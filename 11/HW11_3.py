import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return x / np.sqrt(x**2 + 9)

def func2(x):
    return x**2 * np.log(x)


def rectangle_rule(func, a, b, n):
    h = (b - a) / n
    integral_sum = 0
    for i in range(n):
        integral_sum += func(a + (i + 0.5) * h)
    return h * integral_sum

a1, b1 = 0, 4
a2, b2 = 1, 3
errors1 = []
errors2 = []
n_values = [2**i for i in range(9)]

for n in n_values:
    approx1 = rectangle_rule(func1, a1, b1, n)
    approx2 = rectangle_rule(func2, a2, b2, n)
    actual_value1 = 3
    actual_value2 = 9 * (3 * np.log(3) - 1)
    errors1.append(abs(approx1 - actual_value1))
    errors2.append(abs(approx2 - actual_value2))


plt.figure(figsize=(12, 8))
plt.loglog((b1 - a1) / np.array(n_values), errors1, marker='o', label='Integral 1')
plt.loglog((b2 - a2) / np.array(n_values), errors2, marker='o', label='Integral 2')
plt.xlabel('h', fontsize=14)
plt.ylabel('ошибки', fontsize=14)
plt.title('График зависимости ошибки от h', fontsize=16)
plt.legend()
plt.grid()
plt.show()
