class Car:
    def start(self):
        print("Car started")

car1 = Car()
car1.start()



class Car:
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
print(car1.brand)



# __init__ Method
# __init__ is the constructor in Python.
# It runs automatically when an object is created.
# Used to initialize attributes.