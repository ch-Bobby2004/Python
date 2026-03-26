# check whether two strings are anagrams

str1 = "Dormitory"
str2 = "Dirty room"

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Anagram")
else:
    print("Not Anagram")