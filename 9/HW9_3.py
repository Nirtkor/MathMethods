import numpy as np
import matplotlib.pyplot as plt

# Заданные точки и полином
points = np.array([[0, 1], [2, 2], [3, 4]])
x_values = np.linspace(-2*np.pi, 2*np.pi, 100)
y_values_sin = np.sin(x_values)
y_values_poly = 0.5*x_values**2 - 0.5*x_values + 1

# Вычисление ошибки интерполяции
errors = np.sin(points[:, 0]) - (0.5 * points[:, 0] ** 2 - 0.5 * points[:, 0] + 1)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values_sin, label='sin(x)')
plt.plot(x_values, y_values_poly, label='Интерполяционный полином', linestyle='dashed')
plt.scatter(points[:, 0], points[:, 1], color='red')
plt.plot(points[:, 0], np.sin(points[:, 0]), 'ro', label='Точки')
plt.title('График ошибки интерполяции для sin(x)')
plt.xlabel('x')
plt.ylabel('Значения функции и полинома')
plt.legend()
plt.grid()

# Вывод ошибки интерполяции
print(f'Ошибки интерполяции в заданных точках: {errors}')

# Отображение графика
plt.show()
