import numpy as np
import matplotlib.pyplot as plt
import random

def f(w1,w2):
    return np.tanh(4*w1 + 4*w2) + max(0.4*w1**2, 1) + 1

def random_search(v1, v2):
    f_min = float('inf')
    values = []
    coordinates = []
    right_coordinates = [0,0]
    for i in range(1000):
        angles = np.random.uniform(0, 2 * np.pi)
        x = np.cos(angles)
        y = np.sin(angles)
        if f(v1 + x, v2 + y) < f(v1, v2):
            values.append(f(v1 + x, v2 + y))
            coordinates.append([v1 + x,v2 + y])
    if values:
        f_min = min(values)  
        min_index = values.index(f_min) 
        right_coordinates = coordinates[min_index]
        return right_coordinates[0], right_coordinates[1], f_min
    return v1, v2, f(v1, v2)

i00 = 0
i01 = 0
i1 = 2
i2 = 2
minimum = 1000
for i in range(8):
    i00 = i1
    i01 = i2
    i1, i2, minimum = random_search(i1, i2)
    if i00 == i1 + i01 == i2:
        break

print(i1, i2, minimum)
