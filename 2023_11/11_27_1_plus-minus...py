# OK!
#1. Check if a given number is positive, negative, or zero.

# number = 2
# if number < 0:
#     print("negative")
# elif number > 0:
#     print("positive")
# elif number == 0:
#     print("it's zero, what a shame")

# userInput = int(input("enter the number:"))     # in the 2nd script INPUT COMMAND is STORED and because of this action, 
# if userInput < 0:          # for every condition there is no need to ask multiple times but is suffecient to control the stored   
#     print("negative")    # input (number) with condition and if it's not verified computer skips at next condition.
# elif userInput > 0:
#     print("positive")
# elif userInput== 0:
#     print("it's zero, what a shame")

# if int(input("enter the number:")) < 0:     #where was the error between this 2 scripts? in 1st the input is asked 3 times so if I have 0
#     print("negative")    # as number of input, for each condition (< > == ) will be asked to me to enter the number until the arrive 
# elif int(input("enter the number:")) > 0:   # in last condition in which finaly prints out the result after 3 asks.
#     print("positive")
# elif int(input("enter the number:")) == 0:
#     print("it's zero, what a shame")


# or optimized  
userInput = int(input("enter the number:"))     # in the 2nd script INPUT COMMAND is STORED and because of this action, 
if userInput < 0:          # for every condition there is no need to ask multiple times but is suffecient to control the stored   
    print("negative")    # input (number) with condition and if it's not verified computer skips at next condition.
elif userInput > 0:
    print("positive")
else: 
    print("it's zero, what a shame")
# why? because of fact that < > == are boolean operators built in computer and if two of them are not satisfied the last will be necessarly satisfied
