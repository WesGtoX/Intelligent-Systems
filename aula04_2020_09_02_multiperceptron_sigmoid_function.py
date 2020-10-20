# -*- coding: utf-8 -*-
"""aula04_2020_09_02_multiperceptron_sigmoid_function.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oyuif4VELbhe2mrG51cjPGYZNWWwMWPO
"""

import math
import time

"""## MULTIPERCEPTRON AND SIGMOID FUNCTION"""

# structure changes to xor

start = time.time()

matrix_input = [[0, 0], [0, 1], [1, 0], [1, 1]]
l3 = 1.0

w1 = -70.0
w2 = -20.0
w3 = 90.0
w4 = 40.0
w5 = 50.0
w6 = 10.0

t1, t2, t3 = 8.0, 3.0, 5.5
t1, t2, t3 = 80.0, -20.0, -55.0

print(f'l1\tl2\to1\to2\to3')
print(39 * '-')

for l1, l2 in matrix_input:
    o1 = l1
    o2 = l2
    o3 = l3

    l1 = o1 * w1 + o2 * w2 + o3 * t1
    l2 = o1 * w3 + o2 * w4 + o3 * t2
    l3 = 1.0

    o1 = 1.0 / (1.0 + math.exp(-l1))
    o2 = 1.0 / (1.0 + math.exp(-l2))
    o3 = l3

    l1 = o1 * w5 + o2 * w6 + o3 * t3
    o3 = 1.0 / (1.0 + math.exp(-l1))
    print(f'{l1:.1f}\t{l2:.1f}\t{o1:.0f}\t{o2:.0f}\t{o3:.5f}')

end = time.time()

runtime = end - start
print(f'\nRuntime: {runtime:.10f} seconds')

# OUTPUT
# l1     l2     o1  o2  o3
# -----------------------------
# -5.0   -20.0  1   0   0.00669
# 5.0    20.0   1   1   0.99331
# 5.0    70.0   1   1   0.99329
# -45.0  110.0  0   1   0.00000
# 
# Runtime: 0.0006272793 seconds