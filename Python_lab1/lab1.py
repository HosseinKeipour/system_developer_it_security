"""
Program 1
"""
s = "Lexicon"
print(s[0])
print(s[-1])
print(s[:4])
print(s[-3:])
print(s[-2:])
print(s[::-1])
print(50*'*')
"""
Program 2
"""
my_list = [3,7,[1,4,'hello']]
my_list[2][2] = "goodbye"
print(my_list)
print(50*'*')
"""
Program 3
"""
d1 = {'simple_key':'hello'} 
d2 = {'k1':{'k2':'hello'}} 
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d1['simple_key'])
print(d2['k1']['k2'])
print(d3['k1'][0]['nest_key'][1][0])
print(50*'*')
"""
Program 4
"""
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
print(set(my_list))
print(50*'*')
"""
Program 4
"""
age = 4 
name = "Sammy"
print("Hello my dog's name is {} and he is {} years old".format(name, age))
print(f"Hello my dog's name is {name} and he is {age} years old")