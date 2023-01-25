#lists in python

#creating a new list
from re import X


a = list()
b = []
c = ['a',25,'dog',9.43] #lists can have different data types
tuple1 = (10,20)
d = list(tuple1) #pass a tuple into list constructor

#list comprehenision
e = [f for f in range(8)] #creates a list of #'s from 0-7
print(e)

f = [i**2 for i in range(10) if i > 4] #squares the values > 4 and passes the squared values to the list
print(f)

#delete a list or item in a list
g = [1,2,3]
del([c[1]])
del(g)

#append an item to the end of a list

c.append(500)
print(c)
#extend appends a sequence to a list
h = [0,9,8]
c.extend(h)
print(c)

#insert an item at a given index of the list
#pass as follows: (index you want to insert,value you want to insert at that index)
c.insert(2,'Hello')
print(c)

c.insert(1,['a','m']) #inserting a list into the 1 index
print(c)

#pop pops the last item from the list and returns that item
c.pop()
print(c)
print(c.pop()) #will pop off the last element, which will be updated from the first pop function

#remove removes the first instance of an item
c.remove("Hello")
print(c)

#reverse reverses the order of a list. This changes the original list
c.reverse()
print(c)

#sort will sort the items in the list and not change the original list
#sorted() sorts and changes the original list
#can't sort lists with mixed data types

#reverse sort will sort items descending
#use the reverse=True parameter to the sort function to sort in descending order
#c.sort(reverse=True)

#**Tuples in Python**
#tuples are immutable,useful for fixed data, faster than lists

#creating a tuple
#x = ()
#x = (1,2,3)
#x = 1,2,3
#x = 2, #the comma tells Python we are declaring a tuple

#passing a list into tuple function
list1 = [2,4,6]
y = tuple(list1)
print(y,type(y))

#tuples are immutable, but its member objects are mutable.
#example, if you have a list in a tuple, you can modify that list
#p = (1,2,3)
#del[p[1]] #DOES NOT WORK 

z = ([1,2],3)
del(z[0][1])
print(z)

#concatenating 2 tuples together is how you add elements to a tuple; you cannot add or append
z += 4,
print(z)

#**Sets in Python**
#sets store unique items, it does not allow duplicates; it is very fast to access compared to Lists
#sets are unordered so you cannot sort them
#math set ops like union, intersect apply to them

#creating a new set:
sets = {3,5,3,5}
print(sets) #python filters out duplicates and will only print out each element once

#y = set()
#list2 = [x,y,z]
#w = set(list2)

#set operations

#add item to a set
sets.add(7)
#remove
sets.remove(7)

#length of set
print(len(sets))

#check membership in set
print(5 in sets)
print(4 in sets)

#pop random item in set (set is not ordered)
print(sets.pop(),sets)

#delete all items from set
#sets.clear()

#mathematical set operations
#intersection: AND- &
#union: OR- |
#XOR: ^
#difference: set1 - set 2
#subset (set2 contains set1): set1 <= set2
#superset (set1 contains set2): set1 >= set2

#dictionaries in Python
#dictionaries are made of key value pairs
#dicts are unordered

#initializing a dictionary 3 ways:
x = {'chicken':22.7,'turkey':13.3,'fish':6.7} #if you initialize with {}, include key:value pairs separated with a colon
print(x)
x = dict([('chicken',22.7),('turkey',13.3),('fish',6.7)])
print(x)
x = dict(chicken=22.7,turkey=13.3,fish=6.7)
print(x)

#dictionary operations

#add OR update item to a dictionary.
#if the key already exists in the dictionary, it will update the value
#if the key does not exist in the dictionary, it will add it to the dictionary
x['shrimp'] = 38.2
print(x)

#delete an item
del(x['shrimp'])

#length of a dictionary
print(len(x))

#delete all items from dict
x.clear()

#delete the entire dictionary
#del(x)

#accessing keys and values in dictionaries

#accessing keys
print(x.keys())
#accessing values
print(x.values())
#accessing BOTH keys AND values
print(x.items())

#check membership in keys
print('chicken' in x.keys())

#check membership in values
print('25.3' in x.values())

#iterating a dictionary
#remember the items in a dictionary are randomly ordered

#iterating for each key and value in the dictionary:
for key in x:
    print(key, x[key]) #x[key] will output the value associated with the key





