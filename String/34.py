# print the first non-repeating character in a string
def first_non_repeating(s):
    for char in s:
        if s.count(char) == 1:
            return char
    return None

print(first_non_repeating("aabbcdeff"))  # Output: c
print(first_non_repeating("aabbccff"))  # Output: None