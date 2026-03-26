# count vowels and consonants in a string

text = "hello world"

vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in text:
    if char.isalpha():  # check only letters
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)