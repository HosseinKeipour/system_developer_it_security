import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

print(characters)
# 
random.shuffle(characters)
print(characters)


if "password" in "passWord134".lower():
    print(True)