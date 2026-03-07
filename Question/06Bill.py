import random

# Input names as a single string, separated by commas
names_string = "Alice Bob Charlie David"

# Split the string into a list
people = names_string.split(" ")  # ['Alice', 'Bob', 'Charlie', 'David']

# Pick a random index
index = random.randint(0, len(people) - 1)

# Select the person and strip any extra spaces
payer = people[index].strip()

print(f"{payer} will pay the bill!")