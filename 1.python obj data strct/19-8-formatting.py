import os
clear = lambda: os.system('cls')
clear()

# format: injecting a variable in my string to print
#.format()
# how can i do? "string{}".format("something") ex:

##print("my name is {}".format("Teodor"))

# with multiple variables and indexed them, NW:last element of format must be indexed!!!

##print("my name is {2} {0} {1} {3}".format("Teodor","Iskrenov","Georgiev", "and i come from beautiful balkans"))

# if i use key values:

##print("my name is {c} {a} {b} {d}".format(a = "Teodor",b = "Iskrenov",c= "Georgiev", d = "and i come from rich of pussy balkans"))

# with numbers
e = 20 /7
print("the result is {}".format(e))

# if i wanto to cut some comma numbers the syax is "{value:width.precision f}"

print("the result is {k:16.3f}".format(k = e)) #Nw key in format must be declaired !!!
# f-string ex
s = 12
print(f"his age is {s}")

list = [ 1 , 3, 5]
print(list)
a = list.pop()
print(a)


