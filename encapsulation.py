# ------------------ Encapsulation in OOP ------------------
# 1. Encapsulation is the process of wrapping data (variables) and 
#    methods (functions) into a single unit (class).
#
# 2. It restricts direct access to some variables and methods, 
#    which helps protect data and control how it is modified.
#
# 3. In Python, encapsulation is implemented using:
#    - Public members    (accessible everywhere)
#    - Protected members (prefix with a single underscore "_var")
#    - Private members   (prefix with double underscore "__var")
#
# 4. Benefits of Encapsulation:
#    - Data hiding (restricts accidental modification)
#    - Better control over attributes
#    - Increased security
#    - Flexibility for future changes (using methods instead of direct access)



class Student:
    def __init__(self, name, marks, age):
        self.name = name              # public
        self._age = age               # protected (convention: don’t touch outside class/subclass)
        self.__marks = marks          # private (cannot access directly outside class)

    def show_details(self):
        print(f"Name: {self.name}, Age: {self._age}, Marks: {self.__marks}")


s1 = Student("Alice", 85, 20)

# ✅ Public variable: accessible everywhere
print(s1.name)    # Alice

# ⚠️ Protected variable: can access, but not recommended
print(s1._age)    # 20

# ❌ Private variable: direct access not allowed
# print(s1.__marks)   # AttributeError

# ✅ Access private variable indirectly (through method inside class)
s1.show_details()   # Name: Alice, Age: 20, Marks: 85
