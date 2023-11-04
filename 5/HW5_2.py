import math
from HW5_1 import newton

tolerance = 10**-6

def func(r):
    return (math.pi * r**2 * 10) / 3 + (2 * math.pi * r**3) / 3 - 60

def dif_func(r):
    return (2 * math.pi * r * (r + 10)) / 3

radius = newton(func, dif_func, 1, tolerance)

print("Радиус полусферы: {0} см".format(radius))






