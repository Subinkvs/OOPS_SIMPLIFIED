class Parent:

    def operation(self, x, y): # 8, 5
        result = x + y         # x = 8, y = 5,  x + y = 8 +5
        print(result)          #                      = 13

class Child(Parent):
    
    def operation(self, x, y):
        result = x - y
        print(result)

obj = Parent()
obj.operation(8, 5)  # 13

obj1 = Child()
obj1.operation(5, 4) #3



# polymorphism - method overloading, method overriding

