import numpy as np
import matplotlib.pyplot as plt
import random

def f(w):
    return np.dot(w, w.transpose()) + 2

def random_direction(n):
    direction = np.random.randn(n)  # случайный вектор из нормального распределения в n+1 размерности
    direction /= np.linalg.norm(direction)# нормализация вектора
    return direction

def coordinate_search_const_step(prev_point, n, cs, a): # 2.7 
    f_min = float('inf')
    values = []
    coordinates = []
    right_coordinates = [0] * n
    for i in range(len(cs)):
        next_point = prev_point + cs[i] * a
        if f(next_point) < f(prev_point):
            values.append(f(next_point))
            coordinates.append(next_point)
    if values:
        f_min = min(values)  
        min_index = values.index(f_min) 
        right_coordinates = coordinates[min_index]
        return right_coordinates, f_min
    return prev_point, f(prev_point)

def random_search_const_step(prev_point, n, a):
    f_min = float('inf')
    values = []
    coordinates = []
    right_coordinates = [0,0]
    for i in range(1000):
        next_point = prev_point + random_direction(N)*(a**0.5)
        if f(next_point) < f(prev_point):
            values.append(f(next_point))
            coordinates.append(next_point)
    if values:
        f_min = min(values)  
        min_index = values.index(f_min) 
        right_coordinates = coordinates[min_index]
        return right_coordinates, f_min
    return prev_point, f(prev_point)


N = 2
L = 1
point = np.array([3, 4])
checkpoint = None
vectors = [[0]*N for _ in range(2*N)]
for i in range(0, 2*N, 2):
    vectors[i][i//2] = -1
    vectors[i + 1][i//2] = 1
for i in range(7):
    checkpoint = point.copy()
    point, fm = coordinate_search_const_step(point, N, vectors, L)
    if np.array_equal(point, checkpoint):
        break
print(point, fm)

point = np.array([3, 4])
checkpoint = None
for i in range(7):
    checkpoint = point.copy()
    point, fm = random_search_const_step(point, N, L)
    if np.array_equal(point, checkpoint):
        break
print(point, fm)

