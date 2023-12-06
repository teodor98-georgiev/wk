## Write a function that prints the lesser of two given numbers if both numbers are even
# but prints the greater if one or both numbers are odd
# when code is complicated and long is better divide it in methods as this example.
def GetMax(n1,n2):
    if n1 < n2:
        return n2
    else:
        return n1
def GetMin(n1,n2):
    if n1 < n2:
        return n1
    else:
        return n2
def func1(n1,n2):
    # name method properly
    if n1 % 2 == 0 and n2 % 2 == 0:
        return GetMin(n1,n2)
    else:  
        return GetMax(n1,n2)
result = func1(16,17)
print(result)
    # 1. implement function to return max from 2 numbers.