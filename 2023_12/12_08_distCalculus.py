# Distance Between Two Points: Write a program that calculates the distance between two points on a coordinate plane.
def dist_calculus(x1,y1,x2,y2):
    x_dist = (x2-x1)**2
    y_dist = (y2-y1)**2
    quad_sum = x_dist + y_dist
    dist = (quad_sum)**(1/2)
    return dist
result = dist_calculus(-3,-2,-2,-5)
print(result)

result = dist_calculus(0,3,4,0)
print(result)

result = dist_calculus(1.2,2.8,5.2,-0.2)
print(result)

# bravo !