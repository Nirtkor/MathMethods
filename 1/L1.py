# def horner(n, a, x):
#     y=a[n]
#     for i in range(n):
#         y = y * x + a[n-i-1]
#     return y

# o = []
# for i in range(100):
#     if i % 2 == 0:
#         o.append(1)
#     else:
#         o.append(-1)

# x = 1.00001
# x_1 = horner(99, o, x)

# x_2 = (1-x**100)/(1+x)

# different = x_2 - x_1

# print('Стандартный метод решения полинома:', x_1)
# print('Упрощенный метод решения полинома:', x_2)
# print('Разница:', different)

# print((1+(2**-51+2**-52+2**-54))-1)
# print((1+(2**-52+2**-53+2**-60))-1)

# import math

# result = math.sqrt(9.01) - 3
# rounded_result = round(result, 5)

print(rounded_result)

from decimal import Decimal, getcontext

# Установим точность до 4-х десятичных знаков
getcontext().prec = 6

# Вычисление первого выражения
a1 = Decimal("-12345678987654321")
b1 = Decimal("123")
result1 = a1 + (b1**2 + b1**2) / (a1**2 + b1**2).sqrt()
# Вычисление второго выражения
a2 = Decimal("2468864224688642")
b2 = Decimal("13579")
result2 = (a2**2 + b2**2).sqrt() - a2

print(f"Результат первого выражения: {result1:.4f}")
print(f"Результат второго выражения: {result2:.4f}")