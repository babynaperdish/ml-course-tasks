import numpy as np
import matplotlib.pyplot as plt
import random

def f(n):
    return np.sin(3*n) + 0.3*(n**2)

def random_search(x_start):
    f_min = 100000
    x = x_start
    sign = 1 #напрпвление спуска
    step = 0.1 #длина шага
    
    if f(x_start - step) < f(x_start + step): #выбор направления спуска
        sign = -1
    for i in range(10):
        if f(x) < f_min:
            f_min = f(x)
            x += sign * step
        else:
            break
    return x, f_min

length = 11
nums = [0]*length
results = [[0,0]]*length
for i in range(length):
    nums[i] = random.uniform(-5, 5)
    results[i][0], results[i][1] = random_search(nums[i])
    print(results[i][0], results[i][1])

