# calculate power of a number

def power(x, n):
    # Base case
    if n == 0:
        return 1
    
    # Recursive case
    return x * power(x, n - 1)

# Example
print(power(2, 3))  # Output: 8