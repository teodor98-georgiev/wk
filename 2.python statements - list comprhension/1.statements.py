# FOR LOOP: used to iterate something over the obj ( for ex iterating over every character
# in a string, or over an element in list ecc).
# ex
#so, what for loop does? assigns a variable to every part of obj and executes the code below the cycle
# as much as times the len of obj (makes iterations)
# used to execute a code several times (this operation is called iteration)
#other words, when I have to scroll elements of obj and as a result in the output I must have things as much as the elements of obj I use for loop
# !!!!!  comment all use ctrl + /   !!!!!

import os
clear = lambda: os.system('cls')
clear()

##for x in range(0,7):
    ##print("yes")

# a = 12
# b = 29

# if a < b:
#     print("well done")
#     for x in range (23,29):
#         print("now get the godds")
# elif a > b:
#     print("are you serious?")
#     for x in range (23,29):
#         print("go back, take your car and you're faired")


# !!!!!! pay attention with dictionaires !!!!! 
# with standard syntax by default python gives me the keys
 
# d = {'year':2019, 'series number': 2388846, 'brand': 'Mercedes'}
# for item in d:
#     print (item)

# If I want to have all I must type:
#d = {'year':2010, 'series number': 2388846, 'brand': 'Mercedes', 'engine volume':'V8', 'horse power': 388, 'model': 'cl500'}
#for item in d.items():
    #print(item)

# or I can type:
#for key,value in d.items():
   #print(value)

# very similar with tuple unpacking:
#elements = [(1,2,3) , (4,5,6) , (7,8,9)]
#for a,b,c in elements:
    #print(b,c)

## WHILE LOOP
#continue to excecute a block of code while some condition remains true       ## x = x+1  ==    x += 1
# syn
# while some boolean condition:
       #do something
# else:
      #wdciuhca

# s = 9
# while s < 10:
#     print('Yes, Im a good programmer')
#     s += 1
# else:
#     print('go on, don t be silly')      # why it gives me else too ?

######## NOT A PART OF STATEMENTS, JUST SOME EXAMPLES TO MEMORIZE   ######################
# ods and evens for cycle

# for i in range (0,10):
#     if i % 2 == 0:
#        print(i)

# let's do a more complicated ex with format
# a = 1

# for letter in 'abcdefghfy':
#     print("At index {} the votation is {}.".format(a,letter))
#     a += 2
## GETTING BACK TO STATEMENTS #####
# instead of using this complicate syn as said up before, there is ENUMERATE comand:

#s = "ggjk"
# enumerate command
# for item in enumerate(s):
#     print(item)

# or I can say:
# for index,letter in enumerate(s):
#     print(index)
#     print(letter)
#     print('\n')
# zip command: used to zipping together two or more lists:
# alpha = [1,2,3,4]
# beta = ['a','b','c']
# gamma = [100,200,300]
# for item in zip(alpha,beta,gamma):
#     print(item)
# using unpacking

# for a,b,c in zip(alpha,beta,gamma):
#     print(c)

# input function: very nice

input("type here your name:")





















 





