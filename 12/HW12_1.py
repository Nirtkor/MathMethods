import math


def f1(x):
    return x / math.sqrt(x**2 + 9)

def f2(x):
    return x**2 * math.log(x)

def simpson_method(f, a, b, m):
    h = (b - a) / m
    result = f(a) + f(b)
    for i in range(1, m):
        if i % 2 == 0:
            result += 2 * f(a + i * h)
        else:
            result += 4 * f(a + i * h)
    result *= h / 3
    return result

a1, b1 = 0, 4
a2, b2 = 1, 3

integral1_m16 = simpson_method(f1, a1, b1, 16)
integral1_m32 = simpson_method(f1, a1, b1, 32)
integral2_m16 = simpson_method(f2, a2, b2, 16)
integral2_m32 = simpson_method(f2, a2, b2, 32)


print("Интеграл а при m=16: {0}".format(integral1_m16))
print("Интеграл а при m=32: {0}".format(integral1_m32))
print("Интеграл б при m=16: {0}".format(integral2_m16))
print("Интеграл б при m=32: {0}".format(integral2_m32))

