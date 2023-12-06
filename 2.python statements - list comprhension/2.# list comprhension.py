# LIST COMPRHENSION
# quick way to create a list in python, syn: [expression for item in iterable]

#expression: is what you want to include in the new list
# item: represents each element in the iterable
# for item in iterable specifies the loop and how you want to iterate through the iterable.

import os
clear = lambda: os.system('cls')
clear()
#remind: for cycle is used to do as much operations as the number of elements in my itarable,
#I get a variable that for assigns to each element of iterable and executes the statements below cycle as much as number of elements in the iterable (iteration)
# It's like scrolling something, where there is scrolling I must use for cycle
# !!!!!!!! str obj.cts ARE NOT CALLABLE!!!!



# c = [1,2,3]
# b = a.append(4)
# print(b)
# !!!!!! it gives None because .append() works only with c list, b element is not recognized, if I want a new list called b i have to write:
# c = [1,2,3]
# b = c.append(4)
# b = c
# print(b)

# for asking to uncle what happens if print is in cycle
mystring = 'pro'
mylist = []
for letter in mystring:
    mylist.append(letter)
print(mylist)
# or I can wrtite, syn: variable for variable in iterable:
mylist = [letter for letter in mystring]
#print(mylist)

d = [1,2,3,4,5,6,7,8,9]
for i in d:
    if i % 2 == 0:
        print(i)
# why only first works and at this 2nd I have only 9?   I have to store my comprhension in some variable!!!!!!


sre = [i for i in d if i % 2 == 0]
print(sre)



