# function = a block of resuable code which only runs when it is called.
# function definition = def function_name():
# function call = function_name()


# parameters = variables that are passed into a function.
# arguments = the value that is sent to the function when it is called.



def greeting(name):
    print(f"Hello, {name}!")

greeting("Alice")
greeting("Bob")
greeting("Charlie")


def add(num1, num2):
    print(num1 + num2)

add(5, 10)
add(20, 30)
add(-5, 15)


# return statement = function sends a value back to the caller.
# These values are known as the function's return value.

def multiply(num1, num2):
    a = num1 * num2
    return a

x = multiply(5, 10)




print(x)
print(multiply(20, 30))
