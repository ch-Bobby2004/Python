# remove duplicates
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = []

for n in numbers:
    if n not in unique:
        unique.append(n)

print(unique)

# Unordered (elements have no fixed position)
numbers = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(numbers))

print(unique)


numbers = [1, 2, 2, 3, 4, 4, 5]
# unique and ordered
unique = list(dict.fromkeys(numbers))

print(unique)
# {1:None, 2:None, 3:None, 4:None, 5:None}
# [1, 2, 3, 4, 5]