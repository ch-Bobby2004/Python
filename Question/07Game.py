import random

# Options
options = ["Rock", "Paper", "Scissors"]


player = random.choice(options)
computer = random.choice(options)

print(f"Player chose: {player}")
print(f"Computer chose: {computer}")

# Determine winner
if player == computer:
    print("It's a tie!")
elif (player == "Rock" and computer == "Scissors") or \
     (player == "Paper" and computer == "Rock") or \
     (player == "Scissors" and computer == "Paper"):
    print("Player wins!")
else:
    print("Computer wins!")