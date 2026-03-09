# Function with Default Parameter
# If the user does not give a value, the default value is used.

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Amit")



# Function Returning Multiple Values
def calculate(a, b):
    add = a + b
    subtract = a - b
    return add, subtract

result = calculate(10, 5)

print("Addition:", result[0])
print("Subtraction:", result[1])


# Recursive Function (Advanced)
# A function calling itself.
# Example: Factorial

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


