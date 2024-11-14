import numpy as np
import matplotlib.pyplot as plt
import random

def f(w):
    return np.dot(w, w.transpose()) + 2

def random_direction(n):
    direction = np.random.randn(n)  # случайный вектор из нормального распределения в n+1 размерности
    direction /= np.linalg.norm(direction)# нормализация вектора
    return direction #убери это?......

def random_search_const_step(prev_point, n):
    f_min = float('inf')
    values = []
    coordinates = []
    right_coordinates = [0,0]
    for i in range(1000):
        next_point = prev_point + random_direction(N)
        if f(next_point) < f(prev_point):
            values.append(f(next_point))
            coordinates.append(next_point)
    if values:
        m = len(values)/i
        return m
    return 0


N = 3
point = np.array([[0]*N for i in range(1)])
point[0][0] = 1
print(point)
print(random_search_const_step(point, N)< 0.5*((3**0.5)/2)**(N-1))

