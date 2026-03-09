# In Python, id() is a built-in function that returns the unique identity (memory address) of an object during its lifetime.
# Returns an integer representing the object's identity.

# In CPython (the common implementation), this is typically the memory address where the object is stored.

# Two objects with the same identity are the same object in memory.
x = 10
print(id(x))
x = 5
print(id(x))

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))