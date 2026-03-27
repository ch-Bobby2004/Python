# Complete example with try, except, else, finally

try:
    # risky code
    # num = int(input("Enter a number to divide 100 by: "))
    num = 23
    result = 100 / num

except ValueError:
    # Handles invalid input (not a number)
    print("Error: You did not enter a valid number!")

except ZeroDivisionError:
    # Handles division by zero
    print("Error: Cannot divide by zero!")

except Exception as e:
    # Catches any other unexpected exceptions
    print("Unexpected error occurred:", e)

else:
    # Runs only if no exception occurred
    print(f"Success! 100 divided by {num} is {result}")

finally:
    # Runs no matter what
    print("Program execution completed.")