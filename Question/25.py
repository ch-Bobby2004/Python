# find the maximum difference between two consecutive elements in a list,

numbers = [2, 5, 1, 9, 7]

max_diff = 0  # initialize maximum difference

for i in range(len(numbers)-1):
    diff = abs(numbers[i+1] - numbers[i])  # difference between consecutive elements
    if diff > max_diff:
        max_diff = diff

print("Maximum difference between consecutive elements:", max_diff)


numbers = [2, 5, 1, 9, 7]

max_diff = max([abs(numbers[i+1] - numbers[i]) for i in range(len(numbers)-1)])

print("Maximum difference between consecutive elements:", max_diff)
