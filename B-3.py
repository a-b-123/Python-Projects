#data types in python are strings, int, float, boolean
#you don't need to declare the variable type before the variable name like in
#other languages

name = "Aditya"
age = 70
isMale = True
print("Aditya's name is " + name + " and he is a male? \n",isMale)

#working with strings
phrase = "Hello"
print("Aditya\"\"Bidnur") #using the escape character (\) to print out a quotation mark within the quotes
print(phrase)
print(phrase + " " + "YouTube!") #concatenating strings together
#string functions
print(phrase.lower().islower()) #converts string to lowercase. Use .upper() for uppercase
print(len(phrase)) #prints the length of the string
print(phrase[1]) #prints the character at the specified index in the string. Indexing starts at 0
print(phrase.index("e")) #will return the index position of the parameter passed 
print(phrase.replace("ll","bb")) # will replace the first inputted parameter in the string with the second