# Reverse the String
def reverse_string(s):
    # Base case
    if len(s) == 0:
        return s
    # Recursive case
    return reverse_string(s[1:]) + s[0]

# Example
text = "hello"
print(reverse_string(text))  # Output: "olleh"