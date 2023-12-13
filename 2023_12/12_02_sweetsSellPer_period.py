#OK!!
# how much did you gained from the lemon and orange selling ?

def gain_day(lemon,orange,price_lemon,price_orange):
    tot1 = lemon*price_lemon
    tot2 = orange*price_orange
    tot = tot1 + tot2
    return tot
result = gain_day(25,5,0.50,1)
result2 = gain_day(34,78,0.50,2)
print(result)
print(result2)










