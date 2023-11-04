from HW8_1 import jacoby

def exact_solution(n):
    return [1] * n

n_values = [100, 100000]
for n in n_values:
    c = [-1] * (n - 1)
    a = [-1] * (n - 1)
    b = [3] * n
    r = [2] + [1] * (n - 2) + [2]
    x0 = [0] * n
    eps = 1e-6
    max_iter = 1000

    print(f"n = {n}:")
    result = jacoby(c, a, b, r, x0, eps, max_iter)
    exact = exact_solution(n)
    print("Число итераций: {0}".format(max_iter))
    print("Прямая ошибка на последней итерации: {0}".format(max(abs(result[i] - exact[i]) for i in range(n))))
    print("Обратная ошибка на последней итерации: {0}".format(max(abs((result[i] - exact[i]) / exact[i]) for i in range(n))))
