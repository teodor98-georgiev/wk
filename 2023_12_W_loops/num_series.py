# # Area of a Triangle: Create a program to calculate the area of a triangle given its base and height
# def AreaTriangle(base,height):
#     Area = (base*height)/2
#     return Area
# result = AreaTriangle(2,3)
# print(result)
n = 1
while n <= 20:   # 22 is ore than 20 so it stops, doesn't stop at 19 becuse it's < than 20 and while loop 
    n += 3    # continues until the condition it's true, when it's not true, it doesn' go ahead more
    print(n)

insertion = input("enter here your favourite meal (press q to quit):")
while insertion != "q":
    print ("your fovourite meal is: " f"{insertion}")
    insertion = input("enter another meal:")
print("bye")


