# pyramid

n = 4  # height of the pyramid

for i in range(1, n+1):
    # print spaces
    for j in range(n-i):
        print('  ', end='')
    # print stars
    for k in range(2*i-1):
        print('* ', end='')
    print()  # move to next row
    
print()
    
n = 4  # height of the pyramid

for i in range(n, 0, -1):
    # print leading spaces to center
    print('  ' * (n - i) + ' *' * (2*i - 1))
    
    
    