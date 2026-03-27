class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        
        val = self.data[self.index]
        self.index += 1
        return val
        
        
        
lst = [10, 20, 30]

obj = ListIterator(lst)

for x in obj:
    print(x)