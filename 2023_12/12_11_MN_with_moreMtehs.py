# Max numbers with more methods: remember, groups of two numbers and step by step as said, row by row
def Max(n1,n2):
    if n1 >= n2:
        return n1
    else:
        return n2

def Max3(n1,n2,n3):
    n12_max = Max(n1,n2)
    n123_max = Max(n12_max,n3)
    return n123_max

result = Max3(3,4,5)
print(result)

def Max7(n1,n2,n3,n4,n5,n6,n7):
    n12_max = Max(n1,n2)
    n123_max = Max(n12_max,n3)
    n1234_max = Max(n123_max,n4)
    n12345_max = Max(n1234_max,n5)
    n1234567_max = Max3(n12345_max,n6,n7)
    return n1234567_max

result2 = Max7(-1,-4,67,-900,-459,-2,-344)
print(result2)

# OK