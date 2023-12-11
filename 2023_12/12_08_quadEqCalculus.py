# Quadratic Equation Solver: Create a program that solves a quadratic equation

def quadEq_calculus(a,b,c):
    if a == 0:
        return "operation is not executable"
    square_delta = (b**2)-(4*a*c)
    if square_delta < 0:
        return "0 real solutions"
    delta = (square_delta)**(1/2)
    x1 = (-b + delta)/(2*a)
    x2 = (-b - delta)/(2*a)  
    if x1 == 0:
          #return x2 + "only one real solution"    why not properly works, beacuse int and str are not concatenable (TypeError)
        return x2 , "only one real solution"
    elif x2 == 0:
        return x1 , "only one real solution"
    else:
        return x1,x2
    
# verdict = quadEq_calculus(3,9,0)
# print(verdict)

verdict = quadEq_calculus(0,9,71)
print(verdict)


# ZDR 1. bez vgraden method  DONE
# 2. definicionno mnojestvo   DONE
# 3. bez str   DONE
# 4. 3-4 primera   DONE