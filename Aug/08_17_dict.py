# declare dictionary, print out content in for cycle

import os
clear = lambda: os.system('cls')
clear()

s = {"brand": "Mercedes",
     "model": "glc 300 de",
     "production_year": "2016-2023",
     "color": "white"}

for keys,values in s.items():
    txt1 =  " {0} - {1}".format(keys,values)
    print(txt1)
# brand - Mercedes
# model - glc ....
    
