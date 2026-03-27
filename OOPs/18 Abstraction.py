# Abstraction = showing only essential features and hiding unnecessary details

# You don’t show the “how it works”, only what it does
# Achieved in Python using abstract classes from the abc module



from abc import ABC, abstractmethod

class Vehicle(ABC):  # abstract class
    @abstractmethod
    def start(self):
        pass   # no details, just definition

class Car(Vehicle):
    def start(self):
        print("Car started")  # implementation

class Bike(Vehicle):
    def start(self):
        print("Bike started")  # implementation

c = Car()
c.start()

b = Bike()
b.start()


# Abstraction = show only what is necessary, hide the internal details