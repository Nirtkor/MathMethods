import math
def bisect_method(fun, inter, eps):
    a, b = inter
    fa = fun(a)
    fb = fun(b)
    
    if fa * fb > 0.:
        print(f"Bad interval [{a}, {b}]")
        print(f"Bad interval [{fa}, {fb}]")
        return 0.
    
    while (b - a) / 2 > eps:
        c = (b + a) / 2
        fc = fun(c)
        
        if fc == 0.:
            break
        
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return (b + a) / 2


eps = 10 ** -6

def first_exercise():
    inter = [2, 3]
    def fun(x):
        return x ** 3 - 9
    
    ans = bisect_method(fun, inter, eps)
    print("fun => x**3 = 9, \nx = {0}".format(ans))

def second_exercise():
    inter = [1, 2]
    def fun(x):
        return 3 * x ** 3 + x ** 2 - x - 5
    ans = bisect_method(fun, inter, eps)
    print("fun => 3 * x ** 3 + x ** 2 - x - 5, \nx = {0}".format(ans))

def third_exercise():
    inter = [6, 7]
    def fun(x):
        return math.cos(x) ** 2 + 6 - x
    ans = bisect_method(fun, inter, eps)
    print("fun => cos(x) ** 2 + 6 - x, \nx = {0}".format(ans))

if __name__ == "__main__":
    first_exercise()
    second_exercise()
    third_exercise()



