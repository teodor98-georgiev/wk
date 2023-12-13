# Calculate the Perimeter of a Circle: Write a program to calculate the perimeter of a circle
# given its radius.
import math
def Circle_per(radius):
    perimeter = 2*math.pi*radius
    return perimeter
result = Circle_per(3)
print(result)
