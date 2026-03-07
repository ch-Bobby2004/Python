# Lists (list)

# A list is an ordered collection of items. It can contain different types.

numbers = [1, 2, 3, 4]
mixed = [1, "Hello", 3.14, True]
print(numbers)
print(mixed)

# Lists are mutable → you can change items

numbers[0] = 10
print(numbers[-1]) #Last Element
print(numbers)




fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple (first item)
print(fruits[-1])  # Output: cherry (last item)

fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

fruits.append("orange")   # Add at the end
fruits.insert(1, "kiwi")  # Add at specific index
fruits.remove("apple")    # Remove an item by value
print(fruits)             # Output: ['kiwi', 'blueberry', 'cherry', 'orange']