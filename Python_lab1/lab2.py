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
    out = ''
    for i in range(len(my_str)):
        if i%2==0:
            out += my_str[i]
    return out

print(stringBits("Hello"))
print(stringBits('Hi'))
print(stringBits('Heeololeo'))
print(40*'=')

def end_other(end, main):
    """
    Program 3
    """
    if end.lower() in main.lower()[-len(main):] or main.lower() in end.lower()[-len(end):]:
        return True
    return False

print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))
print(40*'=')

def doubleChar(s):
    """
    Program 3
    """
    out =''
    for char in s:
        out=out+2*char
    return out

print(doubleChar('The'))
print(doubleChar('AAbb'))
print(doubleChar('Hi-There'))
