# BMI Category Calculator: Create a program that calculates the Body Mass Index (BMI) and
# categorizes it into underweight, normal, overweight, or obese.

def BMI_calculation(weight,height):
    BMI = weight/height**2
    if BMI <= 18.4:
        return "eat more bread!!, you're underweight"
    elif BMI <= 24.9:
        return "all wright keep this weight, don't gorge more"
    elif BMI <= 39.9:
        return "well, correct your course, you're a bit overweight"
    else:
        return "are you seing yourself in mirror? what for a fat ball you become?"
    
print("tell me weight in kg and height in m and I will tell you what to do")
insertion1 = float(input("enter your weight here:"))
insertion2 = float(input("enter your height here:"))

verdict = BMI_calculation(insertion1,insertion2)
print(verdict)

#izlishna proverka - mahni