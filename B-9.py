#dictionaries in Python
#a dictionary is a structure that allows us to store info in key-value pairs
#we create these pairs, and when we want to access a certain piece of info, we can access it
#by its key

#creating a dictionary; create a dictionary inside the curly brackets
monthConversions = {
    #the values on left of colon is key and right side is value
    #each key must be unique; you can't have duplicates
    "Jan": "January",
    "Feb":"February",
    "Aug": "August",
    "Dec": "December",
    "Oct": "October",
    "Jul": "July",
}
#accessing a specific key or value: dictionaryName[key]
print(monthConversions["Jul"]) #this will return the value for the key "Nov"
print(monthConversions.get("Oct")) #get function also returns value. Get allows us to pass non-exisitng values along with values
# to use: get(non-exisitng key, value for non-exisiting keys)

#while loops: syntax is while condition:
#while loop is a structure that allows us to loop through and execute block of code multiple time
#as long as the condition is True
i = 1
while i <= 10:
    print(i)
    i += 1
print("Done with loop")

#for loops: syntax is for "variable" in collection
#the variable represents a different value everytime we go through the for loop. Used in every loop iteration
#and will most likely have different value each iteration
#for loop allows us to loop over different collections of items. Used through arrays, letters in strings,
#numbers, etc.
for letter in "Aditya":
    print(letter) #prints each letter in the string "Aditya"
#for loop through array
sports = ["soccer", "football", "basketball", "cricket", "golf"]
for sport in sports:
    print(sport)
#for loop through range of numbers. The second number in range function does not get included and not get printed
for index in range(10): #prints from 0-10, NOT including 10
    print(index)
for value in range(3,10): #prints nums from 3-10, not including 10
    print(value)
#using len to go through array
len(sports)
for sport in range(len(sports)):
    print(sport)

for num in range(5):
    if num == 0:
        print("First iteration")
    else:
        print("Not first")

#exponent function
def exponent(base,power):
    result = 1
    for index in range(power): #range is 0 to the indicated value but not including the indicated value
        result = result * base
    return result 
user = int(input("Enter the power you want to use: "))
print(exponent(3,user))
