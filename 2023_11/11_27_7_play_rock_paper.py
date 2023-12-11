#7. Create a rock-paper-scissors game where the user can play against the computer.

def playRockPaperSci(userTool):
    compTool = "rock"
    print("mine is:"+compTool)
    if usrInpTool == compTool:
        print("tie game")
    elif usrInpTool == "paper":
        print("loser")
    elif usrInpTool == "scissors":
        print("loser^2")
    else:
        print("SPEAK IN ENGLISH!!")

print("Play, enter rock, scissors or paper:")
usrInpTool = input("enter an element:")

playRockPaperSci(usrInpTool)

# OK




