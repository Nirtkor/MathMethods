import math
import matplotlib.pyplot as plt
from HW3_1 import bisect_method

equations = {
    "1) 2x^3 - 6x - 1 = 0": {
        "equation": lambda x: 2 * x ** 3 - 6 * x - 1,
        "range": [-10, 10]
    },
    "2) e^(x - 2) + x^3 - x = 0": {
        "equation": lambda x: math.exp(x - 2) + x ** 3 - x,
        "range": [-10, 10]
    },
    "3) 1 + 5x - 6x^3 - e^(2x) = 0": {
        "equation": lambda x: 1 + 5 * x - 6 * x ** 3 - math.exp(2 * x),
        "range": [-10, 10]
    }
}

def find_roots(equation, x_range, tolerance):
    roots = []
    a, b = x_range[0], x_range[1]
    x = a
    step = 0.01
    while x <= b:
        if equation(x) * equation(x + step) < 0:
            root = bisect_method(equation, [x, x + step], tolerance)
            roots.append(root)
        x += step
    return roots

def plot_and_save_graph(function, filename, roots):
    x = [i for i in range(-10, 11)]
    y = [function(i) for i in x]
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(filename)
    for root in roots:
        plt.axvline(x=root, color='r', linestyle='--', label=f'Root: {root:.6f}')
    plt.legend()
    plt.savefig(filename)
    plt.close()

for title, data in equations.items():
    equation = data["equation"]
    equation_range = data["range"]
    result = find_roots(equation, equation_range, 1e-6)
    
    print(title)
    print(f"Roots: {result}\n")
    
    filename = title + '.png'
    plot_and_save_graph(equation, filename, result)
