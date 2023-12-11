# # Min of Three Numbers: Write a program that finds the maximum of three numbers.
def min_number(n1,n2,n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    elif n3 <= n2 and n3 <= n1:
        return n3

result = min_number(7,3,-71)
print(result)

# sashtite zabelejki    DONE

# with methods and for more numbers
def Min(n1,n2):     # notice, when I have more than 2 numbers to compare I have to compare each group per 2 numbers 
    if n1 <= n2:
        return n1
    else:
        return n2

def min_numbers(n1,n2,n3,n4):
    n1_n2_max = Min(n1,n2)
    n3_n4_max = Min(n3,n4)
    return Min(n1_n2_max,n3_n4_max)


result = min_numbers(2,5,6,7)
print(result)

# ZDR da NE e str()    DONE