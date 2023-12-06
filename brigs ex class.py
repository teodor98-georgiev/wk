# ex: insert number of spots of giraffes object taken as example (NOT CLASS GIRAFFES !!!!!)
class Giraffes():
# object of class (or instance of class) = name of class()   (this procedure is called "initialization" > self.attribute = param from init function)
    def __init__(self, spots): # initilization: giving attributes to an object (CONSTRUCTOR)
        self.giraffe_spots = spots # giraffe_spots is an attribute of class Giraffes' instance, spots is a parameter
ozwald = Giraffes(100)
print(ozwald.giraffe_spots)
# once are wrote functions in classes, the same functions can be called from the the following classes but only if the latte
# are daughters of precedently defined classes

#ex2: defining a class of car with some attributes (partly invented)
# class Cars:
#     def __init__(self, color,age):  #self.color, self.age are attributes of obj in this case, but in general they are prefixed by text
#         self.color = color    #giving attribute calling init function to obj cars below (NOT CLASS!!!) = parameter (IN INIT FUNCTION)
#         self.age = age
# car1 = Cars("blue",23)   # creating desired objs
# car2 = Cars("red",20)
# #calling obj
# print(car1.color,car1.age)
# print(car2.color,car1.age)








    






    





