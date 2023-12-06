# OK
#made by me
def check_triangle(an1,an2,an3):     # the function work starts from its calling or from the row under the function block
    sum = an1 + an2 + an3     # attention with debugging, if I start from def the block function will be executed               
    if sum == 180:            #implicitly (the debug procedure won't viualize the block of function)
        print("that's a valid triangle")
    else:
        print(sum, "imbecile, the sum must be 180 degrees")

check_triangle(89,100,3)

