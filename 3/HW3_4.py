import math
from HW3_1 import bisect_method

R = 1
volume = 1
target_volume = volume
tolerance = 1e-3 

def segment_volume(h):
    return math.pi * h**2 * (R - h / 3)

water_depth = bisect_method(lambda h: segment_volume(h) - target_volume, [0, 2 * R], tolerance)

print(f"Глубина воды в резервуаре: {water_depth:.3f} м")
