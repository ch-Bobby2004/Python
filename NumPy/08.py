import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr[0])  # 10 → first element
print(arr[3])  # 40 → fourth element
print(arr[-1])  # 50 → last element
print(arr[-2])  # 40 → second last element
print(arr[1:4])    # [20 30 40] → index 1 to 3
print(arr[:3])     # [10 20 30] → from start to index 2
print(arr[2:])     # [30 40 50] → from index 2 to end
print(arr[::2])    # [10 30 50] → every 2nd element

arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
print(arr2d[0, 1])  # 2 → first row, second column
print(arr2d[2, 2])  # 9 → third row, third column
print(arr2d[-1, -1])  # 9 → last row, last column


print(arr2d[0:2, 1:3])  # first two rows, columns 1 and 2
print(arr2d[::2, ::2])  # every 2nd row and every 2nd column
print(arr2d[arr2d > 2])
