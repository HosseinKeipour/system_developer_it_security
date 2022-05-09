import re

# pat = 'term'

# text = 'This is a string with term 1, but id does not have the other term'

# print(re.search(pat, text))
# print(re.match(pat, text))
# print(re.findall(pat, text))

# sd*         s followed by 0, 1, or more d
# sd+         s followed by 1, or more d
# sd?         s followed by 0, 1 d
# sd{2}       s followed by minimum 2 d
# sd{2,3}     s followed by minimum 2 and maximum 3 d
# [a-z]          lower case

print(50*'=')
def multi_re_find(patterns,phrase):
    for pattern in patterns:
        print("Searching the phrase using re check: %r" % pattern)
        print(re.findall(pattern,phrase))
        print('\n')

test_phrase = ' This is a string! But it has punctation. How can we remove it?'

test_pattern = ['[a-z]+',
                '[A-Z]+',
                '[a-zA-Z]+',
                '[A-Z][a-z]+'
                ]

test_pattern = [r'\d+',     # digits
                r'\D+',     # non-digits
                r'\s+',     # whitespace
                r'\S+',     # non-whitespace
                r'\w+',     # non white space
                r'\W+',     # alphanumeric char
                r'\W'       # non-alphanumeric char
                ]        
multi_re_find(test_pattern, test_phrase)

print(50*'=')

normal="Hello\nWorld"
print (normal)

raw=r"Hello\nWorld"
print (raw)
