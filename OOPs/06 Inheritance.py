# What is Inheritance?

#  Inheritance = one class gets properties and methods from another class

# Real-Life Example

# Think of:

# Parent 
# Child 

#  Child gets features from parent (like name, habits)




class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):   # Dog inherits Animal
    pass

d = Dog()
d.speak()


class Dog(Animal):
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # from Animal
d.bark()   # from Dog



class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def speak(self):
        print("Dog barks")

d = Dog()
d.speak()  # Dog barks


# Inheritance = reuse code from another class