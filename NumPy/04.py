import numpy as np

arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6]])

print(arr_2d)
print("Shape:", arr_2d.shape)
print(np.zeros((2, 3)))      # 2 rows, 3 columns
print(np.ones((2, 3)))
print(np.arange(1, 7).reshape(2, 3))   # reshape 1D to 2D
print(np.linspace(0, 1, 6).reshape(2, 3))
arr = np.arange(0, 10, 2)  # 0 to 9, step 2
print(arr)

print(np.array([1, 2, 3]).dtype)        # int
print(np.array([1.0, 2.5, 3.1]).dtype)  # float
print(np.array([1, 2, 3], dtype=float)) # force float
print(np.array([1, 0, 1], dtype=bool))  # boolean


arre = np.empty((2, 3))
print(arre)
arr = np.full((2, 3), -1)
print(arr)