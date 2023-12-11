#10 Simulate a basic ATM machine where a user withdraw ammounts - in which banknots?


# v1.
# 0. (ima banknoti 10 , 01 leva)
# 1. Kolko shte teglite?
# 2. input int ( 12)
# 3. output 
# ( 10 lv x 1 br)
# ( 01 lv x 2 br)

# v2.
# 0. (ima banknoti 50, 20, 10, 5, 01 leva)
# 1. Kolko shte teglite?
# 2. input int ( 123)
# 3. output 
# ( 50 lv x 2 br)
# ( 20 lv x 1 br)
# ( 01 lv x 3 br)

# v1
def withdraw(withdraw):
    banknotes_nom = 10
    monets_nom = 1
    if withdraw > 0:
        cutted = withdraw/10
        banknotes_count = int(cutted)
        monets_count = withdraw % banknotes_nom
        return "your withdraw is given in " + str(banknotes_nom) +  " lv x " + str(banknotes_count) + " banknote" + " and " + str(monets_nom) + " lv x " + str(monets_count) + " monets"
    else:
        return "invalid sum, try again"

withdraw_sum = withdraw(6007)

print(withdraw_sum)

#v2
# def withdraw2(withdraw2):
#     banknotes_nom1 = 5
#     banknotes_nom2 = 10
#     banknotes_nom3 = 20
#     banknotes_nom4 = 50


   