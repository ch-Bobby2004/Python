numbers = [1, 2, 3, 4]

for n in numbers:
    print(n)
    
    # range(5) generates numbers 0 to 4.
for i in range(5):
   print(i)
   
   
word = "Python"

for letter in word:
    print(letter)
    
A = {10, 20, 30}

for x in A:
    print(x)
    
for i in range(5):
    if i == 3:
        break
    print(i)
    
for i in range(5):
    if i == 2:
        continue
    print(i)
    
    # for Loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished")


for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop finished")

# else does not execute because the loop stopped using break.

numbers = [2, 4, 6, 8]

for n in numbers:
    if n == 5:
        print("Found")
        break
else:
    print("Not found")