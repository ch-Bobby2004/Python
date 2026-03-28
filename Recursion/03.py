def factorial(n):
    if n == 0 or n == 1:   # Base case
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120



def sum_n(n):
    if n == 0:   # Base case
        return 0
    else:
        return n + sum_n(n - 1)

print(sum_n(5))  # Output: 15