import numpy as np

arr = np.arange(1, 10)  # 1D array [1 2 3 4 5 6 7 8 9]
print("Original:", arr)

arr_2d = arr.reshape(3, 3)  # 3x3 2D array
print("Reshaped 3x3:\n", arr_2d)

flat = arr_2d.flatten()
print("Flattened:", flat)
print("Transposed:\n", arr_2d.T)

a = np.array([1,2,3])
b = np.array([4,5,6])

# Horizontal (1D arrays)
h = np.concatenate((a,b))
print("Concatenate:", h)

# Vertical stacking (2D arrays)
v = np.vstack((a,b))
print("Vstack:\n", v)

arr = np.arange(1, 7)
split_arr = np.split(arr, 3)  # split into 3 equal parts
print("Split:", split_arr)

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Element at (1,2):", arr_2d[1,2])
print("Second row:", arr_2d[1,:])
print("First column:", arr_2d[:,0])