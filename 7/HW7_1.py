def tridiag_solve(n, c, a, b, r):
    alpha = [0] * n
    beta = [0] * n
    x = [0] * n

    alpha[0] = a[0]
    beta[0] = r[0] / alpha[0]

    for i in range(1, n):
        alpha[i] = a[i] - c[i - 1] * b[i - 1] / alpha[i - 1]
        beta[i] = (r[i] - c[i - 1] * beta[i - 1]) / alpha[i]

    x[n - 1] = beta[n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = beta[i] - b[i] * x[i + 1] / alpha[i]

    return x

c = [1, 1, 1]
a = [2, 10, -5, 4]
b = [1, -5, 2]
r = [-5, -18, -40, -27]

print(tridiag_solve(4, c, a, b, r))
