from HW8_3 import gauss_seidel

def exact_solution(n):
    return [1 if i % 2 == 0 else -1 for i in range(n)]

n = 100
c = [1] * (n - 1)  # Нижняя диагональ
a = [1] * (n - 1)  # Верхняя диагональ
b = [2] * n  # Главная диагональ
r = [1] + [0] * (n - 2) + [-1]  # Вектор правой части
x0 = [0] * n  # Начальное приближение
eps = 1e-3  # Требуемая точность
max_iter = 1000  # Максимальное количество итераций

print(f"n = {n}:")
result = gauss_seidel(c, a, b, r, x0, eps, max_iter)
exact = exact_solution(n)
print("Число итераций: {0}".format(max_iter))
print("Прямая ошибка на последней итерации: {0}".format(max(abs(result[i] - exact[i]) for i in range(n))))
print("Обратная ошибка на последней итерации: {0}".format(max(abs((result[i] - exact[i]) / exact[i]) for i in range(n))))
