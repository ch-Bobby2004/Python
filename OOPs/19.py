from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass  # we don't define HOW it starts

class Car(Vehicle):
    def start(self):
        print("Car started")  # actual implementation

class Bike(Vehicle):
    def start(self):
        print("Bike started")  # actual implementation

# Using objects
vehicles = [Car(), Bike()]
for v in vehicles:
    v.start()  # we just know it starts, no need to know internal details