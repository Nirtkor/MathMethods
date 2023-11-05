import numpy as np
import matplotlib.pyplot as plt

years = np.array([1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003])
production = np.array([67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777])

# метод лагранжа:
def lagrange_interpolation(x, y, x_val):
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_val - x[j]) / (x[i] - x[j])
        result += term
    return result


estimated_production_1998 = lagrange_interpolation(years[:4], production[:4], 1998)

x_values = np.linspace(1994, 2003, 100)
y_values = lagrange_interpolation(years[:4], production[:4], x_values)

plt.figure(figsize=(10, 6))
plt.plot(years, production, 'o', label='Исходные данные')
plt.plot(x_values, y_values, label='Интерполяционный полином', linestyle='dashed')
plt.scatter(1998, estimated_production_1998, color='red', label='Оценка 1998')
plt.title('Добыча нефти по годам')
plt.xlabel('Год')
plt.ylabel('Добыча нефти (миллионы баррелей в день)')
plt.legend()
plt.grid()


print(f"Оценка добычи нефти в 1998 году: {estimated_production_1998}")
plt.show()
