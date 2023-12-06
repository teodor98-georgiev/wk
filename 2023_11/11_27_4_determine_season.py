# OK!
# 4. Determine the season (spring, summer, fall, winter) based on the user-input month.
# remem. for each condition in multiple statements of if, variables must be explicitly mentioned!!!!

# 1 fix var naming                   done
# 2 improve user note before input   done
# 3 add missing months               done
# 4 make this with method, think     done

def det_season(monthInput):
    if monthInput == "june" or monthInput == "july" or monthInput == "august":
      print("fuck all, let's have bath in see, it's summer!")

    elif monthInput == "septmber" or monthInput == "october" or monthInput == "november":
      print("the winter is coming, what's a sadness")

    elif monthInput == "december" or monthInput ==  "january" or monthInput == "february":
      print("i must be prepared, let's change tyres")

    elif monthInput == "march" or monthInput == "april" or monthInput == "may":
      print("the spring is here, I can hang out")

entering_input = input("enter a month:")
det_season(entering_input)

