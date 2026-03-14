# In Python, the zip() function is used to combine two or more iterables (like lists, tuples, or strings) element-wise into pairs (tuples).

list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c']

zipped = zip(list1, list2)
print(list(zipped))