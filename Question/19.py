# max element in list

numbers = [10, 25, 7, 40, 15]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element:", largest)


numbers = [10, 25, 7, 40, 15]
print("Largest element:", max(numbers))


from functools import reduce

numbers = [10, 25, 7, 40, 15]

largest = reduce(lambda a, b: a if a > b else b, numbers)

print("Largest element:", largest)