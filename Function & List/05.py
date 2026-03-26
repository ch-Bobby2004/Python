# move all zeros in a list to the end
numbers = [0, 1, 0, 3, 12, 0, 5]

# Pointer for next non-zero element
position = 0

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[position] = numbers[i]
        position += 1

# Fill remaining positions with zeros
for i in range(position, len(numbers)):
    numbers[i] = 0

print(numbers)