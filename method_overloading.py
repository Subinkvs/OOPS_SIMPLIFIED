# Method overloading means having multiple methods with the same name but different parameters.
# *args allows the method to accept any number of arguments.(for variable number of positional arguments).


class Calculator:
    def add(self, *args):
        return sum(args)

# Usage
calc = Calculator()



print(calc.add(5))            # 5
print(calc.add(5, 10))        # 15
print(calc.add(5, 10, 20))    # 35
print(calc.add(1, 2, 3, 4, 5))# 15




# **kwargs allows the method to accept any number of arguments.(for variable number of keyword arguments).


class Calculator:
    def add(self, **kwargs):
        print("kwargs received:", kwargs)   # just to see what happens
        return sum(kwargs.values())


# Usage
calc = Calculator()

print(calc.add(a=5))                  
print(calc.add(x=5, y=10))            
print(calc.add(num1=5, num2=10, num3=20))   
print(calc.add(n1=1, n2=2, n3=3, n4=4, n5=5)) 

