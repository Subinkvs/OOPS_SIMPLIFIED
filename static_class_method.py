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
