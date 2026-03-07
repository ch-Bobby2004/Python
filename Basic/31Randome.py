# What is the random module?
# The random module in Python is a built-in module that provides functions to generate:
# Random numbers
# Random sequences
# Random selections from a list or string




import random
print(random.random())  # 0.237891 (example)
print(random.randint(1, 10))  # Could be any number from 1 to 10
# Returns a random number from a range.
print(random.randrange(0, 20, 2))  # Even number between 0 and 18
print(random.randrange(1, 20, 2))  
colors = ['red', 'green', 'blue']
print(random.choice(colors))  # 'green' (example)


cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
print(cards)  # [3, 5, 1, 4, 2] (example)
print(random.uniform(1, 10))  # 3.872 random float




colors = ['red', 'green', 'blue', 'yellow']

# Pick 2 random elements (with replacement)
# k specifies how many elements you want to select from a sequence.
result = random.choices(colors, k=2)
print(result)  # ['blue', 'red']  (example)





num = int(random.random() * 100) + 1
print(num)





# random is not cryptographically secure

# The numbers from random are pseudo-random, generated using an algorithm.

# This is fine for:

# Games

# Simulations

# Random sampling

# Shuffling data

# But do not use it for security purposes, like:

# Generating passwords

# Cryptographic keys

# Security tokens

# Because someone could predict the sequence if they know the algorithm and seed.