import numpy as np
from scipy import integrate

def f1(x):
    return x / np.sqrt(x**2 + 9)

def f2(x):
    return x**2 * np.log(x)

a1, b1 = 0, 4
a2, b2 = 1, 3

exact_value1, _ = integrate.quad(f1, a1, b1)
exact_value2, _ = integrate.quad(f2, a2, b2)

n_values = [16, 32]
for n in n_values:
    x1 = np.linspace(a1, b1, n + 1)
    y1 = f1(x1)
    trapezoidal_value1 = np.trapz(y1, x1)

    print("Для первой функции (n={0}):".format(n))
    print("Приближенное значение интеграла методом трапеций: {0}".format(trapezoidal_value1))
    print("Точное значение интеграла: {0}".format(exact_value1))
    print("Погрешность: {0}".format(abs(trapezoidal_value1 - exact_value1)))
    print("-" * 30)



for n in n_values:
    x2 = np.linspace(a2, b2, n + 1)
    y2 = f2(x2)
    trapezoidal_value2 = np.trapz(y2, x2)


    print("Для второй функции (n={0}):".format(n))
    print("Приближенное значение интеграла методом трапеций: {0}".format(trapezoidal_value2))
    print("Точное значение интеграла: {0}".format(exact_value2))
    print("Погрешность: {0}".format(abs(trapezoidal_value2 - exact_value2)))
    print("-" * 30)

