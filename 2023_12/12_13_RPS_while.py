#OK 
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
    comp_choice = random.randint(1,3)
    user_choice = input("enter here your tool or 'exit':")
    
    while user_choice != "exit":
        if comp_choice == 1:
            playRock(user_choice)
        elif comp_choice == 2:
            playPaper(user_choice)
        elif comp_choice == 3:
            playSci(user_choice)
        user_choice = input("enter here your tool or 'exit':")
        comp_choice = random.randint(1,3)
playALL()

