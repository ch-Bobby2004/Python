# even or odd element

numbers = [1, 2, 3, 4, 5, 6]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)


numbers = [1, 2, 3, 4, 5, 6]

even_count = len(list(filter(lambda x: x % 2 == 0, numbers)))
odd_count = len(list(filter(lambda x: x % 2 != 0, numbers)))

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
