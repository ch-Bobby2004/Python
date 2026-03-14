# check if all elements in a list are unique


numbers = [1, 2, 3, 4, 5]

if len(numbers) == len(set(numbers)):
    print("All elements are unique")
else:
    print("There are duplicates")



numbers = [1, 2, 3, 4, 5]
unique = True

for i in numbers:
    if numbers.count(i) > 1:
        unique = False
        break

if unique:
    print("All elements are unique")
else:
    print("There are duplicates")


# Using a Dictionary

numbers = [1, 2, 3, 4, 5]
seen = {}

unique = True
for n in numbers:
    if n in seen:
        unique = False
        break
    seen[n] = True

if unique:
    print("All elements are unique")
else:
    print("There are duplicates")
