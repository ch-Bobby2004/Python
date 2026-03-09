student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print(student)

 # Key–value pairs
 # Keys must be unique
# Values can be duplicated
# Mutable (can be modified)

print(student["name"])
print(student["age"])


student["age"] = 21
student["city"] = "Mumbai"

print(student)

student.pop("age")
print(student)

print(student.keys())    # returns keys
print(student.values())  # returns values
print(student.items())   # returns key-value pairs



person = {
    "name": "Amit",
    "age": 25,
    "city": "Pune"
}

for key, value in person.items():
    print(key, ":", value)