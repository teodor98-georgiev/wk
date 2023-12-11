#8 Temperature Converter: Create a program that converts temperature from Fahrenheit to Celsius 
# Step2, different def: or vice versa, depending on user input.

# 1. convertFahrToC()
# 2. ?? convertCelcToF()
# 3. user input 2 broq

#   a. from what? (F / C)
#   b. temperature Number? (int)
#  a. ili b. - convertFahrToC or convertCelcToF

def convertFahr_Cels(Fahr):
    return (Fahr - 32)/1.8

def convertCel_Fahr(Cel):
    return (Cel*1.8) + 32

inputFahr = int(input('1.Enter Fahr temperature:'))
inputCels = int(input("2.Enter the Celsius temperature:"))

resultFC = convertFahr_Cels(inputFahr)
print(resultFC)
print("this is temperature measured in Celsius degrees")

resultCF = convertCel_Fahr(inputCels)
print(resultCF)
print("this is temperature measured in Fahrenheit degrees")

# OK