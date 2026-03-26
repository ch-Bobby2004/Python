# To check if a string is a palindrome

text = "madam"

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
    

text = "Madam"

text = text.lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
    
    
    
    

text = "nurses run"

text = text.replace(" ", "").lower()

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")