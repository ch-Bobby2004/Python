def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):  # _ valid variable name
    # for i in range(n):
        yield a
        a, b = b, a + b

# Using the generator
for num in fibonacci(10):
    print(num)