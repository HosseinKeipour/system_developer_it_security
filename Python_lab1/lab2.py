def arrayCheck(my_list):
    """
    Program 1
    """
    if str([1,2,3])[1:-1] in str(my_list):
        return True
    else:
        return False

print(arrayCheck([1, 1, 2, 3, 1]))
print(arrayCheck([1, 1, 2, 4, 1]))
print(arrayCheck([1, 1, 2, 1, 2, 3]))
print(40*'=')

def stringBits(my_str):
    """
    Program 2
    """
    return my_str[::2]

print(stringBits("Hello"))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))
print(40*'=')

def end_other(a, b):
    """
    Program 3
    """
    if a.lower() in b.lower()[-len(b):] or b.lower() in a.lower()[-len(a):]:
        return True
    return False
    # a =a.lower() 
    # b = b.lower()
    # return a.endswith(b) or b.endswith(a)

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
print(40*'=')

def doubleChar(s):
    """
    Program 4
    """
    out =''
    for char in s:
        out=out+2*char
    return out

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))
