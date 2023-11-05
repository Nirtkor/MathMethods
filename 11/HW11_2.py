import numpy as np


def f1(x):
    return x / np.sin(x)

def f2(x):
    return np.arctan(x) / x

def midpoint_rule_integration(func, a, b, n):
    h = (b - a) / n
    integral_sum = 0
    for i in range(n):
        midpoint = (a + h * (i + 0.5))
        integral_sum += func(midpoint)
    return h * integral_sum


a1, b1 = 0, np.pi / 2
a2, b2 = 0, -1

n_values = [16, 32]
for n in n_values:
    rectangle_value1 = midpoint_rule_integration(f1, a1, b1, n)
    rectangle_value2 = midpoint_rule_integration(f2, a2, b2, n)

    print("Для первой функции (n={0}):".format(n))
    print("Приближенное значение интеграла методом центральных прямоугольников: {0}".format(rectangle_value1))
    print("-" * 30)

    print("Для второй функции (n={0}):".format(n))
    print("Приближенное значение интеграла методом центральных прямоугольников: {0}".format(rectangle_value2))
    print("-" * 30)

