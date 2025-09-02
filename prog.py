# POP = Procedure Oriented Programming is a programming paradigm that uses functions and procedures 
# for structuring code.
# function = block of code that performs a specific task
# procedure = set of instructions written in a sequential manner to solve a problem
# data = functions act on data, but data and functions are separate
# main program = execution starts from top to bottom, calling functions as needed


# POP: Function-based
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(add(5, 3))       # 8
print(multiply(5, 3))  # 15


# OOP = object oriented programming is a programming paradigm that uses objects and classes for 
# structuring code.

# class = blueprint for creating objects
# object = instance of a class

# method = function that is defined inside a class
# self = instance of the class
# __init__() = special method that is called when the object is created (constructor) to initialize
# value to the object and the object remembers the value
# attributes = variables that belong to the class


# OOP: Class-based
class Calculator:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def multiply(self):
        return self.a * self.b

calc = Calculator(5, 3)
print(calc.add())       
print(calc.multiply())  




