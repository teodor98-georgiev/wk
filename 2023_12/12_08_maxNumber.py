# Max of Three Numbers: Write a program that finds the maximum of three numbers.
def max_number(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        return str(n1)
    elif n2 >= n1 and n2 >= n3:
        return str(n2)
    elif n3 >= n2 and n3 >= n1:
        return str(n3)
    

result = max_number(3,3,-891)
print(result)

# uslovieto ne e spazeno (take out text DONE)
# ima dupki   DONE 







    

    