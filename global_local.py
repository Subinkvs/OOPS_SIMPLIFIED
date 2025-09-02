# global variables = variables that are shared and accessible across functions
# local variables = variables that belong only to the specific function


# global variables example

x = 10   # global variable

def add_five():
    return x + 5   # can access global variable inside function

print(add_five())  


# local variables example

def add():
    x = 5   # local variable example
    result = 5 + x
    return result

print(x)
print(add())
