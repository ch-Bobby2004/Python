# map() in Python! It’s similar to filter(), but instead of filtering items, it applies a function to every item in a list (or any iterable).

numbers = [1, 2, 3, 4, 5]

# Multiply each number by 2
doubled = map(lambda x: x * 2, numbers)

print(doubled)          # Output: <map object at 0x...>
print(list(doubled))    # Output: [2, 4, 6, 8, 10]

# Explanation:

# map(function, iterable) applies the function to each item.

# Like filter(), map() returns an iterator, so you usually wrap it in list() to see the