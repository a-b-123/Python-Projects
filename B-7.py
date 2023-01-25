#functions in python
#a function is a block of code that performs one specific task
#they help us organize out code better

#creating a function: must use keyword def. Indent after function declaration
def sayhi():
    name = input("Enter your name: ")
    print("Hello" + " " + name)

#after creating the function, you must call it to actually invoke and use it:
#to call function, simply type the name followed by (); provide arguments in the parentheses if you need to
sayhi()

#declaring function with parameters: parameter is a piece of info that we give to the function
def saybye(names, age): #this means you need to provide a name when using this function 
    print("Goodbye" + " " + names + ", you are" + " " + str(age) + "years old")

age = int(input("Enter your age: "))    
saybye("adi", age)

def cube(num):
    return num*num*num #return statement. Anything after the return statement will not get printed.
    
result = cube(3)    
print(result)



