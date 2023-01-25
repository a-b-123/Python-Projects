#lists in python
#lists are a structure that allows us to store multiple different related data values to use in your program.
#usually, we can only store one value in a variable, but list allows us to store multiple
#creating a list is like creating a variable
#we can store any data type in a list, and we can mix and match data types in the list
#lists can hold millions of values
people = ["Kevin", "Aditri", "Jim", "Raj", "Sam"]
print(people)
#accessing elements of the list by using indices. Indices start at 0
print(people[1])
print(people[-1]) #accessing lists from the rightmost end of the list. The first element at the back of the list is index position -1
print(people[1:]) #will print values from index 1 to the end of the list
print(people[1:3]) # prints values from 1 to 3, but does not print that value at index 3
people[2] = "Mike" #changing value at an index

luckynums = [1,4,5,4,5.5,-2,44]
print(luckynums)
#extend function allows you to add another list to an existing list
people.extend(luckynums)
print(people)
#use append function to add elements to end of a list
people.append("Yash")
print(people)
#insert function allows you to insert an element at any index in the list. The 2 arguments it takes
#are the index position you want to replace the value of and the value you want to replace it with
people.insert(2, "Harry")
print(people)
#remove function allows us to remove an element.
people.remove("Kevin")
print(people)
#.clear() allows us to completely clear the list
#.pop() will pop the last element off the end of the list.

#.index() will tell us if a specific element is in the list by providing the index the element is at, if it is in there
print(people.index("Aditri"))

#.count() will tell us how many of a specific element we have in the list
#.sort() will list the elements in ascending order (or alphabetical)
#.reverse() will print the list in reverse order
#.copy() will make a copy of an existing list
peeps = people.copy()
print(peeps)

#Tuples in Python
#A tuple is a data structure that lets us store different values. Similar to a list, except a few differences,.
#creating a tuple: put the values you want to store in closed parentheses
coordinates = (4,5)
print(coordinates)
#accessing indices of tuples: indices start at 0
print(coordinates[0])
#cannot change the values of tuples after declared, unlike lists
#use () to create tuples and use [] to create lists
#use tuples for data that will never change; main difference between tuple and list is that tuple is immutable
tuplist = [(4,5), (6,7), (30,44)]