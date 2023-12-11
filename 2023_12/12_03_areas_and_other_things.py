# ZDR uslovie
import math
def Surf_Per(a,b,c,angle):
    angle_deg = math.radians(angle)
    sin_angle = math.sin(angle_deg)
    high2 = c*sin_angle
    surface = (a*high2)/2
    return surface
# result = Surf_Per(2,3,5,76)
# print("The surface is = ", result, "m2")

def Perimeter(a,b,c):
    perimeter = a + b + c
    return perimeter
# result2 = Perimeter(2,3,5,76)
# print("the perimeter is = ",result2, "m2")

def ResultsTriangle():
    res_surface = Surf_Per(2,3,5,76)
    res_perimeter = Perimeter()
    result = "The surface is = " + res_surface + "m2 " + "the perimeter is = " +  res_perimeter + "m2"
    return result

print_result = ResultsTriangle()
print(print_result)