# perform a right rotation on a list by any number of positions

numbers = [1, 2, 3, 4, 5]
k = 2  # number of rotations

# Right rotation by slicing
rotated = numbers[-k:] + numbers[:-k]

print(rotated)


numbers = [1, 2, 3, 4, 5]
k = 2

for _ in range(k):
    last = numbers.pop()   # remove last element
    numbers.insert(0, last)  # insert it at the beginning

print(numbers)
