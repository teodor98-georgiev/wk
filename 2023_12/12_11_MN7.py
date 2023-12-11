def Max(n1,n2):
    if n1 >= n2:
        return n1
    else:
        return n2
    
def Max7(n1,n2,n3,n4,n5,n6,n7):
    n12_max = Max(n1,n2)
    n123_max = Max(n12_max,n3)
    n1234_max = Max(n123_max,n4)
    n12345_max = Max(n1234_max,n5)
    n123456_max = Max(n12345_max,n6)
    n1234567_max = Max(n123456_max,n7)
    return n1234567_max
result = Max7(0,0,3,9,87,-33,9)
print(result)

# OK