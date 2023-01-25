#class function in Python
#a class function is a function we can use in a class to either modify the objects of that
#class where it can give us specific info about objects

#inheritance
#inheritance is where we can define many attributes and functions in a class that we want to use from another class
#and we can create another class that inherits all those attributes
#to use inheritance, follow these steps:
#1 import the class from the file you want
#2 include the class name you are importing next to the parent class
from Chef import Chef
from IndianChef import IndianChef

myChef = Chef()
myChef.chicken()
myChef.special()

myIndianChef = IndianChef()
myIndianChef.special()
myIndianChef.chicken()