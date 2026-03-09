fruits = ["apple", "banana", "cherry"]

print(fruits)
print(len(fruits))
fruits.append("orange")  # ['apple', 'banana', 'cherry', 'orange']

fruits.insert(1, "kiwi")  # ['apple', 'kiwi', 'banana', 'cherry', 'orange']

fruits.remove("banana")   # ['apple', 'kiwi', 'cherry', 'orange']

popped = fruits.pop()     # removes 'orange'

fruits.count("apple")     # 1

fruits.sort()             # ['apple', 'cherry', 'kiwi']

fruits.reverse()          # ['kiwi', 'cherry', 'apple']

print(fruits[1])
print(fruits[-1])
print(fruits[-2])


