#calculate area and perimeter of a triangle with different measures of cathets
# ZDR DONE imena na funkcii?
import math
def SurfTriangle(a,c,angle):
    angle_deg = math.radians(angle)
    sin_angle = math.sin(angle_deg)
    high2 = c*sin_angle
    surface = (a*high2)/2
    return surface

def PerTriangle(a,b,c):
    perimeter = a + b + c
    return perimeter

def ResultsTriangle():
    res_surface = SurfTriangle(2,3,5,76)
    res_perimeter = PerTriangle()
    result = "The surface is = " + res_surface + "m2 " + "the perimeter is = " +  res_perimeter + "m2"
    return result

print_result = ResultsTriangle()
print(print_result)