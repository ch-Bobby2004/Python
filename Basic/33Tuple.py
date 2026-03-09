# Using parentheses
my_tuple = (1, 2, 3, 4,5,4)
print(my_tuple)  # (1, 2, 3, 4)
print(min(my_tuple))  
print(my_tuple.count(4))
print(my_tuple.index(4))

# Without parentheses (tuple packing)
t2 = 5, 6, 7
print(t2)        # (5, 6, 7)

# Single element tuple (needs a comma!)
single = (10,)
print(type(single))  # <class 'tuple'>

print(my_tuple[0])   # 10 → first element
print(my_tuple[-1])  # 40 → last element
print(my_tuple[1:3]) # (20, 30) → slicing works too



t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenation
print(t1 + t2)  # (1, 2, 3, 4, 5, 6)

# Repetition
print(t1 * 2)   # (1, 2, 3, 1, 2, 3)

# Membership
print(2 in t1)  # True
print(7 in t1)  # False


list1 = [1,24,5,54]
#conver list to tuple
print(tuple(list1))