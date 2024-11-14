import numpy as np
import matplotlib.pyplot as plt
import random
def f(w):
    return np.dot(w, w.transpose()) + 2

def random_direction(n):
    direction = np.random.randn(n)# случайный вектор из нормального распределения в n+1 размерности
    direction /= np.linalg.norm(direction)# нормализация вектора
    return direction #убери это?......

def random_search_const_step(w, n, p):
    f_min = float('inf')
    values = []
    coordinates = []
    right_coordinates = [0,0]
    for i in range(p):
        next_point = point + random_direction(n)
        if f(next_point) < f(point):
            values.append(f(next_point))
            coordinates.append(next_point)
    if values:
        m = len(values)/p
        return m
    return 0
    
point = np.array([[1]])
res_p0 = []
res_p1 = []
res_p2 = []
P = [100, 1000, 10000]
N = []
for i in range(1, 26):
    N.append(i)
    res_p0.append(random_search_const_step(point, i, 100))
    res_p1.append(random_search_const_step(point, i, 1000))
    res_p2.append(random_search_const_step(point, i, 10000))
    point = np.append(point, [0])

print(res_p0)

plt.plot(range(1, 26), res_p0, marker='o', color = 'blue')
plt.plot(range(1, 26), res_p1, marker='x', color = 'red')
plt.plot(range(1, 26), res_p2, marker='s', color = 'green')           
plt.title('График количества направлений спуска')
plt.xlabel('Размерность N')
plt.ylabel('Кол-во направлений спуска, деленных на P')
plt.grid()
plt.show()

