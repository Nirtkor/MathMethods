import math

tolerance = 1e-8
max_iterations=100000

def function_a(x):
    return (2*x + 2)**(1/3)

def function_b(x):
    return 7 - math.exp(x)

def function_c(x):
    return math.log(4 - math.sin(x))

def simple_iteration(func, initial_value):
    x0 = initial_value
    for i in range(max_iterations):
        x1 = func(x0)
        if abs(x1 - x0) < tolerance:
            return x1, i+1
        x0 = x1
    return None, max_iterations

print("F(Z) (a):")
solution_a, iterations_a = simple_iteration(function_a, 1)
print("Root:", solution_a)
print("Iterations:", iterations_a)

print("\nF(Z) (b):")
solution_b, iterations_b = simple_iteration(function_b, -100)
print("Root:", solution_b)
print("Iterations:", iterations_b)

print("\nF(Z) (c):")
solution_c, iterations_c = simple_iteration(function_c, 1)
print("Root:", solution_c)
print("Iterations:", iterations_c)
