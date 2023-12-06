# creating clean repeatable code is a key part of becoming a good programmer
# FUNCTIONS: allows to create blocks of code that can be easily executed many times, without needing to constantly
#rewrite the entire block of code
# syn:                 def name_of_function():
 #             optional: "docstring explains what function do"
#I call function:      name_of_function()
import os
clear = lambda: os.system('cls')
clear()

# def minnie():
#     print("hello")
# minnie()
# more complex:
# def minnie(name):
#     print('hello'+ name)
# minnie('ester')
#or
# def minnie(name):
#   print(f'hello {name}')
# minnie('ester')

# typically instead of print() is used return to send back the result of the function, instead of just printing it out
# return allow us to assign the output of the function to a new variable
# NOTICE: return allows to save the result of function to a variable which can be used in other parts of program:
# def minnie(name):
#    return f'hello {name}'
# variable = minnie('gonzaga')
# print(variable)

# def my(num1,num2):
#    return num1*num2
# hy = my(3,5)
# print(hy)

def check(list):
   for i in list:
      if i % 2 == 0:
         return True
      else:
         return False   # WRONG!!!!!!!!!!!!  because function checks first number but not the rest of the elements because of more 'havier' false
   #return False         correct because in this way I'm sure for cycle will scroll all components of my list (or iterable)
   # or
         #return pass
r = check([1,2,45])
print(r)
# 






  
    

