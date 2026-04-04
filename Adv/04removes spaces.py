# .lstrip() → removes spaces from the left of a string.
s = "   hello "
s = s.lstrip()
print(s)  # "hello "
# .strip() → removes both left and right spaces
s = "   hello   "
s = s.strip()
print(s)  # "hello"


encodedText = "ch   ie   pr"
rows = 3

# After diagonal read
result = "cipher   "

# Remove trailing spaces
decoded = result.rstrip()
print(decoded)  # "cipher"