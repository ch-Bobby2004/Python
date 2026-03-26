# whether a give list is sorted or not
def is_sorted_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

# Test examples
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 3, 2, 4, 5]

print(is_sorted_ascending(numbers1))  # Output: True
print(is_sorted_ascending(numbers2))  # Output: False05