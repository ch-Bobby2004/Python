def even_gen(n):
    for i in range(0, n+1, 2):
        yield i

for num in even_gen(20):
    print(num, end=" ")