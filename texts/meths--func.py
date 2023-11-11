#WARMU    NOTICE: join is used to unite elements of tuple or str!!!!
#Else is used at the end of cycle when no one of previous if and elif are verified
# Write a function that returns the lesser of two given numbers if both numbers are even
# but returns the greater if one or both numbers are odd
def func1(n1,n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        return n1
    else:
        return n2
d = func1(5,9)
print(d)

# Write a function takes a two-word string and returns True if both words begin with same letter
def func2(a,b):
    if a[0]==b[0]:
        return True
    else:
        return False
s = func2("saxophone","faxobeat")
print(s)

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def func3 (f,d):
    if f + d == 20 or d == 20:
        return True
    else:
        return False
g = func3(18,2)
print(g)

# LEV 1
#EX 1
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def func4():
    h = ""
    l = "oldmcdonald"
    for index, char in enumerate(l):   # I used enumerate because if I might use classic i in if below, it won't work, not allows to do math op.ns 
       if index == 0 or index == 3:    # for reason that i'm working with str not with lists, tuples or dicts
          h += char.upper()
       else:
           h += char # not continue because continue skips the operation dictated by if loop at the top
    return h
s = func4()
print(s)

#EX2
#MASTER YODA: Given a sentence, return a sentence with the words reversed
# def func5():
#     k = ""
#     g = ["I", "feel","good"]     
#     for i in reversed(g):
#         k += str(i) + " "    # where was error: loop does his job or rather it iterates from good to I but in the body when I wrote str(g) the k value is substituted
#     return k                 # by the list g, converted entirely in str, so when it iterates from good to I it substitutes str(g) (list g converted entirely to str) 
# h = func5()                  # for every item in list g from good to I, so instead of having good feel I, I get I feel good 3 times with the iteration from right 
# print(h)                     # to left ( three times because of every iteration I have 3 items: good, feel, I)
# EX 3
# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# def func6 (num):
#     if num < 100:
#         print(True)
#     elif num > 10:
#         print (True)
#     elif num == 200:
#         print(True)
#     return func6
# x = func6(13)
# LEV 2
# Ex4 FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#ex.ple

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
# a = [1,3,3,5,6,89,4]
# b = [1,4,5,63,5,7,2,3]
# def find():                                      # don't work because of return statement in else which as definition stops executing and return specified value, like saying: Stop here and return this value.
#     for index,value in enumerate(b[:-1]):        # NOTICE: because of b[index + 1] if I don't write (b[:-1]) but only (b) I risk to get out of bounds of list b
#         if value == 3 and b[index + 1] == 3:     # having the typical error
#             return True                          # to make all this working and make that code instead of controlling 1st pair of elements, controls all them 
#         else:                                    # I have to type:
#             return False
# r = find()
# print (r)

# def find():
#     for index, value in enumerate(b[:-1]):
#         if value == 3 and (b[index + 1]) == 3:     # int is not callable, don't write value(listname[index + 1]), but (listname[index + 1])
#             return True
#     return False    # Return False if no consecutive 3s are found in the ENTIRE list
# r = find()
# print (r)
# so here this modified code checks the entire list for consecutive 3s. If it finds a pair of consecutive 3s at any point in the list, 
# it immediately returns True. If no such pair is found after checking the entire list (because of out return in the for loop) it returns False 
# and exits out of the function

#EX4: Given a string, return a string where for every character in the original there are three characters
# def mult():
#    h = "daimlerw213"
#    d = [i*3 for i in h]
#    p = ''.join(d)
#    return p
# o = mult()
# print(o)

#EX5: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def ret(cards):
    if sum(cards) <= 21:
        return sum(cards)
    
    if cards[0] == 11:
      cards[0] = 1
      if sum(cards) <= 21:
        return sum(cards)
      
    if cards[1] == 11:
      cards[1] = 1
      if sum(cards) <= 21:
        return sum(cards)
      
    if cards[2] == 11:
      cards[2] = 1
      if sum(cards) <= 21:
        return sum(cards)
      
    return "BUST"


cardCalculated = ret([11,10,11])
print(cardCalculated)

cardCalculated = ret([10,10,10])
print(cardCalculated)






















print(cardCalculated)

fb = [8,6,11]
h = ret(fb)
print(h)

fb = [9,4,3]
h = ret(fb)
print(h)


#EX5: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 
# and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
