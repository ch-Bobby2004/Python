
# Size of the square

n = 5  # size of the square

for i in range(n):            # outer loop for rows
    for j in range(n):        # inner loop for columns
        print('*', end='')    # print * without moving to next line
    print()    

# the * n is Python’s string repetition operator. It means:
# Take the string '* ' and repeat it n times.
# If n = 4, then '* ' * n becomes:

print('Hi! ' * 3)

n = 4
for i in range(n):
    print('* ' * n)