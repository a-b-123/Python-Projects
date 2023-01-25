#working with numbers
#a module in python is a file that we can import into our current python file
#module files have helpful functions, variables, etc. already predefined to use in your program
#you can create a module file on your own with your own functions/variables you want to use. Simply write
#the file and import it into your program to use; you don't have to keep rewriting functions you want to use
#there are also many exisiting modules with existing code for you to use
#2 types of modules:
#1 Built In Modules: modules built in to python language; you already have access to them
#2 External modules: modules not built in to python
#to install python modules, use pip install <python module> in command prompt/terminal
#syntax for using modules:
#import <module name>

#accessing modules:
#moduleName.componentOfModule

from math import * #enables the program to import the math module to use multiple math functions by going out and gathering those functions

print(2)
print(-33.3)
print(2.3474) #simply printing out numbers

print(3 + 4.5)
print(3-4.5) 
print(3*4.5)
print(3/4.5)
print(3*(4+5)) #python follows order of operations
print(10 % 3) # modulus operator (returns remainder)

mynum = 5
print(mynum)
print(str(mynum) + " is how old he is") #converts int to a string

#functions used with numbers
mynum1 = -6
print(abs(mynum1)) #absolute value of a number
print(pow(4,6)) #exponent. First argument is base, second argument is power
print(max(4,14,9)) #returns the maximun value of all the provided arguments. Use min() to find the minimum of arguments
print(round(3.2)) #rounds following normal rounding rules
print(floor( 3.7)) #chops off the decimal point and rounds down no matter what. Using ceil() rounds number up no matter what
print(sqrt(36)) #returns square root of number
