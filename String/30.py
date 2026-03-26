# Reversing a string
text = "hello"
reversed_text = text[::-1]
print(reversed_text)

text = "hello"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)