
import os
clear = lambda: os.system('cls')
clear()

# EX1: map function allows to substitute some normal code when I use for cycle for some operations. syn: map(func,iterable)
a = [1,2,3,4]   # It loops over each item (that means it produces an iterator) of an iterable and applies the transformation function to it. 
def square(k):    # Then, it returns a map object that stores the value of the transformed item.
    return k**2
for i in map(square,a):
    print(i)
print ("")
# EX2: filter function
n = [1,2,3,4,6,7,88,93]
def even(num):
    return num%2 == 0
for i in filter(even,n):
    print(i)
# lambda expression ( or known as anonymous function)
#EX2
# def gh(num):
#     return num/2
# gh(88)

# but it's equals to:
# def gh(num): return num/2
# gh(88)

# OR
gh = lambda num: num**2
print(gh(6))
# often it is used combined with map and filter:
yu = list(map(lambda num: num**2,n))                             #!!!!! returns an iterator, and it does not modify the original iterable in place. 
print(yu)                                   # If I want to get the operation of function and print result, I need to convert the 
                                             # result of map to a list or any iterable or iterate over it.list

    

