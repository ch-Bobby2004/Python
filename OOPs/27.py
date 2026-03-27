class Fibonacci:
    def __init__(self, limit):
        self.a = 0
        self.b = 1
        self.limit = limit
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        
        val = self.a
        self.a, self.b = self.b, self.a + self.b
        self.count += 1
        return val
        
fib = Fibonacci(7)

for x in fib:
    print(x)