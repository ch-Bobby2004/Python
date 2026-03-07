# coin toss or generate a 0 or 1 randomly
import random


coin = random.randint(0, 1)
print("Coin number:", coin)

if coin == 0:
    print("Result: Head")
else:
    print("Result: Tail")