import os
clear = lambda: os.system('cls')
clear()
#REMEMBER: in normal indexing start from 0, last index is not considered (I have to put one number more)
# and in str indexing, spaces are considered as characters
#REMEMBER in rev indexing start from right from -1 1st element and spaces are characters 9only in str)

# REMEMBER: A WHILE LOOP in Python is used to repeatedly execute a block of code as long as a certain condition is true.
#  It is typically used when you don't know in advance how many times you need to loop, and you want to keep looping until a specific condition is met.
#ex1
a = [('hui',23),('ale',73),('gio',45)]
# for i in a:
#     print(i)

#ex2: who's the employe of the year ?

# ASK: if I put hours and employ of the year before def why I get error?
#ANS A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
# !!!!!!!! NOTICE: A variable is only available from inside the region it is created. This is called scope. !!!!!!!!!

def check(a):                                 # what i'm doing here: for index scrolls 1st element of a (hui and 23) then looks in if cycle, compares 23 
    hours = 0                                 # with 0, because 23 > is greater than 0 so hours becomes 23 not more 0 and so employe of month is hui, BUT
    employe_month = ''                        # this was the first iteration, at 2nd iteration hours (before was 23) becomes 333, at this moment the employ of 
    for employe,employe_hours in a:           # the month is ale but looking at the 3trd iteration 45 is < than 333 so pc passes this istruction make remaining
        if employe_hours > hours:             # ale like employe of the year
            hours = employe_hours
            employe_month = employe
        else:
            pass
    return(employe_month,employe_hours) 
s = check(a)
print(s)
# I can call my function even with variables:
# name,h = check(a)
# print(name)
# print(h)
# I can check how many items in my funct I have, how?
# item = check(a)
# print(item)

#INTERACTION BETWEEN FUNCTIONS
#ex1: guess location of one over 3 index position
#NOTICE: input always return a string 
# list = ['_','+','_']
# def player_guess():
#     guess = ''
#     while guess not in ['0','1','2']:                   # to make sure guess is correct
        # guess = input("Pick a number: 0,1 or 2")        #go ahead and keep asking me this imput
    # return int(guess)
#['0','1','2'] are as str because as said input gives a str so needs to see str in the probable indexes, than with int I trasform guess in int to directly 
# index off this list
# s = player_guess()
# print(list[s])

#s = 0 or 1 or 2
#list = ['_','+','_']
# list[0] = ''
# list[1] = '1'
# list[2] = ''
# list[s] = ??
# print(list[s])

# def fun(num1,num2):  # NOTICE: when you use return, ALWAYS store the fun in a variable and print the variable, otherwise it won't work
#     return num1+num2
# d = fun(1,3)
# print(d)

# name = "jose"
# print("My name is {}".format(name))

def myfunc(name):
    return "my name is " + name
d = myfunc("jose")
print(d)


def is_even(n):       # function takes one parameter
    if n%3 == 0:
        return True
    else:
        return False
d = is_even(90)       # 90 = argument
print(d)

def is_greater(n1,n2):   
    if n1 > n2:
        return True
    elif n1 <= n2:
        return False
f = is_greater(60,90) # function takes two arguments
print(f)
# WHAT ABOUT MULTIPLE ARGUMENTS ?

# def geg(n1,n2,n3,n4,n5,n6,n7):
#     return sum(n1,n2,n3,n4,n5,n6,n7)
# h = geg(14,27,34,4,5,63,7)
# print(h)

# NO!!!!! def takes 2 or 5 arguments not more. I have to use *arguments or args or any other variable
def fef(*args):
    return sum(args)
    # print(args)
# fef(1,2,3,4,5,6,7)
o = fef(1,3,4,5,7)
print(o)
# REMEMBER--1: if I print any *args from def i get a tuple (iterable) which is very useful
# REMEMBER--2: if i print **kwargs i get back a dictionary, ex commented below:

def myfunc(**kwargs):     
    if 'fruit' in kwargs:
        print("my fruit of choice is {}".format(kwargs["veggie"]))
    else:
        print('I did not find any fruit here')
myfunc(veggie = 'tomatoe')    #"veggie" is a keyword argument 
#     print(kwargs)
# f = myfunc(fruit = "apple")
# **kwargs is very useful because allows me to use this dictionaires later in my function
#keyword arguments = named arguments
# I can use *args and **kwargs at the same time but the order is a must in the calling of function !!!!!!!!!!!
# args and kwargs are a must in the using of outside libraries
def myfunc(*args,**kwargs):
    # print (args)
    # print(kwargs)
    print("I would like {} {}".format(args[2],kwargs['animal']))
myfunc(10,20,30, fruit = 'orange', food = "eggs", animal = "dog")


# REMEMBER 
# ex1: I can write: but is longer and complicated if code is long
# s1 = 34
# def isless():
#     if s1 % 2 == 0:
#         return "I'm g programmer"
#     else:
#         return "Go away fuckin' shit"
# g = isless()
# print(g)

# ex2
# def isless(s1):
#     if s1 % 2 == 0:
#         return "I'm g programmer"
#     else:
#         return "Go away fuckin' shit"
# g = isless(35)
# print(g)

# SOME EXCERCISES IN args and kwargs FROM UDEMY
# ex1
def myfunc(*args):
    return sum(args)
f = myfunc(2,3,4,5,6)
print(f)
#ex2     #NOTICE: I must return out ALWAYS of cycle (but inside function) because when return is executed
# code exits out of function and no further code in the loop or after the loop is executed, as a result list a is never actually appended with even numbers.
def myfunc(*args):
    a = []
    for i in args:
      if i % 2 == 0:
        a.append(i)
      else:
        continue
    return a
k = myfunc(75,22,34,55,3,89,42)
print(k)
# ex3

def myfunc(f):
   l = ""
   for i in range(len(f)):
      if i % 2 == 0:
          l += f[i].upper()
      else:
          l += f[i].lower()
   return l
j = myfunc("Anthropomorphism")
print(j)