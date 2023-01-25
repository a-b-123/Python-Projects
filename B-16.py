#Linked Lists in Python
#Every linked list is composed of nodes, and each node has 2 parts: Data and a pointer to the next node
#nodes can store any type of data
#the last node has data, but no pointer because there is no next node
#the first node is called the root node and we have a pointer to the root
#Linked List operations:
#find(data), add(data), remove(data),print_list()
#Linked List attributes:
#root: a pointer to the first node in the list
#size: the number of nodes in the list
#when we use the add() function, we create a new node and make its pointer point to the root node. The root pointer now points to the 
#newly added root
#when we use the remove() function, we find the value by starting at the beginning and going through the list till we find it.
#to "remove" it, we change the previous node's pointer to the node after the one we want to delete
#doubly linked lists nodes' have data and 2 pointers; 1 pointer to the next node and 1 to the previous node

class Node(object):

    def __init__ (self, d, n = None,p = None):
        self.data = d
        self.next_node = n
        self.prev_node = p
    
    def __str__(self):
        return('(' + str(self.data) + ')')

    def get_next (self):
        return self.next_node

    def set_next (self, n):
        self.next_node = n

    def get_data (self):
        return self.data

    def set_data (self, d):
        self.data = d


class LinkedList (object):

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def get_size (self):
        return self.size

    def add (self, d):
        new_node = Node (d, self.root)
        self.root = new_node
        self.size += 1

    def remove (self, d):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node.get_next()
                self.size -= 1
                return True		# data removed
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        return False  # data not found

    def find (self, d):
        this_node = self.root
        while this_node is not None:
            if this_node.get_data() == d:
                return d
            else:
                this_node = this_node.get_next()
        return None

myList = LinkedList()
myList.add(5)
myList.add(8)
myList.add(12)

print("size="+str(myList.get_size()))
myList.remove(8)
print("size="+str(myList.get_size()))
print(myList.remove(12))
print("size="+str(myList.get_size()))
print(myList.find(5))

#a circular linked list is like regular linked list, except the end node loops back to the root node
#in circular ll, we insert a node we want to add as the second node in the list so we don't have to keep changing the loop

class Nodes(object):

	def __init__ (self, d, n = None):
		self.data = d
		self.next_node = n

	def get_next (self):
		return self.next_node

	def set_next (self, n):
		self.next_node = n
		
	def get_data (self):
		return self.data

	def set_data (self, d):
		self.data = d
		
	def __str__(self):
		return "Node value: " + str(self.data)

class CircularLinkedList (object):

	def __init__ (self, r = None):
		self.root = r
		self.size = 0

	def get_size (self):
		return self.size

	def add (self, d):
		if self.get_size() == 0:
			self.root = Node(d)
			self.root.set_next(self.root)
		else:
			new_node = Node (d, self.root.get_next())
			self.root.set_next(new_node)
		self.size += 1

	def remove (self, d):
		this_node = self.root
		prev_node = None

		while True:
			if this_node.get_data() == d:	# found
				if prev_node is not None:
					prev_node.set_next(this_node.get_next())
				else:
					while this_node.get_next() != self.root:
						this_node = this_node.get_next()
					this_node.set_next(self.root.get_next())
					self.root = self.root.get_next()
				self.size -= 1
				return True     # data removed
			elif this_node.get_next() == self.root:
				return False	# data not found
			prev_node = this_node
			this_node = this_node.get_next()

	def find (self, d):
		this_node = self.root
		while True:
			if this_node.get_data() == d:
				return d
			elif this_node.get_next() == self.root:
				return False
			this_node = this_node.get_next()
		
	def print_list (self):
		print ("Print List..........")
		if self.root is None:
			return
		this_node = self.root
		print (this_node)
		while this_node.get_next() != self.root:
			this_node = this_node.get_next()
			print (this_node)

def main():
	myList = CircularLinkedList()
	myList.add(5)
	myList.add(7)
	myList.add(3)
	myList.add(8)
	myList.add(9)
	print("Find 8", myList.find(8))
	print("Find 12", myList.find(12))

	cur = myList.root
	print (cur)
	for i in range(8):
		cur = cur.get_next();
		print (cur)

	print("size="+str(myList.get_size()))
	myList.print_list()
	myList.remove(8)
	print("size="+str(myList.get_size()))
	print("Remove 15", myList.remove(15))
	print("size="+str(myList.get_size()))
	myList.remove(5)	# delete root node
	myList.print_list()
	
main()
