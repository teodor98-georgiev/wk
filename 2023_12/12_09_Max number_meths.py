# Max number with methods, 
 
# funkciq - da vrashta po-golqmoto ot 2 chisla
# nova funkciq - da izpolzva gornata funkciq, da vrashta po-golqmoto ot 3 chisla    UNABLE
# nova funkciq - da izpolzva gornata funkciq, da vrashta po-golqmoto ot 5 chisla    UNABLE

def Max(n1,n2):     # notice, when I have more than 2 numbers to compare I have to compare each group per 2 numbers 
    if n1 >= n2:
        return n1
    else:
        return n2

def max_numbers(n1,n2,n3,n4):
    n1_n2_max = Max(n1,n2)
    n3_n4_max = Max(n3,n4)
    return Max(n1_n2_max,n3_n4_max)

result = max_numbers(2,5,6,7)
print(result)

# OK