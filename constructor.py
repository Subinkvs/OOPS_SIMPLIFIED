# Using a constructor makes your class more organized, stateful, and scalable
# In larger programs with multiple attributes and methods, constructors are extremely useful.
# Constructors save you from passing values repeatedly and make the object self-contained and organized.

class Calculate:

    def __init__(self, a):
        self.a = a

    def area(self):
        result = self.a ** 2
        return result

    def perimeter(self):
        result = 4 * self.a
        return result

obj = Calculate(2)
print(obj.area())
print(obj.perimeter())



# Employee System

class Employee:
    def show_details(self):
        print(self.name, self.emp_id, self.salary, self.department)

# Create object
emp = Employee()
emp.name = "Bob"
emp.emp_id = 101
emp.salary = 50000
emp.department = "IT"

emp.show_details()  # Output: Bob 101 50000 IT


class Employee:

    def __init__(self, name, emp_id, salary, department):
        self.name = name 
        self.emp_id = emp_id
        self.salary = salary
        self.department = department

    def show_details(self):
        return f"{self.name}, {self.emp_id}, {self.salary}, {self.department}"

emp = Employee('Rahul', 222, 20000, 'IT')
print(emp.show_details())




