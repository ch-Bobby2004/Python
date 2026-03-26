# remove duplicate characters from a string

text = "programming"

result = ""
for char in text:
    if char not in result:
        result += char

print(result)

text = "programming"

result = "".join(set(text))  #(fast but order not guaranteed)
print(result)


text = "programming"

result = "".join(dict.fromkeys(text))
print(result)