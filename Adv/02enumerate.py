# nums → your list (e.g., [2, 7, 11, 15])
# enumerate(nums) gives both the index and the value at the same time.
# i → index (0, 1, 2, ...)
# num → value at that index (2, 7, 11, ...)
# Exactly — that’s one of the nice things about enumerate:

# You don’t need to know the length of the list. Python automatically keeps track of the index for you.
nums = [2, 7, 11, 15]

for i, num in enumerate(nums):
    print(f"Index: {i}, Value: {num}")