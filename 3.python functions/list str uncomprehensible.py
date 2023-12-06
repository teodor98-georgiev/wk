import os
clear = lambda: os.system('cls')
clear()


my_list = ["apple", "banana", "cherry"]
result_string = ""
for item in my_list:
    result_string += item + ", "
# Remove the trailing comma and space
result_string = result_string[:-2]
print(result_string)