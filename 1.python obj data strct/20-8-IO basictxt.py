import os
clear = lambda: os.system('cls')
clear()

# when i open a text file saved in python script or py ntebook
myfile = open("file to open.txt")
myfile.read() # transforms all that is in my file in string. When i use it it's like i have a cursor that seeks the file,
# when i try to re-read i get an empty string, do i need to get on the initial position the cursor:
myfile.seek(0)
myfile.read()
myfile.readlines() #everything gets in a list with several lines for each lines in myfile

# when file is saved somewhere in pc i have to pass the entire path
## myfile = open(C:Users\\...)

myfile.close() # to close it and to avoid any errors of opened files

# a speedy comand to open and close at the same time is using with command:
with open ("myfile.txt") as whatever_I_call_it:
    storage_variable_of_whatever_I_call_it =  whatever_I_call_it.read()
# read files and overwrite files:
with open("myfile.txt" , mode = "r"):
    stored_variable_.. = myfile.read()
# to add something at my file i can use: filename.write("this to add") at the indentation of with:
with open("myfile.txt" , mode = "a"):
    stored_variable.write("this to add")
# then I rewrite below the upper code and i will get the modified file

# all this mode = ... and below read, write ecc are called permisions 




