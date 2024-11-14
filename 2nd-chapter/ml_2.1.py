import numpy as np
import matplotlib.pyplot as plt

def g(w):
    return np.dot(w, w)

def rand(p):
   for N in range(1, N_max + 1):
       # Генерируем P случайных точек в гиперкубе [-1, 1]^N
        W = np.random.uniform(-1, 1, (p, N))
       # Вычисляем значения функции g для каждой точки
        values = np.array([g(w) for w in W])
       # Находим минимальное значение
        min_values.append(np.min(values))
N_max = 100
P = 100
P1 = 1000
P2 = 10000
min_values = []

rand(P)
plt.plot(range(1, N_max + 1), min_values, marker='o', color = 'blue')
min_values = []
rand(P1)
plt.plot(range(1, N_max + 1), min_values, marker='x', color = 'red')
min_values = []
rand(P2)
plt.plot(range(1, N_max + 1), min_values, marker='s', color = 'green')
plt.title('Минимальные значения квадратичных функций против размерности N')
plt.xlabel('Размерность N')
plt.ylabel('Минимальное значение g(w)')
plt.grid()
plt.show()
