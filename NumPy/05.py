# Identity Matrix in NumPy
# An identity matrix is a square matrix where:

# Diagonal elements = 1
# All other elements = 0

import numpy as np

arr = np.eye(3)
print(arr)
print(np.eye(4))
print(np.identity(3))

# np.eye(n) → can create non-square matrices too (e.g., np.eye(2,3))
# np.identity(n) → only square matrix



arr = np.random.rand(2, 3)
print(arr)

# 2×3 array with values between 0 and 1

arr = np.random.randint(1, 10, (2, 3))
print(arr)

# Integers from 1 to 9

arr = np.random.randn(2, 3)
print(arr)

# Values from normal distribution (mean=0, std=1)

np.random.seed(42)

arr = np.random.rand(2, 3)
print(arr)

# Output will be same every run
