# write a function that calls another function for addition of two numbers ?

def add(x, y):
    result = operate(x, y)
    return result

def operate(a, b):
    x = a + b
    return x

print(add(10, 20))
x = add(5, 10)
print(x)

