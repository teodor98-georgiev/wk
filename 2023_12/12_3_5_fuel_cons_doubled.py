#po razhod - litri na 100 km - da vadi izm. km za 1 litar
  #primer - razhod(5,100) da razpechatva ( moje da minete 20km s 1 litar)
def km_1l(litres,km):
    conversion = km/litres
    return conversion

result = km_1l(2.2,100)
print("you can travel",result, "kilometres with one litre")
