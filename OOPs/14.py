class Student:
    school = "ABC School"   # class variable

    def __init__(self, name):
        self.name = name    # instance variable

s1 = Student("Alice")
s2 = Student("Bob")

print(s1.name, s1.school)  # Alice ABC School
print(s2.name, s2.school)  # Bob ABC School

Student.school = "XYZ School"  # change class variable
print(s1.school, s2.school)    # XYZ School XYZ School

s3 = Student("Jk")
print(s3.name, s3.school)    # XYZ School XYZ School

