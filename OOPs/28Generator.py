# A generator is a special type of iterator that generates values on the fly using yield. It is memory-efficient, especially for large datasets.



def my_generator():
    yield 1  # yields value instead of returning
    yield 2
    yield 24
    yield 3

gen = my_generator()

print(next(gen))  
print(next(gen))  

for val in gen:
    print(val)  







def my_generator(n):
    for i in range(1, n+1):
        yield i  # yields value instead of returning

gen = my_generator(5)

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2

for val in gen:
    print(val)  # Output: 3, 4, 5