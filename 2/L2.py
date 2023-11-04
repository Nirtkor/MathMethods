def fixed_iter(fun, x0, n): 
    x = x0
    for i in range(n):
        print("xk=",x," f(xk)=",fun(x))
        x = fun(x)
        return x 
def func(x):
    return (1-x)**(1./3.)
x0 = 0.6
n = 30
z = fixed_iter(func, x0, n) 
print("z = ", z) 
print("f(z) = ", func(z))