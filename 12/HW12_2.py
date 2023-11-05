import math
from HW12_1 import simpson_method

def f1(x):
    return x**3

def f2(x):
    return math.sin(x)


a1, b1, m1 = 0, 1, 32
a2, b2, m2 = 0, math.pi, 32

length1 = simpson_method(lambda x: math.sqrt(1 + 9 * x**4), a1, b1, m1)
length2 = simpson_method(lambda x: math.sqrt(1 + math.cos(x)**2), a2, b2, m2)

print("Длина кривой для a]: {}".format(length1))
print("Длина кривой для b: {}".format(length2))

