numbers = [4, 11, 8, 15, 3, 22]

# Using filter with a lambda function
greater_than_10 = list(filter(lambda x: x > 10, numbers))  #type cast in list

print(greater_than_10)  # Output: [11, 15, 22]

# Explanation:

# filter(function, iterable) keeps only elements where the function returns True.

# lambda x: x > 10 is a short function that returns True if x > 10

# Not exactly — the filter() function itself does not return a list in Python. It returns a filter object, which is an iterator.
numbers = [4, 11, 8, 15, 3, 22]

# filter returns a filter object
filtered = filter(lambda x: x > 10, numbers)
print(filtered)        # Output: <filter object at 0x...>

# Convert filter object to list
filtered_list = list(filtered)
print(filtered_list)   # Output: [11, 15, 22]
