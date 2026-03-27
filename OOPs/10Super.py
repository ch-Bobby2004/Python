# super() is a function that lets you call methods from the parent class in a child class.

# Used mostly in inheritance
# Helps reuse parent class code without rewriting it


class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")
        super().greet()  # call Parent's greet

c = Child()
c.greet()



# super() = parent class reference
# Allows child to use parent methods
# Useful in overridden methods