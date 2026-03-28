def count_digits(n):
    if n == 0:
        return 1
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)
    
    
num = 1
print(count_digits(num))  # Output: 5