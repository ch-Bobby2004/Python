# An iterator is an object that implements the iterator protocol, which consists of:
# __iter__() → returns the iterator object itself
# __next__() → returns the next value, raises StopIteration when done



# List is iterable
my_list = [1, 2, 3]

# Get an iterator using iter()
my_iter = iter(my_list)

print(next(my_iter))  # Output: 1
print(next(my_iter))  # Output: 2
print(next(my_iter))  # Output: 3
# next(my_iter) now raises StopIteration  
# inernaly use try etc