def ret(cards):
    if sum(cards) <= 21:
        return sum(cards)
    
    if cards[0] == 11:
      cards[0] = 1
      if sum(cards) <= 21:
        return sum(cards)
      
    if cards[1] == 11:
      cards[1] = 1
      if sum(cards) <= 21:
        return sum(cards)
      
    if cards[2] == 11:
      cards[2] = 1
      if sum(cards) <= 21:
        return sum(cards)
      
    return "BUST"


cards = [[9,10,11],[1,2,3],[11,11,11],[10,9,1],[9,9,11]]

for A123 in cards:
   r1 = ret(A123)
   print(r1)

