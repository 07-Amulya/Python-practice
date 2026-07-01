"""
file1.py
x = 10

main.py
import file1
print(file1.x)



maths.py
def add(a, b):
    return a + b

main.py
from maths import add
print(add(2, 3))



demo.py
x = 5

main.py
import demo as d
print(d.x)



sample.py
a = 100

main.py
from sample import a
a = 200
print(a)



calc.py
def show():
    print("Hello")

main.py
from calc import *
show()


import math
print(math.sqrt(16))



import random
random.seed(1)
print(random.randint(1, 5))



test.py
print("Loaded")

main.py
import test
import test
"""