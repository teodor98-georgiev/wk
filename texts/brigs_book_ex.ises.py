# if,elif,else
#1
# twinkies = 60
# if twinkies < 100:
#     print("too much bit")
# elif twinkies > 500:
#     print("too much")

#2
# money = 2000
# if (money < 100 or money < 500):
#     print("True1")
# elif (money < 1000 or money < 5000):
#     print("True2")
#3   ????
# ninjas = 40
# if ninjas >= 50:
#     print("Are too much")
# elif ninjas <= 30:
#     print('There going to be fight but I will survive')
# else:
#     print("I can win on them")

#lists, tuples, dicts
# games = ["coding", "sportsgym","freshair in country"]
# foods = ["all except capperi and zucca"]
# favourites = games + foods
# print(favourites)

# ninjaFighters = 25 / 3
# samuraiFighters = 40 / 2
# summing = ninjaFighters + samuraiFighters
# print(summing)

# name = "Teodor"
# surname = "Georgiev"
# final ="%s %s" % (name,surname)
# print(final)

#for loop
# years = list(range(0,16))
# weightEarth = 80
# perclost = 0.16
# weightMoon = weightEarth*perclost
# for year,finalWeight in enumerate(years):
#     finalWeight = weightMoon + year
#     print(year, finalWeight)
# functions
#1
# def weight(weightEarth, perclost):
#     weightMoon = weightEarth*perclost
#     years = list(range(0,15))
#     perYear = []
#     for year,finalWeight in enumerate(years):
#         finalWeight = weightMoon + year
#         perYear += year, finalWeight, "////"
#     return (perYear)                 
# result = weight(100,0.16)
# print(result)

#2 
# def weight(weightEarth, perclost):
#     weightMoon = weightEarth*perclost
#     years1 = list(range(0,6))
#     years2 = list(range(0,20))
#     for year in range(len(years2)):
#         finalWeight = weightMoon + year 
#     return (finalWeight)                 
# result = weight(80,0.16)
# print(result)

#3
def weight(weightEarth = int(input("Weight on Earth:")) ,perclost = float(input("percentage of lost weight:" ))):
    weightMoon = weightEarth*perclost
    years = list(range(int(input("start year ")),int(input("final year:"))))
    perYear = ()
    for year,finalWeight in enumerate(years):
        finalWeight = weightMoon + year
        perYear += (year, finalWeight, "/////")
    return perYear                 
result = weight()
print(result)

# ex from uncle


