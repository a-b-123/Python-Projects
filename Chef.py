#inheritance
#inheritance is where we can define many attributes and functions in a class
#and we can create another class that inherits all those attributes

class Chef:
    
    def chicken(self):
        print("Chef makes a chicken")

    def salad(self):
        print("Chef makes a salad")

    def special(self):
        print("Chef makes the special of the week")

#encapsulation
#encapsulation is when we want to restrict the access to the variables and methods in a class
#this is used to prevent data from being modified
#there are 2 methods used to guard data: public classes (accessible by anyone) and private classes
#(which are not accessible by just anyone)
#how to define private methods and variables:

class Car:
    #private variables can only be modified inside the class, not outside
    #2 underscores indicates private
    __maxspeed = 0
    __name = ""
    def __init__(self):
        self.__updatesoftware() #updatesoftware is a private method and we are calling it inside the class
                                #using 2 underscores indicates a private method is being used
        self.__maxspeed = 200
        self.__name = "supercar"
    def drive(self):
        print("driving")
        print(self.__maxspeed)
    def setspeed(self,speed):
        self.__maxspeed = speed #since this modification of variables is happening inside the class, it is ok
        print(self.__maxspeed)
    def __updatesoftware(self):
        print("updating software")

blackcar = Car() #creating an object blackcar. Whenever we create an object, it will call the init method default so whatever
                 #is in the init method will be outputted
blackcar.drive()
blackcar.__updatesoftware() #if we tried to access this method outside the class without declaring it in init, we would get an error
blackcar.setspeed(100)

#polymorphism is functions which behaves differently for different objects
#basically, you have the same function in different classes, but in each class the body of the function is different