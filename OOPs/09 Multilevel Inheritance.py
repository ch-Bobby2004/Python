class Grandfather:
    def house(self):
        print("Big House")

class Father(Grandfather):
    def car(self):
        print("Car")

class Child(Father):
    def bike(self):
        print("Bike")

c = Child()
c.house()
c.car()
c.bike()