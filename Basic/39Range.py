# In Python, range is actually a data type (class), but it is used through a function-like call.

#  range is a Data Type

# range represents a sequence of numbers.
r = range(5)
print(type(r))

for i in range(5):
    print(i)

num  = range(5)
print(num)



l1 = [2,3,2,4,3,2]

for i in range(len(l1)):
    print(l1[i])