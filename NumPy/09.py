#  Sudoku 

# Each row contains digits 1–9 without repetition.
# Each column contains digits 1–9 without repetition.
# Each 3×3 subgrid contains digits 1–9 without repetition.


import numpy as np

def validate_sudoku(grid):
    grid = np.array(grid)  # Ensure it is a NumPy array

    # 1 Check rows
    for i, row in enumerate(grid):
        if row.sum() != 45:
            print(f"Invalid row {i+1} sum: {row.sum()}")
            return False
        if len(np.unique(row)) != 9:
            print(f"Invalid row {i+1} duplicate values: {row}")
            return False

    # 2 Check columns
    for j, col in enumerate(grid.T):  # transpose to iterate columns
        if col.sum() != 45:
            print(f"Invalid column {j+1} sum: {col.sum()}")
            return False
        if len(np.unique(col)) != 9:
            print(f"Invalid column {j+1} duplicate values: {col}")
            return False

    # 3️⃣ Check 3x3 subgrids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = grid[i:i+3, j:j+3].flatten()
            if subgrid.sum() != 45:
                print(f"Invalid subgrid starting at ({i+1},{j+1}) sum: {subgrid.sum()}")
                return False
            if len(np.unique(subgrid)) != 9:
                print(f"Invalid subgrid starting at ({i+1},{j+1}) duplicates: {subgrid}")
                return False

    print("Sudoku is valid ✅")
    return True

# Example Sudoku grid (valid)
sudoku_grid = [
    [5,3,4,6,7,8,9,1,2],
    [6,7,2,1,9,5,3,4,8],
    [1,9,8,3,4,2,5,6,7],
    [8,5,9,7,6,1,4,2,3],
    [4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],
    [9,6,1,5,3,7,2,8,4],
    [2,8,7,4,1,9,6,3,5],
    [3,4,5,2,8,6,1,7,9]
]

validate_sudoku(sudoku_grid)