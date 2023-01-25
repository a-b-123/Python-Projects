#this file uses the Student class from B-11.py to creat an object of the Student class
#creating an actual instance of a class is an object; the creation of the class is the template
#for the object

from Student import Student

student1 = Student("Aditya", "Math", 3.33, "Active") #here we are creating a Student object
#student1 is an object of the Student class
student2 = Student("Aditri", "Undecided", 3.7, "Non-Active")
print(student1)
#accessing specific attributes of an object:
print(student1.name)
print(student2.gpa)
print(student2.honors())