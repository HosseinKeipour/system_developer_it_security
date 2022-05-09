#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'decryptPassword' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def decryptPassword(s):
    # Write your code here
    password = [''] * 3
    flag = False
    for i in range(len(s)):
        if flag:
            flag = False
            continue
        if i >= len(s)-1:
            if s[i].isdigit():
                password += '0'
                password.insert(0,s[i])
            else:
                password += s[i]
            break
        if s[i].isdigit():
            password += '0'
            password.insert(0,s[i])
        elif s[i].islower() and s[i+1].isupper():
            password[i+2] = s[i+1]+s[i]+'*'
            flag = True
        else:
            password += s[i]
    password = ''.join(map(str, password))
    return password



s = "hAck3rr4nk"
print(decryptPassword(s))
