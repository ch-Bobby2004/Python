# randomly select who pays the bill
import random


people = ['Alice', 'Bob', 'Charlie', 'David']

person = random.choice(people)
print(f"{person} will pay the bill!")

#without using choice function

# List of people
people = ['Alice', 'Bob', 'Charlie', 'David']

# Generate a random index
index = random.randint(0, len(people) - 1)

# Pick the person at that index
payer = people[index]

print(f"{payer} will pay the bill!")