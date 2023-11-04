import math

def newton(func, dif_func, x0, e):
    count = 0
    x = x0
    f_x = func(x)
    df_x = dif_func(x)
    while abs(f_x / df_x) > e:
        count += 1
        x = x - f_x / df_x
        f_x = func(x)
        df_x = dif_func(x)
    return x

tolerance = 10**-8

def func_a(x):
    return x**5 + x - 1

def dif_func_a(x):
    return 5 * x**4 + 1

root_a = newton(func_a, dif_func_a, 1, tolerance)
print("Корень уравнения (a): {0}".format(root_a))

def func_b(x):
    return math.sin(x) - 6 * x - 5

def dif_func_b(x):
    return math.cos(x) - 6

root_b = newton(func_b, dif_func_b, 1, tolerance)
print("Корень уравнения (b): {0}".format(root_b))

def func_c(x):
    return math.log(x) + x**2 - 3

def dif_func_c(x):
    return 1 / x + 2 * x

root_c = newton(func_c, dif_func_c, 1, tolerance)
print("Корень уравнения (c): {0}".format(root_c))
