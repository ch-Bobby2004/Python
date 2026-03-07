# 2D list (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)
# Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements
print(matrix[0][0])  # 1  → first row, first column
print(matrix[1][2])  # 6  → second row, third column

matrix.append([10, 11, 12])
print(matrix)

print(len(matrix))

numbers = [1,2,3,4,5,5,[3,5,3,],5,3,3]
print(numbers)
print(len(numbers))
print(numbers[5])
print(numbers[6])
print(numbers[6][0])
print(numbers[len(numbers)-2])
print(numbers[6][:])
