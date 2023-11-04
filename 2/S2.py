def fixed_iter(fun, x0, n):
    x = x0
    for i in range(n):
        print("xk=" ,x, "f(kx)=", fun(x))
        x = fun(x)
    return x
