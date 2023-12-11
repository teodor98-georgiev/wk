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
    # random_number = 2
    random_number = random.randint(1,3)
    if random_number == 1:
        playRock(input("enter the tool:"))
    elif random_number == 2:
        playPaper(input("enter the tool:"))
    elif random_number == 3:
        playSci(input("enter the tool:"))
# result = playALL(random.randint(1,3))
playALL()


