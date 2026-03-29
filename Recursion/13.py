# print the first occurrence of an uppercase character in a string,

def first_uppercase(s, i=0):
    # Base case: reached end of string
    if i == len(s):
        return None
    
    # Check if current character is uppercase
    if s[i].isupper():
        return s[i]
    
    # Recursive call
    return first_uppercase(s, i + 1)

# Example
text = "helloWorld"
print(first_uppercase(text))  # Output: W