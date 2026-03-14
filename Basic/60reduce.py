# reduce() in Python. This is another functional programming tool, like map() and filter(), but it’s used to combine all items in an iterable into a single value.

# In Python 3, reduce() is not built-in; you need to import it from functools:
# from functools import reduce


from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Using reduce to sum numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # Output: 15


# lambda x, y: x + y is applied pairwise:

# 1 + 2 → 3
# 3 + 3 → 6
# 6 + 4 → 10
# 10 + 5 → 15

# reduce() returns a single value, not a list.