# find the longest sequence of consecutive 1’s in a list of 0’s and 1’s

def longest_consecutive_ones(arr):
    max_count = 0
    count = 0
    for num in arr:
        if num == 1:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
    return max_count

# Test
arr = [1, 1, 0, 1, 1, 1, 0, 1]
print(longest_consecutive_ones(arr))