# Inheritance allows a class (child class) to use the properties and methods of another class (parent class).
# This helps in code reusability and creating a logical hierarchy.

# Parent Class
class Animal:
    def speak(self):
        print("This animal makes a sound.)"

# Child Class (inherits from Animal)
class Dog(Animal):
    # method overrding
    def speak(self):
        print("The dog barks.")

# Usage
animal = Animal()
dog = Dog()

print(animal.speak())  # Calls parent class method
print(dog.speak())     # Calls child class method (overrides parent)




A company has different types of employees: general employees, developers, and managers.

 1  Every employee has a name and a salary.

 2  Developers also have a programming language they specialize in.

 3  Managers have a team size they manage.

? Write a Python program using inheritance where:

   1 Employee is the base class that stores name and salary.

   2 Developer and Manager are child classes that inherit from Employee.

   3 Each class should have a method show_details() that prints employee information.

        For Employee: print name and salary.

        For Developer: print name, salary, and programming language.

        For Manager: print name, salary, and team size.

   4  Create one object each of Employee, Developer, and Manager and display their details.



 # Use super() to call parent class constructor
 super().__init__(name, salary)

















# Parent Class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_details(self):
        return f"Name: {self.name}, Salary: ₹{self.salary}"


# Child Class 1 (inherits from Employee)
class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        # Use super() to call parent class constructor
        super().__init__(name, salary)
        self.programming_language = programming_language
    
    def show_details(self):
        # Overriding parent method
        return f"Developer: {self.name}, Salary: ₹{self.salary}, Language: {self.programming_language}"


# Child Class 2 (inherits from Employee)
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size
    
    def show_details(self):
        # Overriding parent method


        return f"Manager: {self.name}, Salary: ₹{self.salary}, Team Size: {self.team_size}"


# ---- Usage ----
# Create objects of each class
emp1 = Employee("Rahul", 30000)
dev1 = Developer("Subin", 50000, "Python")
mgr1 = Manager("Anjali", 70000, 10)

# Print details
print(emp1.show_details())  # From Employee class
print(dev1.show_details())  # From Developer (overrides Employee)
print(mgr1.show_details())  # From Manager (overrides Employee)
