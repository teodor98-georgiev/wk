# Water State Checker: Given a temperature input, determine if water at that temperature is in a solid, liquid, or gaseous state

def det_temperature(temperature):
    if temperature <= 0:
        return "the water is in solid state"
    elif temperature <= 100:
        return "the water is in liquid state"
    else:
        return "the water is in gaseous state"
    
insertion = int(input("enter here the temperature in Celsius degrees:"))
verdict = det_temperature(insertion)    #he arguments can be variables or numbers, if they are variables, the cointaining
print(verdict)   # of this variables must be OUTSIDE of the scope function

