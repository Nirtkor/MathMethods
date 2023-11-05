import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


x = np.linspace(0, np.pi/2, 5)
y = np.cos(x)

endpoint_derivatives = [0, -np.sin(np.pi/2)]

spline = CubicSpline(x, y, bc_type=((1, endpoint_derivatives[0]), (1, endpoint_derivatives[1])))


x_values = np.linspace(0, 4, 100)
y_values_spline = spline(x_values)
y_values_cos = np.cos(x_values)

plt.plot(x_values, y_values_spline, label='сплайн')
plt.plot(x_values, y_values_cos, label='cos(x)', linestyle='dashed')
plt.scatter(x, y, color='red', label='точки')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Зажатый кубический сплайн, интерполирующий cos(x)')
plt.legend()
plt.show()
