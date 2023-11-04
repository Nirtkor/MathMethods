def gauss_seidel(c, a, b, r, x0, eps, max_iter):
    n = len(b)
    x = x0.copy()
    for iter_count in range(max_iter):
        x_new = x.copy()
        for i in range(n):
            if i == 0:
                x_new[i] = (r[i] - a[i] * x_new[i + 1]) / b[i]
            elif i == n - 1:
                x_new[i] = (r[i] - c[i - 1] * x_new[i - 1]) / b[i]
            else:
                x_new[i] = (r[i] - c[i - 1] * x_new[i - 1] - a[i] * x_new[i + 1]) / b[i]

        error = max(abs((x_new[i] - x[i]) / x_new[i]) for i in range(n)) if any(x_new) else float('inf')

        x = x_new
        if error < eps:
            return x
    return x
