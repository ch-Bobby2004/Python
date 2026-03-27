# Polymorphism = same thing behaving differently in different situations

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self): #function overriding
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.speak()
    
# Same method name speak(), behaves differently for each object.