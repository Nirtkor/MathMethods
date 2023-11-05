import numpy as np
import matplotlib.pyplot as plt

years = np.array([1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003])
production = np.array([67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777])

poly_coeffs = np.polyfit(years, production, 9)
poly = np.poly1d(poly_coeffs)
estimated_production_2010 = poly(2010)
x_values = np.linspace(1994, 2010, 100)
y_values_poly = poly(x_values)

plt.figure(figsize=(10, 6))
plt.plot(years, production, 'o', label='Исходные данные')
plt.plot(x_values, y_values_poly, label='Полином степени 9', linestyle='dashed')
plt.title('Добыча нефти по годам')
plt.xlabel('Год')
plt.ylabel('Добыча нефти (миллионы баррелей в день)')
plt.legend()
plt.grid()

print(f"Оценка добычи нефти в 2010 году: {estimated_production_2010}")
plt.show()

# Значительное проявление феномена Рунге обнаружено не было.
# Считаю, что полином недостаточно точно демонстрирует оценку добычи, данные довольно сильно искажены в большую сторону.
