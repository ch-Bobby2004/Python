# In Python, defaultdict is a subclass of the built-in dict class that provides a default value for the dictionary if the key has not been set yet.

# When you use defaultdict(int), you're creating a dictionary where any missing key will have a default value of 0 (because int() returns 0 when called without arguments).

# Key Points:
# defaultdict is part of the collections module.
# int is passed as the default factory function. It means that if you try to access a key that doesn’t exist, it will be automatically created with the value 0.
# Example:
from collections import defaultdict

# Create a defaultdict where missing keys default to 0
my_dict = defaultdict(int)

# Access a key that doesn't exist yet
print(my_dict['apple'])  # Output: 0 (default value)

# Increment the value for the 'apple' key
my_dict['apple'] += 1
print(my_dict['apple'])  # Output: 1 (after incrementing)

# Accessing another missing key
print(my_dict['banana'])  # Output: 0 (default value)
# Why use defaultdict(int)?
# Automatic initialization: You don't need to check if a key exists or initialize it manually. It saves you from writing extra logic like if key not in dict: dict[key] = 0.
# Common in counting: It's very useful when you're counting occurrences or building frequency distributions, like when you're counting how many times different words appear in a text.