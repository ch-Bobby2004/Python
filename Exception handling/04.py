try:
    # x = int(input("Enter a number: "))
    x  = int()
    result = 10 / x
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("Unexpected error:", e)
    
    
# Known errors are handled clearly
# Unknown errors are still caught safely