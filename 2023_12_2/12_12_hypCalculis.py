# Pythagorean Theorem Calculator: Develop a program to calculate the hypotenuse of a right triangle.
def hyp(cath1,cath2):
    hyp = ((cath1**2) + (cath2**2))**(1/2)
    return  hyp
result = hyp(3,3)
print(result)
