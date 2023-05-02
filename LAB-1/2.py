"""
_summary_: NUMPY
"""

import random

import numpy as np

print(np.array([1,2,3,4,5], float))
print(np.array([1,2,3,4.7,5], int))
print(np.array([[1,2,3],[4,5,6]], float).transpose())
print(np.reshape(np.array(np.linspace(34, 46, 10), int), (5,2)))

a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]], float)
b = np.reshape(np.array(list(a.flatten())[::-1], float), (3,4))
sqM = np.reshape(np.array(random.sample(list(np.linspace(0, 100, 100)), 9), int), (3,3))

print(a+b)
print(a*b)

print("--------"*6,"\n"*5)

#STATS
print(a)
print(np.mean(a, axis=1)) #ROW WISE
print(np.mean(a, axis=0)) #COL WISE
print(np.median(a.flatten()))
print(np.std(a.flatten()))


print(a[a>4])
