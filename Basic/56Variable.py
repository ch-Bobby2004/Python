x = 10  # global variable

def show():
    print("Inside function, x =", x)

show()
print("Outside function, x =", x)



def my_function():
    y = 5  # local variable
    print("Inside function, y =", y)

my_function()
# print(y)  # This will cause an error!