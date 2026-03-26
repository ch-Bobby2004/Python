try:
    print(x)  # x is not defined
except NameError:
    print("Variable x is not defined!")


text = "hello"

try:
    text.push()
except AttributeError as e:
    print("Caught an error:", e)



numbers = [1, 2, 3]

try:
    print(numbers[5])
except IndexError as e:
    print("Caught an error:", e)