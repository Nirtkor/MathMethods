from HW3_1 import bisect_method

def cube_root_bisection(number, tolerance=1e-8):
    equation = lambda x: x**3 - number
    root = bisect_method(equation, [0, number], tolerance)
    return root

number_2_root = cube_root_bisection(2)
number_3_root = cube_root_bisection(3)
number_5_root = cube_root_bisection(5)

print(f"Кубический корень числа 2: {number_2_root:.8f}")
print(f"Кубический корень числа 3: {number_3_root:.8f}")
print(f"Кубический корень числа 5: {number_5_root:.8f}")
