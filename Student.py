#Classes and Objects in Python
#C and O make your program organized 
#not everything in the real world can be represented using the Python data types
#like people, items, etc
#C and O's allow us to create our own data types for anything we want to
#A class is basically declaring a new data type that you can use that may not fit the mold of exisitng python data types
#In a class, you give all the attributes of the data type you are creating, using existing data types
#creating a class:
#class <name of class>:

class Student:
    #the initialize function allows us to map out what attributes the data type we are creating will have.
    #in the init function, we are defining all the attributes the class we are creating will have
    #here, a student has a name,major,gpa,and status
    def __init__(self, name, major, gpa, status): 
        self.name = name
        self.major = major
        self.gpa = gpa
        self.status = status
#class function:
    def honors(self):
        if self.gpa >= 3.5:
            print("Honors student")
        else:
            print("Not honors student")


