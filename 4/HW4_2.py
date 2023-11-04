from HW4_1 import simple_iteration

tolerance = 1e-8
max_iterations = 1000

def func_a(x):
    return (2*x + 2/x**2) / 3

def func_b(x):
    return (2*x + 3/x**2) / 3

def func_c(x):
    return (2*x + 5/x**2) / 3

print("For A=2:")
solution_a, iterations_a = simple_iteration(func_a, 1)
print("Root:", solution_a)
print("Iterations:", iterations_a)

print("\nFor A=3:")
solution_b, iterations_b = simple_iteration(func_b, 1)
print("Root:", solution_b)
print("Iterations:", iterations_b)

print("\nFor A=5:")
solution_c, iterations_c = simple_iteration(func_c, 1)
print("Root:", solution_c)
print("Iterations:", iterations_c)
