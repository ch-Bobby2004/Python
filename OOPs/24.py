# make your own version of range() using an iterator

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


nums = MyRange(1, 6)

for n in nums:
    print(n)