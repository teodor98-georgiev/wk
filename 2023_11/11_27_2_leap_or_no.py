# OK!
#2. Check if a given year is a century year (ending in 00) and, if so, whether it is a leap year.
# number = "2001"
# if number[2:4] == "0""0" or number[2:4] == "0""4" or number[2:4] == "0""8" or number[2:4] == "1""2" or number[2:4] == "1""6":
#     print("yes it's a century year and leap year")
# else:
#     print("no, doesn't respect the requirements")

# corrected by uncle suggestions
def type_year(year):
    if year % 100 == 0:
        print("it's a century year")
    if year % 4 == 0:  #putting here if instead of elif is an error, because computer automatically goes to next statement
        print("it's a leap year")    # (if previous is verified) #BUT in this case might not be considered an error
    else:
        print("no way of leap year")

yearEntered = int(input("enter the year:" ))
type_year(yearEntered)      

if True:
    print("true1")
if True:
    print("true2")
#
if True:
    print("true1")
elif True:
    print("true2")
# kato gornoto, prosto gornoto e po-kaso
if True:
    print("true1")
else:
    if True:
        print("true2")
