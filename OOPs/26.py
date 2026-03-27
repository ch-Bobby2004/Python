class ReverseList:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        
        val = self.data[self.index]
        self.index -= 1
        return val
        
lst = [10, 20, 30]

obj = ReverseList(lst)

for x in obj:
    print(x)