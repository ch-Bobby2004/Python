try:
    # num = int(input("Enter a number: "))
    num  = 3
except ValueError:
    print("Not a number!")
else:
    print("You entered:", num)
    
    
try:
    file = open("data.txt", "r")
    data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("This runs no matter what.")
    file.close()  # safely close file