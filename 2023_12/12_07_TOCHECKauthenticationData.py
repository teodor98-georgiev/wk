# Simple License Key Validator: Write a program that validates a given license key format (e.g., checks if 
# it contains a certain number of digits/characters). FCKGW-RHQQ2-YXRKT
# FCKGW-RHQQ2-YXRKT

# 123
# asd
# GW-RH-Q2-YX-KT

# length - 17?
# bukvi i cifri
# at which position is separator
# case is upper

# import re
# probe = "AJ89S-DK67YTF-HI90G"
# # print(len(probe))
# match = re.findall(r'\d',probe)
# print(match)
# print(bool(match))

def license_control(insertion_license):
    license = ""+""+""+str(int)+str(int)+"-"+str()+""+""+str(int)+str(int)+"-"+str(int)+str(int)+""+""+""
    if "" is "".upper() in license:
        return "welcome"
    else:
        return "something has gone wrong"

print("insert license as shown in template:")
print("AAAnn-AAAnn-nnAAA for which n stands for number")
insertion_license = (input("Enter here your license:"))
result = license_control(insertion_license)
print(result)

# ZDR 4 metoda - vseki da proverqva samo 1 neshto !!!
# i 1 metod - da gi vika tezi 4
# nov fail

