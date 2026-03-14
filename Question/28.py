# check if a tuple is a palindrome

t = (1, 2, 3, 2, 1)

if t == t[::-1]:
    print("Tuple is a palindrome")
else:
    print("Tuple is NOT a palindrome")

