#data structures in Python

#sequence data types: string, list, tuple

#indexing: access any item in a sequence data type using the element's index.
#indexing starts at 0.

#string indexing:
from re import L


a = 'frog'
print(a[3])

#list indexing
b = ['pig','cow','horse']
print(b[1])

#tuple indexing
c = ('apple', "orange", 'banana', 'kiwi')
print(c[1])

#slicing - [start:end-1:step]. We can slice out substrings, sublists, suptuples using indexes
#if you have no third parameter, the step is assumed to be 1
#the start is inclusive and end-1 is inclusive (prints out the element before the number listed)
d = 'computer' #quotes don't count
print(d[1:4]) #start at index 1 and count till index 4 starting from 0 but don't include the 4th index
print(d[1:6:2]) #start at index 1, go till 5 and only print every 2nd element
print(d[3:]) #empty after a colon means go till the end
print(d[:5])#empty before the colon means start at the beginning
print(d[-1]) #negative index starts from the end; this is INCLUSIVE of the last element and indexing from the end starts at 1
print(d[-3:])
print(d[:-2])

#adding/concatenating
#combine 2 sequences of the same type by using +

#string concatenation
e = 'horse' + 'shoe'
print(e)

#list concatenation
f = ['pig', 'cow'] + ['horse', 'dog']
print(f)

#tuple concatenation
#for an element to be considered a tuple, you MUST include a comma after the element
g = ('apple','orange','banana') + ("kiwi","grapes","berries") + ('mango',)
print(g)

#multiply a sequence data type using *

#string
h = 'bug ' * 3
print(h)
#list
i = [8,5] * 3
print(i)
#tuple
j = (2,4) * 3
print(j)

#testing whether an item is or is not in a sequence
#returns boolean values

#string
k = 'bug'
print('u' in k)

#list 
l = ['apple','banana','kiwi']
print('mango' in l)
print('apple' not in l)

#tuple
m = ('harry', 'potter', 'catch')
print('22' in m)

#iterating through items in a sequence

#printing just the item
n = [7,8,10]
for item in n:
    print(item)

#printing the index of the item and the item itself
#enumerate will return both the index of the item and the item itself
o = [3,4,9]
for index,item in enumerate(o):
    print(index,item)

#count the number of items in a sequence
#use the len() function
#string
p = 'bug'
print(len(p))

#list
q = ['pig','cow','horse']
print(len(q))

#tuple
r = ('Kevin','Niklas','Aditya')
print(len(r))

#find the minimum/max item in a sequence lexicographically.
#lexicographically means comparing items with their ASCII value
#you can find the minimum of a sequence that has the same data types, but you can't mix types
#maximum is the same, just use the max() function instead
s = 'bug'
print(min(s)) #'b'

t = ['red','blue','orange','green']
print(min(t)) #blue (alphabetically)

u = ('Kevin','Niklas','Aditya')
print(min(u))

#sum of items in a sequence

#list
v = [2,5,8,23]
print(sum(v))
print(sum(v[-2:]))

#tuple
w = (50,4,5,30)
print(sum(w))
print(sum(w[:3]))

#sorting sequence types returns a new list of items in sorted order
#sorting does not change the original list

#string 
x = 'bug'
print(sorted(x))

#list
y = ['pig','cow','horse']
print(sorted(y))

#tuple
z = ('apple','banana','orange','kiwi')
print(sorted(z))

#sorting by a second letter
#use a lambda function and a key parameter to return the second character
#a key parameter specifies a function to be called on each list element prior to making comparisons 
print(sorted(z,key=lambda k:k[1]))

#count of an item in a sequence

#string
print(x.count('u'))

#list
print(y.count('cow'))

#tuple
print(z.count("orange"))

#getting an index of an item; 
#gives the index of the first occurrence of the item

#string
print(x.index('b'))

#list
print(y.index('horse'))

#tuple
print(z.index('orange'))

#unpacking the items of a sequence into n variables
#assign each element a variable
a,b,c = y
print(a,b,c)

