import numpy as np
import matplotlib.pyplot as plt
import random

def f(w1,w2):
    return 100*(w1**2 - w2**2)**2 + (w1 - 1)**2

def random_search_const_step(v1, v2):
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

def random_search_decreasing_step(v1, v2, k):
    f_min = float('inf')
    values = []
    coordinates = []
    right_coordinates = [0,0]
    for i in range(1000): #количество P - направлений спуска
        angles = np.random.uniform(0, 2 * np.pi)
        x = np.cos(angles)
        y = np.sin(angles)
        if f(v1 + (x / k**(0.5)), v2 + (y / k**(0.5))) < f(v1, v2):
            values.append(f(v1 + (x / k**(0.5)), v2 + (y / k**(0.5))))
            coordinates.append([v1 + x,v2 + y])
    if values:
        f_min = min(values)  
        min_index = values.index(f_min) 
        right_coordinates = coordinates[min_index]
        return right_coordinates[0], right_coordinates[1], f_min
    return v1, v2, f(v1, v2)

i00 = 0 #координаты для проверки спуска
i01 = 0 
i1 = 3 #начальные координаты
i2 = 3
results_c = [f(i1, i2)]
results_d = [f(i1, i2)]
kk = 1
minimum_c = 1000
minimum_d = 1000

for i in range(50):
    i00 = i1
    i01 = i2
    i1, i2, minimum_c = random_search_const_step(i1, i2)
    if (i00 == i1 and i01 == i2): # or (minimum_c >= results_c[-1]):
        break
    results_c.append(minimum_c)

print(i1, i2, results_c[-1])
i00 = 0 #координаты для проверки спуска
i01 = 0 
i1 = 2 #начальные координаты
i2 = 2

for i in range(50):
    i00 = i1
    i01 = i2
    i1, i2, minimum_d = random_search_decreasing_step(i1, i2, kk)
    kk += 1
    if (i00 == i1 and i01 == i2) or (minimum_d >= results_d[-1]):
        break
    results_d.append(minimum_d)

print(i1, i2, results_d[-1])


plt.plot(range(0, len(results_c)), results_c, marker='o', color = 'blue')
plt.plot(range(0, len(results_d)), results_d, marker='x', color = 'red')
plt.title('График истории функции потерь')
plt.xlabel('Количество шагов K')
plt.ylabel('Минимальное значение g(w)')
plt.grid()
plt.show()
