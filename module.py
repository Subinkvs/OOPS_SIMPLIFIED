# A module in Python is just a .py file that contains functions, classes, or 
# variables which you can import and reuse in another file.
# syntax -> import module name
from math_mod import *


obj = Calculator()

print(obj.add(5, 6)) # modulename.function
print(obj.substract(6, 5))
print(obj.multiplication(5, 5))
print(obj.division(5, 2))

