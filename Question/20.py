# remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)

numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))

print(unique)