num = 12345
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print(rev)


num = 12345
rev = int(str(num)[::-1])

print(rev)

# [::-1] reverses the string.

def reverse_integer(n):
    return int(str(n)[::-1])

print(reverse_integer(9876))