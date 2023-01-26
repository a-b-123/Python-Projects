#non-built in Python data structures.
#built in data structures are: strings, lists, tuples, sets, dictionaries

#list comprehension allows us to create a list using a loop in a much more condensed operation
#basic format: new_list = [transform sequence [filter]]

#get values within a range
#the value inputted in the range function is non-inclusive
under10 = [x for x in range(10)] #here, we will get a list of numbers from 0-9
print(str(under10))
print(under10)
#both print the same thing, but converting the elements to strings may be useful if you want to do string operations

squares = [x**2 for x in under10]
#you don't have to use a range function; you can use any sequence data type if you want
print(squares)

odds = [x for x in under10 if x % 2 == 1]
print(odds)

tens = [x * 10 for x in range(20)]
print(tens)

s = ['I run 2 times a day 3 days a week']
nums = [x for x in s if x.isnumeric()]

#get index of a list item
#use enumerate function
names = ['adi','joe','jon','patrick']
idx = [x for x, v in enumerate(names) if v == 'adi']
print([idx[0]])

#delete item 
letters = [x for x in 'ABCDEF']
letrs = [a for a in letters if a != 'C']
print(letters,letrs)

#if-else in list comprehension
#the if-else must come before iteration
nums = [5,2,6,10,7]
newlist  = [x if x%2 == 0 else 10 * x for x in nums]
print(newlist)

#nested loop iteraion in 2D list
#b is the subsets and x is the values
a = [[1,2],[3,4]]
list2 = [x for b in a for x in b]
print(list2)

#stacks, queues, and heaps
#stack is LIFO
#use append() to push an item onto the stack
#use pop() to remove an item. Pop() will also output the value popped
#append and pop are done with the item on top of the stack
#peek() allows us to get the item on top of the stack without removing it
#clear() clears all items from the stack
#before using pop() and peek(), check if the stack is empty

#uses for stacks:
#undo: tracks which commands have been executed. Pop last command off command stak to undo it
#lists are the foundational, underlying structure for creating stacks
my_stack = list()
my_stack.append(4)
my_stack.append(7)
my_stack.append(12)
my_stack.append(19)
print(my_stack)

print(my_stack.pop())
print(my_stack.pop())
print(my_stack)

#we can create a stack class that has a full set of class methods
class Stacks():
    def __init__(self): #constructor
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack)-1]
        else:
            return None
    def __str__(self):
        return str(self.stack)


my_stacks = Stacks()
my_stacks.push(1)
my_stacks.push(3)
print(my_stacks)
print(my_stacks.pop())
print(my_stacks.peek())
print(my_stacks.pop())
print(my_stacks.pop())

#Queues
#queues are FIFO
#enqueue used to add an item to the end of the line. Use append() to enqueue an item
#dequeue used to remove an item from the front of the line. Use popleft() to dequeue an item from the front (left side)
#enqueue is used on one of the queue and dequeue is used from the other end of the stack
#queues are used in waiting lines
from collections import deque
my_queue = deque() #deque is indicating we are creating a double-ended queue
my_queue.append(5)
my_queue.append(10)
print(my_queue)
print(my_queue.popleft())

#Heaps
#The underlying structure of a heap is a list
#a heap is a tree data structre in which each parent node is less than or equal to its child node
#in a max heap, each node is <= to its parent node. max heaps are easy to implement using a list
#public functions of a max heap: push,peek,pop
#private functions: swap,floatUp,bubbleDown,str__. These are background functions, they are not part of the user interface
#push adds value to the end of the array
#floatUp() moves the newly added value to its proper position by comparing it to the values above it
#peek() returns the value at heap[1]
#pop() moves the max to the end of array, deletes it, bubbles the new top value down to its proper position and returns the max
