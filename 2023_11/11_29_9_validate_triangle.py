#9 Validate Triangle: Given three angles (input by the user), determine if they can form a valid triangle.
# modified from uncle
def control(an1,an2,an3):       
    sum1 = int(an1) + int(an2) + int(an3)
    if sum1 == 180:
        print("this is a valid triangle")
    else:
        print("imbecile, study a bit the sum must be 180 degrees. {} + {} + {} = {}".format(an1, an2, an3, sum1))

userInp = input("enter 3 angle numbers, split by space. For exit enter only E :")

while userInp != "E":
  str1,str2,str3 = userInp.split()
  total_input = control(str1,str2,str3)
  userInp = input("enter 3 angle numbers, split by space. For exit enter only E :")

print("good bye!")

# zdr debug again    DONE
# BRIEFLY
# in debugging (showing what program do)the block of function (scope of function) is something different from the outside scope 
# because if I start from def the orange index will go soon at the row of calling or in general the row immediatly after the
#end of function's block until founds the caller and than executes the block of function implicitly (without showing the orange
#index that goes into function's block to execute it) thanks with associating args in caller to param in function
#instead, if I start from the block of function the procedure (previous speech) of calling and association args to param 
#is alredy done and in this way the orange index shows what happens in block of function