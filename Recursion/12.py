# Convert decimal number to binary
def decimal_to_binary(n):
    # Base case
    if n == 0:
        return ""
    
    # Recursive call
    return decimal_to_binary(n // 2) + str(n % 2)

# Example
num = 10
result = decimal_to_binary(num)
print(result if result else "0")  # Output: 1010



# For 10:

# 10 ÷ 2 = 5  remainder 0
# 5 ÷ 2 = 2   remainder 1
# 2 ÷ 2 = 1   remainder 0
# 1 ÷ 2 = 0   remainder 1

# Read remainders from bottom to top → 1010