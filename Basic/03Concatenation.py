name = "Bobby"
greeting = "Hello " + name
print(greeting)

print("Welcome",name) #Automatically adds a space between values.

text = "Hello"
text += " World"
print(text)

# Using f-strings (Best & Modern Way)

name = "Bobby"
print(f"Hello {name}")


age = 20
# print("Age: " + age)   # Error

# ✔ Correct way:
print("Age: " + str(age))