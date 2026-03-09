s1 = 'Hello'
s2 = "Python"
s3 = '''This is
a multi-line
string'''
print(s1)
print(s2)
print(s3)

text = "Python"

print(text[0])   # P
print(text[3])   # h
# Negative Indexing
print(text[-1])  # n
print(text[-2])  # o

# String Slicing
text = "Python"
print(text[0:3])   # Pyt
print(text[2:5])   # tho
print(text[:4])    # Pyth
print(text[3:])    # hon


# Concatenation
a = "Hello"
b = "World"

print(a + " " + b)

# String Methods
text = "python programming"
# dont modify og string create a copy and returen
print(text.upper())      # PYTHON PROGRAMMING
print(text.lower())      # python programming
print(text.title())      # Python Programming
print(text.replace("python", "java"))
print(text.split())


name = "Rahul"

print("Hello", name)
print("Length:", len(name))


# reverse the string

s = "hello world"
print(s[10:-12:-1])
print(s[::-1])
