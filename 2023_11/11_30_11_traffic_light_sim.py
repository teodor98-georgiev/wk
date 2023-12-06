# OK!
#11 Traffic Light Simulator: Write a program that simulates a traffic light. The user inputs a color (red, yellow, green),
#  and the program tells what action to take ("stop", "ready", "go").

def light_action(light):
    if light == "red":
        print("stop")
    elif light == "yellow":
        print("ready??") 
    elif light == "green":
        print("go!")
    else:
        print("light is broken, turn around!")

entering = (input("enter the light:"))
light_action(entering)   # how to do with input repeated numerous times until a condition is true ?


