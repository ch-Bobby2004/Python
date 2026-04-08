# List vs NumPy speed comparison
import time
import numpy as np

# Create large data
size = 1000000

# Python list
list1 = list(range(size))
list2 = list(range(size))

start = time.time()
result = [list1[i] + list2[i] for i in range(size)]
end = time.time()

print("List time:", end - start)

# NumPy array
arr1 = np.array(list1)
arr2 = np.array(list2)

start = time.time()
result = arr1 + arr2
end = time.time()

print("NumPy time:", end - start)


# umPy is much faster (10x–50x) depending on system.

# Why NumPy is faster?
# 1. Written in C

# NumPy uses optimized C code internally (not pure Python loops)

# 2. No Python loop
# List → uses for loop (slow)
# NumPy → does operations in one go (vectorized)
# 3. Memory efficiency

# NumPy arrays store data in a compact format
# Python list → slower for large data
# NumPy → fast, efficient, 