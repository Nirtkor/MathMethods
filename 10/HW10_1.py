import numpy as np
import matplotlib.pyplot as plt

points = np.array([[0, 3], [1, 5], [2, 4], [3, 1]])

x = points[:, 0]
y = points[:, 1]

h = np.diff(x)
a = y
b = np.zeros(len(x) - 1)
c = np.zeros(len(x))
d = np.zeros(len(x) - 1)

A = np.zeros(shape=(len(x), len(x)))
A[0, 0] = 1
A[-1, -1] = 1

for i in range(1, len(x) - 1):
    A[i, i - 1] = h[i - 1]
    A[i, i] = 2 * (h[i - 1] + h[i])
    A[i, i + 1] = h[i]

dy = np.diff(y)
rhs = np.zeros(len(x))
for i in range(1, len(x) - 1):
    rhs[i] = 3 * (dy[i] / h[i] - dy[i - 1] / h[i - 1])

c[1:-1] = np.linalg.solve(A[1:-1, 1:-1], rhs[1:-1])

for i in range(len(x) - 1):
    b[i] = dy[i] / h[i] - h[i] / 3 * (2 * c[i] + c[i + 1])
    d[i] = (c[i + 1] - c[i]) / (3 * h[i])

for i in range(len(x) - 1):
    print(f"b{i}: {b[i]}, c{i}: {c[i]}, d{i}: {d[i]}")

def spline(x_val, points, b, c, d):
    x = points[:, 0]
    y = points[:, 1]
    for i in range(len(x) - 1):
        if x[i] <= x_val <= x[i + 1]:
            return y[i] + b[i] * (x_val - x[i]) + c[i] * (x_val - x[i]) ** 2 + d[i] * (x_val - x[i]) ** 3

x_values = np.linspace(0, 3, 100)
y_values = [spline(i, points, b, c, d) for i in x_values]

plt.plot(x_values, y_values, label='сплайн')
plt.scatter(x, y, color='red', label='точки')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Натуральный кубический сплайн')
plt.legend()
plt.show()
