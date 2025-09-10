# getter = a method used to access (read) the value of a private variable.
# setter = a method used to update (write) the value of a private variable.

# private variable = a variable declared with double underscore (__) 
#                    to restrict direct access from outside the class.

# encapsulation = the OOP principle of hiding internal data and 
#                 providing controlled access using getters and setters.


class Person:
    def __init__(self, name, age):
        self.__name = name   # private variable
        self.__age = age

    # Getter
    def get_name(self):
        return self.__name
        

    def get_age(self):
        return self.__age

    # Setter
    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age




# Example usage
p1 = Person("Rahul", 28)

print("Name:", p1.get_name())   # Getter
print("age:", p1.get_age())

p1.set_name("John")           # Setter
p1.set_age(29)
print("Updated Name:", p1.get_name())
print("Updated age:", p1.get_age())
