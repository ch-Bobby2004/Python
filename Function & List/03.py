# add 1 to a number that is stored as a list of digits

def add_one(num):
    carry = 1  # we are adding 1

    # Start from the last digit
    for i in range(len(num) - 1, -1, -1):
        temp = num[i] + carry
        num[i] = temp % 10
        carry = temp // 10

    # If carry is left after processing all digits
    if carry:
        num = [carry] + num

    return num

# Test examples
print(add_one([1, 2, 3]))  # Output: [1, 2, 4]
print(add_one([9, 9, 9]))  # Output: [1, 0, 0, 0]
print(add_one([0]))        # Output: [1]




def add_one_simple(num):
    # If last digit is not 9, just add 1 and return
    if num[-1] != 9:
        num[-1] += 1
        return num
    
    # If last digit is 9, we need to handle carry
    carry = 1
    for i in range(len(num) - 1, -1, -1):
        temp = num[i] + carry
        num[i] = temp % 10
        carry = temp // 10
    
    if carry:
        num = [carry] + num
    
    return num

# Test examples
print(add_one_simple([1, 2, 3]))  # Output: [1, 2, 4]
print(add_one_simple([1, 2, 9]))  # Output: [1, 3, 0]
print(add_one_simple([9, 9, 9]))  # Output: [1, 0, 0, 0]