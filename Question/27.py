# check if a list is a subset of another list

list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]

# Convert lists to sets
if set(list1).issubset(set(list2)):
    print("list1 is a subset of list2")
else:
    print("list1 is NOT a subset of list2")


list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]

is_subset = True
for elem in list1:
    if elem not in list2:
        is_subset = False
        break

if is_subset:
    print("list1 is a subset of list2")
else:
    print("list1 is NOT a subset of list2")
