# largest (longest) word in a string,


s = "Python is a powerful programming language"

words = s.split()
print(words)
largest = ""

for word in words:
    if len(word) > len(largest):
        largest = word

print("Largest word:", largest)