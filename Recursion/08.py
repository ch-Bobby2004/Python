# Check a palindrome or not 
def is_palindrome(s):
    # Base case
    if len(s) <= 1:
        return True
    
    # If first and last characters don't match
    if s[0] != s[-1]:
        return False
    
    # Recursive check on the remaining substring
    return is_palindrome(s[1:-1])

# Example
text = "madam"
print(is_palindrome(text))  # Output: True