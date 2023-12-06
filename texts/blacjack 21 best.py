dealA = [9,10,11]
dealB = [1,2,3]
dealC = [11,11,11]
dealD = [10,10,17]
dealE = [8,7,7]

cards = [dealA,dealB,dealC,dealD,dealE]

def ret(cards):
    if sum(cards) <= 21:
        return sum(cards)
    for i in range(len(cards)):
        if cards[i] == 11:
            cards[i] = 1
            if sum(cards) <= 21:
                return sum(cards)
    return "BUSTED"

for deal in cards:
   r1 = ret(deal)
   print(r1)
