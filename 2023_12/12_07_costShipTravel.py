# Shipping Cost Calculator: Calculate shipping costs based on weight and distance. 
# Define different price brackets for varying ranges of weight and distance

# @ up to 100 T or 1000 miles  =   9 lv/T + 18 lv/mile 

# @ up to 1,000 T or 10,000 miles = 7 lv/T + 10 lv/mile

# @ up to 10,000 T or 18,000 miles = 6 lv/T + 5 lv/mile

# @ over 10,000 T or 18,000 miles = 5 lv/T + 3 lv/mile

def cost_shipping(cargoWeight,distance):
    cost_travel = 0
    txt = "your cost ship in lv is "
    if cargoWeight <= 100.5 or distance <= 1000.5:
        cost_travel += cargoWeight*11 + distance*18
        return txt + f"{cost_travel:,}"
    
    elif cargoWeight <= 1000.5 or distance <= 10000:
        cost_travel.append += cargoWeight*9 + distance*10
        return txt + f"{cost_travel:,}"
    
    elif cargoWeight <= 10000 or distance <= 18000:
        cost_travel.append += cargoWeight*7 + distance*5
        return txt + f"{cost_travel:,}"
    else:
        cost_travel += cargoWeight *6 + cargoWeight*0.3
        return txt + f"{cost_travel:,} lv"

insertion_weight = float(input("Enter here cargo weight in kg:"))
insertion_distance = float(input("Enter here distance in miles:"))
 
print(cost_shipping(insertion_weight,insertion_distance))

# ZDR make text formatting not to repeat but to happen at the end of the function

