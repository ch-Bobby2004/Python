class Person :
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
p1 = Person("Bobby",20)
print(p1.name)
p1.greet()
