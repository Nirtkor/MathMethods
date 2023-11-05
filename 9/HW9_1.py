import numpy as np
import matplotlib.pyplot as plt

def interpolate_and_plot(x, y):
    p = np.polyfit(x, y, len(x) - 1)
    poly = np.poly1d(p)
    x_new = np.linspace(min(x), max(x), 100)
    y_new = poly(x_new)

    plt.figure(figsize=(8, 6))
    plt.plot(x, y, 'o', label='Исходные данные')
    plt.plot(x_new, y_new, label='полином, задача 1', linestyle='dashed')
    plt.title('полином, задача 1')
    plt.xlabel('Год')
    plt.ylabel('CO2')
    plt.legend()
    plt.grid()
    plt.show()

x_data = [1800, 1850, 1900, 2000]
y_data = [280, 283, 291, 370]
interpolate_and_plot(x_data, y_data)
