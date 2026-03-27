# A class-level parameter is a variable shared by all objects of that class.
# Unlike instance variables, which are unique to each object, class variables are common to all objects.

class Car:
    wheels = 4  # class-level parameter (same for all cars)

    def __init__(self, brand):
        self.brand = brand  # instance variable (unique per object)

car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.brand, car1.wheels)  # Toyota 4
print(car2.brand, car2.wheels)  # BMW 4


# Defined inside class but outside __init__
# Shared by all objects
# Can be accessed via class name or object