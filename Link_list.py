# Make a node for linklist
class Node:
	def __init__(self, data=None):
		self.data = data
		self.next = None


# Make the linkelist object
class LinkList:

	# init the Head
	def __init__(self, head = None):
		self.head = head

	# Appending new node in linklist
	def appendl(self, node):
		if self.head == None:
			self.head = node
			node.next = None
			return 1
		current  = self.head
		while current.next:
			current = current.next
		current.next = node
		node.next = None

	# Printing the Linklist
	def printl(self):
		if self.head == None:
			print("Link List is empty")
			return -1
		current = self.head
		while current:
			print(current.data ,end = " ")
			print("-------> ", end = " ")
			current = current.next
		print("None")
	
	#Counte the Lenthe of LinkedList
	def lenthl(self):
		lenth = 0
		current = self.head
		if current == None:
			print("Lenth is: ", lenth)
			return -1
		while current:
			lenth += 1
			current = current.next
		print("Lenth is: ", lenth)
		return lenth

	# Add Data in Begining
	def Add_begining(self, node):
		current = self.head
		if current == None:
			self.head = node
			node.next = None
			print("ADD BEGINING DONE!")
			return -1
		temp = current
		self.head = node
		node.next = temp 
		print("ADD BEGINING DONE!")

	#Get the Data by Positione(Exception : self.head)
	def Get_position(self, pos):
		if pos < 1:
			print("Invalide Input")
			return -1
		current = self.head
		if current == None:
			print("None")
			return None
		track = 0
		while track != pos:
			current = current.next
			track +=1
		print(current.data)

	
	# Insert a Data in patcular Position:
	def Insert(self, node, position):
		current = self.head
		if current == None:
			print("Link List is emity")
			return -1

		if position == 0:
			temp = current
			self.head = node
			node.next = temp
			return 0
		#or position > LinkList.lenthl(self) 
		if position < 0:
			print("INVALID INPUT!")
			return -1
		track = 1
		while track != position:
			current = current.next
			track += 1
		node.next = current.next
		current.next = node
		print("DONE GETING POSITION!")


	#Deleting Data from LinkedList
	def Delete(self, data):
		current = self.head
		if current == None:
			print("Link list is Null")
			return -1

		if current.data == data:
			self.head = current.next
			return 0
		check = True
		while check:
			if current.next.data == data:
				current.next = current.next.next
				print("DONE DELETE!=------")
				check = False
				return -1
			current = current.next

	#To Reverse a Singly Linked List
	def Reverse(self):
		current = self.head
		if current == None:
			print("Link List cannot be reverse bec ll is Empty Now!")
			return -1
		
		prev = None
		while current:
			temp = current 
			current = current.next
			temp.next = prev
			prev = temp
		
		self.head = prev
			
		return print("revesr head  =", prev.data)