
# hollow square
n = 5  # size of the square

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('* ', end='')
        else:
            print('  ', end='')  # space inside the square
    print()  # move to next row
    
    
    # Rectangle
    
rows = 4    # number of rows
cols = 7    # number of columns

for i in range(rows):
    for j in range(cols):
        print('* ', end='')  # print * without going to a new line
    print()  # move to next row
    
    # Right angel triangle
    
n = 5  # height of the triangle

for i in range(1, n+1):          # loop for each row
    for j in range(i):           # print stars equal to row number
        print('* ', end='')
    print()  
 
print()  
print()  
n = 5  # height of the triangle

for i in range(n, 0, -1):       # start from n down to 1
    for j in range(i):
        print('* ', end='')
    print()