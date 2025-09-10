# instance method = a method that works with individual object data. 
#                   requires 'self' as the first parameter. 

# class method = a method that works with class-level data (shared across all objects).
#                requires 'cls' as the first parameter.
#                defined using the @classmethod decorator.

# static method = a utility method that belongs to the class but does not use
#                 object (self) or class (cls) data.
#                 defined using the @staticmethod decorator.


class Student:
    count = 0   # class variable

    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age
        Student.count += 1


    # Instance Method (works with object data using self)
    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

    # Class Method (works with class data using cls)
    @classmethod
    def total_students(cls):
        return f"Total students: {cls.count}"

    # Static Method (general utility, no self or cls)
    @staticmethod
    
    def is_adult(age):
        return age >= 18


# Usage
s1 = Student("Rahul", 22)
s2 = Student("John", 17)
s3 = Student("Sandra", 19)

# Instance method -> called on objects
print(s1.display_info())     # Name: Subin, Age: 22
print(s2.display_info())     # Name: Sundar, Age: 17

# Class method -> called on class (or object, but usually class)
print(Student.total_students())   # Total students: 2

# Static method -> called on class (or object, but usually class)
print(Student.is_adult(22))   # True
print(Student.is_adult(15))   # False


Q1.Employee Management System

Create a class Employee with the following:

An instance method show_details() that prints the employee’s name and salary.

A class method change_company(cls, new_company) that updates the company name for all employees.

A static method is_valid_salary(salary) that checks if the salary is greater than 0 (return True if valid, else False).

👉 Task:

1. Create 3 employees.

2.Check if a salary is valid using the static method.

3.Change the company name using the class method and verify that it is updated for all employees.
















Q2.Bank Account System

Create a class BankAccount with the following:

An instance method deposit(amount) that adds money to the account balance.

A class method set_interest_rate(cls, rate) that updates the interest rate for all accounts.

A static method bank_policy() that prints a simple bank policy message (e.g., "Minimum balance should be 1000").


👉 Task:

1.Create two accounts and deposit money.

2.Update the interest rate using the class method and check that it applies to all accounts.

3.Call the static method to display the policy.