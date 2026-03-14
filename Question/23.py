# Reverse the list
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)


numbers = [1, 2, 3, 4, 5]
reversed_list = numbers[::-1]
print(reversed_list)


numbers = [1, 2, 3, 4, 5]
reversed_list = []

for i in range(len(numbers)-1, -1, -1):
    reversed_list.append(numbers[i])

print(reversed_list)


# start = len(numbers)-1

# len(numbers) is 5 (because [1,2,3,4,5] has 5 elements)

# len(numbers)-1 = 4 → this is the index of the last element

# 2️⃣ stop = -1

# This is the index where the loop stops (exclusive)

# So the loop will continue until it reaches i = 0 and stops before -1

# 3️⃣ step = -1

# This tells range() to move backwards, decreasing the index by 1 each time