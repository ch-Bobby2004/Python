# print the frequency of each character in a string
s = "aabbcdeff"
freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

for char in freq:
    print(char, ":", freq[char])