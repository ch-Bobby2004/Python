# In Python, enumerate() is a built-in function used to get both the index and the value while looping through a list (or any iterable).

# enumerate(iterable, start=0)
# iterable → list, tuple, string, etc.
# start → starting index (default is 0)

l1 = [2, 3,True,3.13,"ch"]

for index, value in enumerate(l1):
    print(index, value)