# recursion = function that calls itself

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1) # function calling itself               
print(factorial(5))
print(factorial(3))
print(factorial(1))