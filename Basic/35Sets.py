A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))
print(A <= B)
print(A.issuperset(B))
print(A >= B)
print(A < B)
# Two sets are disjoint if they have no common elements.
print(A.isdisjoint(B))



# 1. clear() Method

# clear() removes all elements from the set but keeps the set variable.

A = {1, 2, 3, 4}
A.clear()
# del deletes the entire set variable from memory
del A
print(A)