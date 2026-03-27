class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # call Parent __init__
        self.age = age

c = Child("Alice", 10)
print(c.name)  # Alice
print(c.age)   # 10

# super() = lets child class access parent class methods/constructors easily