#WARMUP    NOTICE1: join is used to unite elements of tuple or str!!!!    NOTICE2: every variable must be written with a purpose, print by default prints content and new row!!!
#Else is used at the end of cycle when no one of previous if and elif are verified

# Write a function that returns the lesser of two given numbers if both numbers are even
# but returns the greater if one or both numbers are odd
# def func1(n1,n2):
#     if n1 % 2 == 0 and n2 % 2 == 0:
#         if n1 < n2:
#             return n1
#         elif n1 > n2:
#             return n2
#     else:
#         if n1 < n2:
#             return n2
#         elif n1 > n2:
#             return n1    
# res = func1(20,25)
# print(res)

# Write a function takes a two-word string and returns True if both words begin with same letter
# def func2(a,b):
#     return a[0]==b[0]
#     # if a[0]==b[0]:
#     #     return True
#     # else:
#     #     return False
# result1 = func2("saxophone","saxobeat")
# print(result1)
#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
# def func3 (f,d):
#     if f + d == 20 or f == 20 or  d == 20:
#         return True
#     else:
#         return False      
# g = func3(1,2)
# print(g)

# LEV 1
#EX 1
#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
# def func4():
#     h = ""
#     l = "oldmcdonald"
#     for index, char in enumerate(l):   # I used enumerate because if I might use classic i in if below, it won't work, not allows to do math op.ns 
#        if index == 0 or index == 3:    # for reason that i'm working with str not with lists, tuples or dicts
#           h += char.upper()
#        else:
#            h += char # not continue because continue (as definition it skips operation of if) skips the operation dictated by if loop at the top
#     return h
# s = func4()
# print(s)

# or optimized
def capitalize1and4(name):
    parts = [name[0].upper() , name[1:3] , name[3].upper() , name[4:]]
    return "".join(parts) 
kapitalized = capitalize1and4("oldmcdonald")
print(kapitalized)
    


#EX2
#MASTER YODA: Given a sentence, return a sentence with the words reversed
# def func5(): 
#     k = ""
#     g = ["I", "feel","good"]     
#     for i in reversed(g):
#         k += i + " " 
#     return k                  
# h = func5()                   
# print(h)  # or I can write:

# d = "I feel good"
# k = d.split()
# k = [i for i in reversed(k)]
# print(" ".join(k))   #exactly the same (NOTICE: "" are for space between elements in join(variable)

# EX 3
# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# def func6 (num):
#     if num <= 200 or num >= 10:
#        return True
# x = func6(199)
# print(x)

# LEV 2
# Ex1 FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
#ex.ple

# has_33([1, 3, 3]) → True
# has_33([1, 3, 1, 3]) → False
# has_33([3, 1, 3]) → False
a = [1,3,3,5,6,89,4]
b = [1,4,5,63,5,7,2,3]
# def find():                                      # don't work because of return statement in else which as definition stops executing the function and returns specified value, like saying: Stop here and return this value.
#     for index,value in enumerate(b[:-1]):        # NOTICE: because of b[index + 1] if I don't write (b[:-1]) but only (b) I risk to get out of bounds of list b
#         if value == 3 and b[index + 1] == 3:     # having the typical error
#             return True                          # to make all this working and make that code instead of controlling 1st pair of elements, controls all them 
#         else:                                    # I have to type:
#             return False
# r = find()
# print (r)

def find():
    for index, value in enumerate(b[:-1]): #  If I use b instead of b[:-1], the loop would iterate over all elements of
        if value == 3 and (b[index + 1]) == 3: # b and in the last iteration, when index points to the last element, b[index + 1] would result in an IndexError because there is no element beyond the last one.
            return True   # int is not callable, don't write value(listname[index + 1]), but (listname[index + 1])
    return False    # Return False if no consecutive 3s are found in the ENTIRE list
r = find()
print (r)
# so here this modified code checks the entire list for consecutive 3s. If it finds a pair of consecutive 3s at any point in the list, 
# it immediately returns True. If no such pair is found after checking the entire list (because of out return in the for loop) it returns False 
# and exits out of the function

#EX2: PAPER DOLL Given a string, return a string where for every character in the original there are three characters
def mult():
   h = "daimlerw213"
   d = [i*3 for i in h]
   p = ''.join(d)
   return p
o = mult()
print(o)
# or I can write without list comprehension which is more practical 

def mult2():
    name_to_multiply = "daimlerw213"
    str_concatenated = ""
    for letter in name_to_multiply:
        str_concatenated += (letter*3)
    return(str_concatenated)
result = mult2()
print(result)

#EX3: BLACKJACK Given three integers between 1 and 11, if their sum is less than or equal to 21, 
# return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
# def mult():
#     a = [5,7,8]
#     for number in range(len(a)):    #INT IS NOT SUBSCRIPTABLE AND ITERABLE !!!!!!!!
#         if sum(number[0:]) <= 21:
#             return sum
#         elif sum(number[0:]) > 21 and number == 11:
#             return sum(number[0:]) - 10
#         else:
#             return "BUST"
# result = mult()
# print(result)

# def mult():
#    a = int(input("number1:"))
#    b = int(input("number2:"))
#    c = int(input("number3:"))
#    suma = a + b + c
#    if suma <= 21:
#        return suma
#    else:
#        return "BUSTED"  
# result = mult()
# print(result)

#EX4 SUMMER OF 69: Return the sum of the numbers in the array, except ignore sections of numbers starting 
#with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.def summatory():
# def summer(): ???

#challenging problems
#SPY GAME:Write a function that takes in a list of integers and returns True if it contains 007 in order
# a = [7,2,6,3,9]
# b = [[2],[3],[0],[9],[7],[0],[7]]
# c = [[1],[3],[4],[6],[0],[4],[0],[7]]
# def spy(inpArr):
#     tarsim = "parvo_chislo"
#     for element in b:
#         if tarsim == "parvo_chislo" and element == 0 in b:
#            tarsim = "vtoro_chislo"
#            continue
#         elif tarsim == ... and element = .... in b:
#             tarsim = 
#             continue
#         elif tarsim == ... and element = .... in b:
#             return True
#         else:
#     return "no order like this"
# out = spy()
# print(out)


    