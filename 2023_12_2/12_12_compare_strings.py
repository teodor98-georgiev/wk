# Compare Two Strings: Write a program that compares two strings and checks if they are the same.
str1 = "I am a super soft developer"
str2 = "I am a super doctor"

def comparison_strings(str1,str2):
    if str1 == str2:
        return "strings are the same"
    else:
        return "strings are not the same"
insertion1 = input("enter here the string 1:")
insertion2 = input("enter here the string 2:")
result = comparison_strings(insertion1,insertion2)
print(result)