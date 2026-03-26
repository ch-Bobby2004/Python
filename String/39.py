# reverse the order of words

s = "i love programming"

words = s.split()

for i in range(len(words) - 1, -1, -1):
    print(words[i], end=" ")

s = "i love programming"

print(" ".join(s.split()[::-1]))