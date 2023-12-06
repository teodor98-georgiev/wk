#ex1 
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         return (f"Hello my name is {self.name} and I am {self.age} years old")  #I can call also attributes
# person = Person("Jeremy", 26)
# result = person.greet()
# print(result)

#ex2
# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         return "woof woof"
# dog1 = Dog("Buddy",3)
# print(f"{dog1.name} is {dog1.age} years old")
# dog1.bark()   #the bark method call is not printed or stored anywhere in the code. If you want to see the result, you could add a print statement like this:

#ex3
# class Car():
#     def __init__(self,make,model,year,color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#     def display_info(self):
#         print(self.make)
#         print(self.model)
#         print(self.year)
#         print(self.color)
#     def start_engine(self):
#         print("has started engine")
# car = Car("Daimler", "w221", "2009 year", "white")
# car.display_info()
# car.start_engine()

#ex4
class BankAccount():
    def __init__(self, account_holder, balance, account_number):
        self.account_holder = account_holder    #self.noun are immutable, stay as they are, don't touch them in init method
        self.balance = balance
        self.account_number = account_number

    def display_balance(self):   # in characteristics I do what I want
        formattedbalance = '{:,}'.format(self.balance)
        print(formattedbalance)

    def deposit(self,amount):
        #print(self.balance += amount) #+= is an in-place addition operation, 
      # and I cannot directly use it within the print statement.
        # formatted2 = '{:,}'.format(self.balance)  #NOOOO because formatted 2 and 3 are no attributes of class but only local va.bles of deposit method, they're noaccessible throughout the class. 
        # formatted3 = '{:,}'.format(amount)        # for this reason they have to be initialized in init method, in other words manipulation operations in methods
        # formatted2 += formatted3                 # must be done only with attributes

        # DETAILLY SAID:man. op.ns in methods must be done only with attributes, this ensures that the attributes are initialized when the object is created,
        #   and they can be accessed and modified consistently throughout the class methods.
        # formatedamount = '{:,}'.format(amount)
        self.balance += amount   #example of manipulation operation (math op.ns and concatenation)
        formattedbalance = '{:,}'.format(self.balance)
        print(formattedbalance)
    def withdraw(self,amount):
        if  self.balance >= amount:
            self.balance -= amount
            formattedbalance = '{:,}'.format(self.balance)
            print(formattedbalance)
        else:
            print("the operation cannot be executed because of insufficient founds")

bank = BankAccount("James",18877009797,778638)
bank.display_balance()
bank.deposit(48889788)
bank.withdraw(67909799)

#ex5
#Create a Python class named MathOperations that includes the following methods:

# 1. addition: Accepts two numbers as parameters and returns their sum.
# 2. subtraction: Accepts two numbers as parameters and returns the result of subtracting the second number from the first.
# 3. multiplication: Accepts two numbers as parameters and returns their product.
# 4. division: Accepts two numbers as parameters and returns the result of dividing the first number by the second.
# Make sure to include appropriate comments and docstrings to explain the purpose of each method.
# Additionally, consider adding error handling to handle cases such as division by zero.

# class MathOperations:      # gives error because methods are in init and is not the typical way to structure a class.
#     def __init__(self,alfa,beta):    # and as a result, they are not recognized as class method
#         self.alfa = alfa
#         self.beta = beta
#         if self.alfa or self.beta != 0:
           
#            def addition(self):
#              return self.alfa + self.beta
           
#            def substraction(self):
#              return self.beta - self.alfa
           
#            def multiplication(self):
#              return self.alfa * self.beta
           
#            def division(self):
#              return self.alfa/self.beta
#         else:
#            print("the operation cannot be executed")
# obj = MathOperations(8,9)
# print(obj.addition())
# print(obj.substraction())
# print(obj.multiplication())
# print(obj.division())

class MathOperations():
    def __init__(self,alfa,beta):
        self.alfa = alfa
        self.beta = beta
    def addition(self):
       return self.alfa + self.beta
           
    def substraction(self):
       return self.beta - self.alfa
           
    def multiplication(self):
       return self.alfa * self.beta
           
    def division(self):
       if self.alfa or self.beta != 0:
         return self.alfa/self.beta
       else:
           print("operation cannot be executed")
obj1 = MathOperations(8,78)
obj2 = MathOperations(10,1)
a =(str(obj1.addition()))
b = (str(obj1.substraction()))
c = (str(obj1.multiplication()))
d = (str(obj1.division()))

e = (str(obj2.addition()))
f = (str(obj2.substraction()))
g = (str(obj2.multiplication()))
k = (str(obj2.division()))

print("obj1", "=", a,b,c,d)
print("obj2", "=", e,f,g,k)

#ex6
#Create a Python class named Car with the following attributes and methods:
#attributes
#1. make (string): the make or brand of the car.
#2. model (string): the model of the car
#3. year (int): the manufacturing year of the car.
#4. mileage (float): the current mileage of the car.
#methods
# 1. __init__(self, make, model, year): a constructor that initializes the make, model, year, and sets the initial mileage to 0.
# 2. drive(self, miles): a method that accepts a number of miles driven and updates the mileage of the car.
# 3. get_info(self): a method that returns a string with information about the car, including make, model, year, and current mileage.
class Car():
    def __init__(self,make,model,year,mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
    def drive(self,milesrunned):
        #return (self.mileage += milesrunned) NOOOOO the expression inside the parentheses is interpreted as a tuple, not as an assignment statement.
# assignments in parenthesisi are not allowed
        self.mileage += milesrunned
        #return self.mileage
    def get_info(self):
        print("The car is made by" " "f"{self.make}") 
        print("factory code" " " f"{self.model}")
        print("year" " " f"{self.year}")
        print("has got" " " f"{'{:,}'.format(self.mileage)}" " " "miles until now")
car1 = Car("Daimler AG, Stuttgart (Deutschland)","w222",2014,735)
car2 = Car("Daimler AG, Stuttgart (Deutschland)","w213",2016,252)
print(car1.drive(1000))
print(car2.drive(1000))
car1.get_info()
print()
car2.get_info()
    