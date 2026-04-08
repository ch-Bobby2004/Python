# Converting a Python list to a NumPy array is straightforward using np.array()
import numpy as np

# Python list
my_list = [1, 2, 3, 4, 5]

# Convert to NumPy array
arr = np.array(my_list)

print("List:", my_list)
print("NumPy array:", arr)
print("Type:", type(arr))

my_2d_list = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(my_2d_list)
print(arr_2d)

# analysis of a NumPy array
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

print("Array:\n", arr)
print("Shape:", arr.shape)     # (rows, columns)
print("Number of dimensions:", arr.ndim)
print("Size (total elements):", arr.size)
print("Data type:", arr.dtype)
print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Minimum:", arr.min())
print("Maximum:", arr.max())
print("Standard deviation:", arr.std())
print("Sum of each column:", arr.sum(axis=0))
print("Sum of each row:", arr.sum(axis=1))
print()
print()
print()
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Array a:", a)
print("Array b:", b)

print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)

print("a + 10 =", a + 10)
print("b * 2 =", b * 2)

print("np.add(a, b) =", np.add(a, b))
print("np.subtract(a, b) =", np.subtract(a, b))