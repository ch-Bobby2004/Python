# Count sum of digit
def sum_of_digits(n):
    # Base case
    if n == 0:
        return 0
    
    # Recursive case
    return (n % 10) + sum_of_digits(n // 10)

# Example
print(sum_of_digits(1234))  # Output: 10