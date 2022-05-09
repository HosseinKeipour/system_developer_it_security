# def even_numbers(function):
#     def wrap(numbers):
#         print("Inside wrapper to check odd/even")
#         if numbers%2 == 0:
#             ret= "Even"
#         else:
#             ret= "Odd!"
#         function(numbers)        
#         return ret
#     print("wrapper function is called")
#     return wrap

# @even_numbers

def decorator(function):
   def wrapper(num):
        print("Inside wrapper to check odd/even")
        if num%2 == 0:
            ret= "Even"
        else:
            ret= "Odd!"
        function(num)        
        return ret
   print ("wrapper function is called")
   return wrapper
#@my_decorator
def myfunction(x):
    print("The number is=",x)
myfunction=decorator(myfunction)
no=10
print ("It is ",myfunction(no))