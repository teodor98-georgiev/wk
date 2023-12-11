# OK

# def max_range(capacity,consumption):
#     per_100 = consumption/100
#     km_litres = (per_100)**-1
#     range = capacity * km_litres
#     return range
# result = max_range(68,6.8)
# result2 = max_range(57,1)
# result3 = max_range(90,13)
# print("actual car = ", result, "km")
# print("if it's hybrid = ",result2, "km")
# print("with bentley flying spur w12 engine= ", result3, "km")

def ultimate_litres(capacity,consumption,last_range):
    per_100 = consumption/100
    km_litres = (per_100)**-1
    range = capacity * km_litres
    last_litres = (last_range*capacity)/range
    return last_litres
result = ultimate_litres(68,6.8,130)
print("my rav4 = ", result, "litres")


# def max_imposed_range(money_torefill,diesel_price,consumption = 6.8):
#     per_100 = consumption/100
#     km_litres = (per_100)**-1
#     litres_imposed = money_torefill/diesel_price
#     range_imposed = km_litres * litres_imposed
#     return range_imposed
# result2 = max_imposed_range(130,2.66)
# print(result2, "kilometres of max range with 130 lev")



    
    