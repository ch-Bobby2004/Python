# fromkeys() creates a dictionary where you provide keys, and Python assigns the same default value to all keys
keys = ["a", "b", "c"]

d = dict.fromkeys(keys, 0)

print(d)

keys = ["name", "age", "city"]

d = dict.fromkeys(keys)

# n Python, None is a special constant that represents the absence of a value or “nothing”.

# It is often used to indicate that a variable exists but has no meaningful value yet.

print(d)

keys = ["a", "b", "c"]

d = dict.fromkeys(keys)

d["a"] = 1
d["b"] = 2
d["c"] = 3

print(d)


# update
student = {"name": "Rahul", "age": 20}

# Update age
student["age"] = 21

print(student)
# Using update() Method

# The update() method can update multiple key–value pairs at once.

student.update({"age": 22, "course": "Python"})
print(student)


