def Square(n):
    for i in range(0, n+1 ):
        yield i*i

for num in Square(20):
    print(num, end=" ")