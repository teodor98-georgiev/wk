#12. Simple Interest Calculator: Calculate the simple interest for given principal, rate of interest, and time period. 

# ZDR DONE popravi !!! proveri s 3 primera
def int_calc(gived_amount, interest, days):
    percent = interest / 100
    interestDay = gived_amount*percent
    daysInterest = interestDay*days
    toReturn = gived_amount + daysInterest
    return toReturn

result1 = int_calc(100, 20, 10)
result2 = int_calc(-100,10,10)
result3 = int_calc(0,0,0)

print(result2)




