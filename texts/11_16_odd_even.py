# Write a function that prints the lesser of two given numbers if both numbers are even
# but prints the greater if one or both numbers are odd
def func1(n1,n2):
    if n1 % 2 == 0 and n2 % 2 == 0:
        if n1 <= n2:
            return n1
        else:
            return n2
    else:
        if n1 <= n2:
            return  n2
        else:
            return n1  
testCases = [[18,20],[20,18],[17,20],[20,17]]
for element in testCases:
  res = func1(element[0],element[1])
  print(res)
