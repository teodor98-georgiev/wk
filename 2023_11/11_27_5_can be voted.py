# OK!
# 5.  Determine the eligibility of a person to vote based on its age.

# fix  ages and hole (44 ???)    DONE

# age = int(input("Enter the age:"))
# if age >= 45:
#     print("welcome in the governement tribe")
# elif age == 43:
#     print("with a bit italian mafia and tricks we can vote him")
# else:
#     print("to much young, stay away from hell")

def votepossibility(age):
    if age < 65 and age >= 45:
        return "welcome in the government tribe"
    elif age < 44 and age >= 42:
        return "with  bit italian mafia and tricks you'll be with us"
    elif age > 65:
        return("grandaddy, stay at home and rest")
    else:
        return "move on, to much young for the hell"
result = votepossibility(800)
print(result)

