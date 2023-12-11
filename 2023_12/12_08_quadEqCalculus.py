# Quadratic Equation Solver: Create a program that solves a quadratic equation

def quadEq_calculus(a,b,c):
    delta = ((b**2)-(4*a*c))**(1/2)
    x1 = (-b + delta)/(2*a)
    x2 = (-b - delta)/(2*a)
    if isinstance(delta,complex):
        return "0 real solutions"
    elif delta == 0:
        if x1 == 0:
          #return x2 + "only one real solution"    why not properly works, beacuse int and str are not concatenable (TypeError)
          return str(x2) + "only one real solution"
        elif x2 == 0:
           return str(x1) +  "only one real solution"
    else:
        return x1,x2
    
verdict = quadEq_calculus(3,9,0)
print(verdict)

verdict = quadEq_calculus(0,9,0)
print(verdict)


# ZDR 1. bez vgraden method
# 2. definicionno mnojestvo
# 3. bez str
# 4. 3-4 primera