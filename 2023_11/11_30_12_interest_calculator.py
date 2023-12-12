#12. Simple Interest Calculator: Calculate the simple interest for given principal, rate of interest, and time period. 


# ZDR DONE obsajdane   suma. prcent, dni. 100 10 %/den    10 dena 
def int_calc(sum, interest, days):
    percent = 10 / 100
    interestDay = sum*percent
    daysInterest = interestDay*days
    toReturn = sum + daysInterest
    return toReturn

result = int_calc(100, 20, 100)

print(result)




