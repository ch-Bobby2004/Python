for i in range(1, 4):          # Outer loop
    for j in range(1, 4):      # Inner loop
        print(f"i={i}, j={j}")
        
rows = 5
for i in range(1, rows+1):
    for j in range(i):
        print("*", end="")   # Print stars in the same line
    print()                  # Move to next line
    
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:             # Outer loop iterates over each inner list
    for element in row:        # Inner loop iterates over elements of the inner list
        print(element, end=" ")
    print()                    # New line after each row