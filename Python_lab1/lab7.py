import re

phrase = 'This is a string and it has some numbers like 5533 and a symbol #hashtag'

# Sequence of digits
out = re.findall(r'\d+', phrase)
print(out)
# Sequence of non-digits
out = re.findall(r'\D+', phrase)
print(out)
# Sequence of whitespace
out = re.findall(r'\s+', phrase)
print(out)
# Sequence of non-whitespace
out = re.findall(r'\S+', phrase)
print(out)
# alphanumeric characters
out = re.findall(r'\w', phrase)
print(out)
# non alphanumeric
out = re.search(r'\W', phrase)
print(out)