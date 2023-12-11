# OK!
#6. Calculate the discount amount and final price based on the original price and a discount percentage. NOTICE: the discount
#percentage must presence in the function's caller

# input 100 leva, imash (input) 20% ottstapka
# output (dicsount amount = 20 leva), (final price = 80 leva)

def discount_amount(price,discount_perc):
     discount_lv = price * (discount_perc/100)
     price_discounted_lv = price - discount_lv
     
     print("final price =", price_discounted_lv)
     print("discount lv =", discount_lv)

discount_amount(1000,20)   


# OK
