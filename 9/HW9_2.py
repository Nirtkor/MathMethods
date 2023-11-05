import numpy as np
import matplotlib.pyplot as plt


years = np.array([1960, 1970, 1990, 2000])
population = np.array([3039585530, 3707475887, 5281653820, 6079603571])
known_population_1980 = 4452584592
linear_coeffs = np.polyfit([1970, 1990], [population[1], population[2]], 1)
linear_estimate_1980 = np.polyval(linear_coeffs, 1980)
quadratic_coeffs = np.polyfit([1960, 1970, 1990], [population[0], population[1], population[2]], 2)
quadratic_estimate_1980 = np.polyval(quadratic_coeffs, 1980)
cubic_coeffs = np.polyfit(years, population, 3)
cubic_estimate_1980 = np.polyval(cubic_coeffs, 1980)

plt.figure(figsize=(10, 6))
plt.plot(years, population, 'o', label='Исходные данные')
x_values = np.linspace(1950, 2050, 100)
plt.plot(x_values, np.polyval(linear_coeffs, x_values), label='Прямая линия (1970-1990)', linestyle='dashed')
plt.plot(x_values, np.polyval(quadratic_coeffs, x_values), label='Парабола (1960-1970-1990)', linestyle='dashed')
plt.plot(x_values, np.polyval(cubic_coeffs, x_values), label='Кубический полином (все данные)', linestyle='dashed')
plt.title('Оценка численности населения Земли')
plt.xlabel('Год')
plt.ylabel('Численность населения')
plt.legend()
plt.grid()

print(f"Оценка населения в 1980 году с использованием прямой линии: {linear_estimate_1980.round()}")
print(f"Исследование прямой выявило расхождение с данными на: {linear_estimate_1980.round()-known_population_1980}")
print(f"Оценка населения в 1980 году с использованием параболы: {quadratic_estimate_1980.round()}")
print(f"Исследование параболой выявило расхождение с данными на: {quadratic_estimate_1980.round()-known_population_1980}")
print(f"Оценка населения в 1980 году с использованием кубического полинома: {cubic_estimate_1980.round()}")
print(f"Исследование полиномом выявило расхождение с данными на: {cubic_estimate_1980.round()-known_population_1980}")

plt.show()
