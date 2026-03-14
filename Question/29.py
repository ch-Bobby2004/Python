# merge two lists into a dictionary


keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Merge lists into dictionary
merged_dict = dict(zip(keys, values))

print(merged_dict)



keys = ['a', 'b', 'c']
values = [1, 2, 3]

merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print(merged_dict)



# In Python, the zip() function is used to combine two or more iterables (like lists, tuples, or strings) element-wise into pairs (tuples).