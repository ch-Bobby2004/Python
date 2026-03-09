# Using global Keyword

# If you want to modify a global variable inside a function, use the global keyword.

x = 10  # global

def change_global():
    global x
    x = 20
    print("Inside function, x =", x)

change_global()
print("Outside function, x =", x)