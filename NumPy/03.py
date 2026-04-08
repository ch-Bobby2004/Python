import numpy as np

list1 = [1,2,3,4]
print(list1)
print(type(list1))   # print the type

# Numpy Array
np_array = np.array([1,2,3,4])
print(np_array)
print(type(np_array))   # print the type

# Python list → flexible, can hold mixed data types
# NumPy array → faster, optimized for numerical operations, fixed type


# To create a 1D array in NumPy, you use np.array() with a single list.

arr = np.array([10, 20, 30, 40])

print(arr)
print(type(arr))
print(arr.shape)
# A 1D array has only one axis (no rows/columns structure).
# shape will look like (n,) where n is number of elements.

# Using np.zeros() (most common placeholder)

print(np.zeros(5))        # [0. 0. 0. 0. 0.]
print(np.ones(5))         # [1. 1. 1. 1. 1.]
print(np.arange(1, 6))    # [1 2 3 4 5]
print(np.linspace(0, 1, 5))  # evenly spaced values