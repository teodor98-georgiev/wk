#6. Calculate the discount amount and final price based on the original price and a discount percentage. NOTICE: the discount
#percentage must presence in the function's caller

def discount_amount(price,percentage):
    discount_lv = (price*percentage)/100
    discounted_price = price - discount_lv
    return (f"discounted price in lv : {discounted_price}", f"discount amount in lv : {discount_lv}")

result = discount_amount(100,20)
print(result)
