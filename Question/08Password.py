import random
import string

length = 12

chars = string.ascii_letters + string.digits + string.punctuation

password = ''.join(random.choice(chars) for a in range(length))

print("Your password is:", password)