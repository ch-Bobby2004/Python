print("\n🎯" + "="*40 + "🎯")
print("      🔢  GUESS THE NUMBER GAME  🔢      ")
print("            Can you find it?             ")
print("        Levels: Easy | Normal | Hard     ")
print("🎯" + "="*40 + "🎯\n")

import random

# Big welcome/login string
print("""
=========================================
   WELCOME TO THE GUESS THE NUMBER GAME
=========================================
""")

# Login form using input
username = input("Enter your username: ")
password = input("Enter your password: ")

print(f"\nHello {username}! Let's start the game.\n")

# Choose difficulty
print("Choose difficulty level:")
print("1 - Easy (1-10)")
print("2 - Normal (1-50)")
print("3 - Hard (1-100)")

level = input("Enter level (1/2/3): ")

if level == "1":
    number = random.randint(1, 10)
    max_attempts = 5
elif level == "2":
    number = random.randint(1, 50)
    max_attempts = 7
elif level == "3":
    number = random.randint(1, 100)
    max_attempts = 10
else:
    print("Invalid level! Default is Normal.")
    number = random.randint(1, 50)
    max_attempts = 7

# Game loop
attempts = 0
print("\nI have chosen a number. Try to guess it!")

while attempts < max_attempts:
    guess = int(input("Your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations {username}! You guessed the number in {attempts} attempts.")
        break
else:
    print(f"😢 Sorry! You did not guess it. The number was {number}.")