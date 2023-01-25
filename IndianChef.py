#the indian chef can do anything the generic chef can do
#instead of copying all the functions from the generic chef class, we can use inheritance
#to use inheritance, follow these steps:
#1 import the class from the file you want
#2 include the class name you are importing next to the parent class
from Chef import Chef
class IndianChef(Chef):
    #inside the IndianChef class, we want to use all of the functions from the Chef class
    #def chicken(self):
    #    print("Chef makes a chicken")

    #def salad(self):
    #    print("Chef makes a salad")

    #def special(self):
    #    print("Indian Chef makes the special of the week")
    
    def curry(self):
        print("Indian chef makes chicken curry")
#instead of copy pasting all the code from the Chef class, we use inheritance next to the class name
