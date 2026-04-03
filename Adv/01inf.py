# What it means
# float('-inf') is negative infinity in Python.
# It’s smaller than any number you might encounter..

# Why float?

# In Python, numbers have types:

# int → integers, e.g., 5, -2
# float → floating-point numbers, e.g., 5.0, -2.0, inf, -inf

# Python doesn’t have a built-in integer infinity, but it does have floating-point infinity.

ans = float('-inf')

nums = [2, 3, -2, 4]
for x in nums:
    ans = max(ans, x)
    print(ans)
    
float('inf')   # positive infinity
float('-inf')  # negative infinity

# This works for comparisons with any numeric type:

x = -100
print(x > float('-inf'))  # True
print(float('inf'))