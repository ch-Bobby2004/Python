''' 1. What is OOP in Python?

Answer:
OOP stands for Object-Oriented Programming, a programming paradigm based on objects and classes. It helps organize code into reusable and modular structures. Python supports OOP features like encapsulation, inheritance, polymorphism, and abstraction.

2. What is a class and an object?

Answer:

Class: A blueprint for creating objects. It defines attributes (variables) and methods (functions).
Object: An instance of a class. Each object can have unique values for the attributes.
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Camry")
print(car1.brand)  # Output: Toyota
3. What is __init__ method in Python?

Answer:
__init__ is a constructor method in Python. It is automatically called when an object is created. It initializes object attributes.

4. What is self in Python?

Answer:
self represents the instance of the class. It is used to access variables and methods associated with the current object.

class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

p = Person("Alice")
p.greet()  # Output: Hello, Alice!
5. What is inheritance in Python?

Answer:
Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Output: Dog barks
6. What are the types of inheritance in Python?

Answer:

Single Inheritance – One child, one parent.
Multiple Inheritance – One child, multiple parents.
Multilevel Inheritance – Chain of inheritance (grandparent → parent → child).
Hierarchical Inheritance – One parent, multiple children.
Hybrid Inheritance – Combination of multiple types.
7. What is encapsulation in Python?

Answer:
Encapsulation is restricting access to variables and methods to protect data.

Public: Accessible from anywhere (self.var)
Protected: Accessible in class & subclasses (self._var)
Private: Accessible only in class (self.__var)
class Test:
    def __init__(self):
        self.__private = 10

    def get_private(self):
        return self.__private

t = Test()
print(t.get_private())  # Output: 10
8. What is polymorphism in Python?

Answer:
Polymorphism allows methods or operators to have different forms.

Method Overloading (Python does not support true overloading; can simulate with default arguments)
Method Overriding (Child class redefines parent method)
class Bird:
    def fly(self):
        print("Bird can fly")

class Penguin(Bird):
    def fly(self):
        print("Penguin cannot fly")

b = Penguin()
b.fly()  # Output: Penguin cannot fly
9. What is abstraction in Python?

Answer:
Abstraction hides complex implementation and shows only the necessary details. In Python, it’s done using abstract classes and the abc module.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts")

c = Car()
c.start()  # Output: Car starts
10. What is the difference between class variables and instance variables?
Feature	Class Variable	Instance Variable
Defined in	Class body	__init__ method
Shared by	All instances	Only that instance
Accessed by	Class or object	Object only
class Test:
    class_var = 0  # class variable
    def __init__(self, val):
        self.instance_var = val  # instance variable

    '''