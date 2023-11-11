#statements texts

#1 Use for, .split(), and if to create a Statement that will print out words that start with 's':
import os
clear = lambda: os.system('cls')
clear()

st = 'Print only the words that start with s in this sentence'
a = st.split()
for element in a:
    if 's' in element:
       print(element)
#2 Use range() to print all the even numbers from 0 to 10.

for i in range (0,11):
    print(i)

#3 Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

s = [i for i in range (1,51) if i % 3 == 0]
print(s)

#4 Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
a = st.split()
for element in a:
    if len(element) % 2 == 0:
        print(element)

#5 Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for i in range (1,31):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#6 Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
a = st.split()
list = []
for element in a:
    s = element[0]
    list.append(s)
print(list)

# 6'
list = [ element[0] for element in a]
print(list)
    
    

    





    

    

    


      

    