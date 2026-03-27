# If both parents have same method name

class A:
    def show(self):
        print("A")

class B:
    def show(self):
        print("B")

class C(A, B):
    pass

c = C()
c.show()

# Python follows left-to-right order
# 👉 This is called MRO (Method Resolution Order)