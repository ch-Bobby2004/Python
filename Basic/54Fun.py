# Function with List Processing
def find_max(numbers):
    max_num = numbers[0]

    for num in numbers:
        if num > max_num:
            max_num = num

    return max_num

nums = [5, 8, 2, 10, 3]
print("Largest number:", find_max(nums))




# *args (Multiple Arguments)

# *args allows a function to accept many arguments.
# Here *args collects all numbers into a tuple.
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers(2, 4, 6))
print(add_numbers(1, 2, 3, 4, 5))




# **kwargs (Keyword Arguments)
# **kwargs allows a function to accept many keyword arguments.

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Rahul", age=20, course="Python")



# Lambda Functions
# A lambda is a short anonymous function.
square = lambda x: x * x

print(square(5))

add = lambda a, b: a + b
print(add(3, 7))


# Built-in Functions
# Python already has many built-in functions.

# Examples:

numbers = [4, 8, 2, 10]

print(len(numbers))   # length
print(max(numbers))   # largest
print(min(numbers))   # smallest
print(sum(numbers))   # total



def add_numbers(a,*args):
    a=7
    total = 0
    for num in args:
        total += num
    return total

print(add_numbers("dfajk",2, 4, 6))
print(add_numbers(1, 2, 3, 4, 5))