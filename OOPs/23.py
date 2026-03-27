# custom iterator class:

class MyNumbers:
    def __init__(self, limit):
        self.num = 0
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < self.limit:
            self.num += 1
            return self.num
        else:
            raise StopIteration

nums = MyNumbers(5)
for n in nums:
    print(n)