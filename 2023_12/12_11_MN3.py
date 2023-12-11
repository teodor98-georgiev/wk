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

# OK