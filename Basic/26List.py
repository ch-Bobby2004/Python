# Slice Function / Slicing
# Slicing allows you to get a sub-list from a list.
# Syntax:
# list[start : end : step]
# start → index to start (inclusive)
# end → index to end (exclusive)

# step → interval between elements (default 1)


my_list = [10, 20, 30, 40, 50, 60]

# Get elements from index 1 to 4 (exclusive)
print(my_list[1:4])    # [20, 30, 40]

# Get elements from start to index 3
print(my_list[:4])     # [10, 20, 30, 40]

# Get elements from index 2 to end
print(my_list[2:])     # [30, 40, 50, 60]

# Get every 2nd element
print(my_list[::2])    # [10, 30, 50]

# Reverse the list
print(my_list[::-1])   # [60, 50, 40, 30, 20, 10]
print(my_list[::-2])   # [60, 50, 40, 30, 20, 10]




# Python also has a built-in slice() function which is equivalent to slicing with :.

# Syntax:

# slice(start, stop, step


my_list = [10, 20, 30, 40, 50, 60]

# Create a slice object
s = slice(1, 5, 2)     # start=1, stop=5, step=2

# Apply to list
print(my_list[s])       # [20, 40]



# Summary:

# List → ordered, mutable collection

# Slicing → list[start:end:step]

# slice() function → reusable slicing object