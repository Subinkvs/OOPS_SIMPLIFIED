# Method overloading means having multiple methods with the same name but different parameters.
# *args allows the method to accept any number of arguments.


class Calculator:
    def add(self, *args):
        return sum(args)

# Usage
calc = Calculator()

print(calc.add(5))            # 5
print(calc.add(5, 10))        # 15
print(calc.add(5, 10, 20))    # 35
print(calc.add(1, 2, 3, 4, 5))# 15
