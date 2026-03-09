# clear() removes all elements from the list, but the list object still exists.
lst = [10, 20, 30, 40]

lst.clear()

print(lst)


# del Keyword
# del is used to delete elements or the entire list.
lst = [10, 20, 30, 40]

del lst[1]


print(lst)
del lst[0:2]
print(lst)

del lst
# print(lst) get error  del list (list in not exists)