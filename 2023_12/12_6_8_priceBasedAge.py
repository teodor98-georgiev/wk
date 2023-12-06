# Age-Based Ticket Pricing: Write a program that changes ticket prices based on age categories (child, adult, senior).
#bilet zopark 10 lv, 5 lv wsrastni 2 lev deca
def change_price(age):
    if age <= 15:
        return "the price to enter is 2 lv"
    elif age > 16 and age <=24:
        return "the price is 5 lv"
    elif age >= 65:
        return "the price is 6 lv"
    else:
        return "the price is 10 lv"
insertion_age = int(input("enter your age:"))
result = change_price(insertion_age)
print(result)
    