def reverse_num(n, rev=0):
    if n == 0:   # Base case
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

num = 1234
print(reverse_num(num))  # Output: 4321