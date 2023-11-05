import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 3, 3, 4, 2])

y_prime = np.array([-2, 1])

cs = CubicSpline(x, y, bc_type=((1, y_prime[0]), (1, y_prime[1])))


x_vals = np.linspace(0, 4, 100)
y_vals = cs(x_vals)


plt.plot(x_vals, y_vals, label='сплайн')
plt.scatter(x, y, color='red', label='точки')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Кубический сплайн')
plt.legend()
plt.show()
