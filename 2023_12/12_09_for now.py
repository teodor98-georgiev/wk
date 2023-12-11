# find max number initially from 2, then from 4,6,8 numbers. NOTICE - you can use the method which compares 2 numbers
def Max(n1,n2):
    if n1 >= n2:
        return n1
    else:
        return n2

def max_numbers(n1,n2,n3,n4):
    n1_n2_max = Max(n1,n2)
    n3_n4_max = Max(n3,n4)
    return Max(n1_n2_max,n3_n4_max)

def max6_numbers(n1,n2,n3,n4,n5,n6):
    n1_n2_max = Max(n1,n2)
    n3_n4_n5_n5_max = max_numbers(n3,n4,n5,n6)
    return Max(n1_n2_max,n3_n4_n5_n5_max)

def max8_numbers(n1,n2,n3,n4,n5,n6,n7,n8):
    n1_n2_n3_n4 = max_numbers(n1,n2,n3,n4)
    n5_n6_n7_n8 = max_numbers(n5,n6,n7,n8)
    return Max(n1_n2_n3_n4,n5_n6_n7_n8)

result = max8_numbers(9,12,-56,89,3,4,5,90)
print(result)

