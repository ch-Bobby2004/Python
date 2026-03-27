class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def lets_fly(entity):
    entity.fly()   # works as long as 'entity' has fly()

b = Bird()
a = Airplane()

lets_fly(b)
lets_fly(a)


# Polymorphism = same name, different behavior depending on object or type