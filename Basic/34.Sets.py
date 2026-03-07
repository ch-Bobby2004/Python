my_set = {1, 2, 3, 4}

# Using set() constructor
# Duplicate values are automatically removed:
my_set = set([1, 2, 3,1 ,4,"hi"])

print(my_set)


s = {1, 2, 3}

s.add(4)          # add single element
s.update([5, 6])  # add multiple elements

print(s)
s.remove(3)   # error if element not found
s.discard(5)  # no error if element not found
s.pop()       # removes random element
print(s)



A = {1, 2, 3}
B = {3, 4, 5}
# Union
# Combine elements from both sets.
print(A | B)
# Intersection
# Common elements.
print(A & B)

# Difference
# Elements in A but not in B.
print(A - B)


# Symmetric Difference
# Elements in either set but not both.

print(A ^ B)


print(2 in A)   # True
print(11 in A)   # False
