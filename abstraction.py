# Abstraction = Hiding the internal implementation and showing only the necessary details to the user.

from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):  
    @abstractmethod
    def start(self):   # Abstract method (no implementation here)
        pass

# Concrete Class 1
class Car(Vehicle):
    def start(self):
        print("Car engine started with a key 🔑")

# Concrete Class 2
class Bike(Vehicle):
    def start(self):
        print("Bike started with a kick 🚴")

# Usage
v1 = Car()
v1.start()   # Car engine started with a key 🔑

v2 = Bike()
v2.start()   # Bike started with a kick 🚴

