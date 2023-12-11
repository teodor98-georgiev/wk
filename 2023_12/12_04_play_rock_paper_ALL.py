#7. Create a rock-paper-scissors game where the user can play against the computer.
import random
def playRock(userTool):
    compTool = "rock"
    print("mine is:"+compTool)
    if userTool == compTool:
        print("tie game")
    elif userTool == "paper":
        print("you won")
    elif userTool == "scissors":
        print("I won")
    else:
        print("SPEAK IN ENGLISH!!")

def playPaper(userTool):
    compTool = "paper"
    print("mine is:"+compTool)
    if userTool == compTool:
        print("tie game")
    elif userTool == "rock":
        print("I won")
    elif userTool == "scissors":
        print("you won")
    else:
        print("SPEAK IN ENGLISH!!")

def playSci(userTool):
    compTool = "scissors"
    print("mine is:"+compTool)
    if userTool == compTool:
        print("tie game")
    elif userTool == "rock":
        print("you won")
    elif userTool == "paper":
        print("I won")
    else:
        print("SPEAK IN ENGLISH!!")

def playALL():
    random_number = random.randint(1,3)
    ask_user = input("enter here your tool:")
    if random_number == 1:
        playRock(ask_user)
    elif random_number == 2:
        playPaper(ask_user)
    elif random_number == 3:
        playSci(ask_user)
playALL()

# ZDR fix - input must be in avariable, not in parameters of each method, because in case of debugging I must see where is problem
# 1. no parameters in playAll   DONE
