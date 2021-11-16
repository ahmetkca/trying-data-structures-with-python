class LinkedList:

	class Node:
		def __init__(self, data, next=None):
			self.data = data
			self.next = next

		def __str__(self) -> str:
			return "({}) ==> {}".format(self.data, self.next.data if self.next else None)

	def __init__(self, head: Node = None, tail: Node = None):
		self.size: int = 0
		self.head: LinkedList.Node = head
		self.tail: LinkedList.Node = tail
		self.iterNode: LinkedList.Node = None
		if self.head is not None:
			currentNode = self.head
			tmp = self.head 
			while currentNode is not None:
				self.size += 1
				tmp = currentNode
				currentNode = currentNode.next
			self.tail = tmp

	def __len__(self):
		return self.size

	def is_empty(self) -> bool:
		return self.size == 0

	def display(self):
		if self.is_empty():
			print('Linked list is empty!')
		currentNode = self.head
		while currentNode:
			if currentNode.next != None:
				print(currentNode.data, end=" => ")
			else:
				print(currentNode.data)
			currentNode = currentNode.next
   
	def insert_first(self, new_node):
		new_node.next = self.head
		self.head = new_node
		self.size += 1

	def insert_last(self, new_node):
		if self.is_empty():
			self.head = self.tail = new_node
			self.size += 1
			return

		if self.size == 1:
			self.head.next = new_node
			self.tail = new_node
			self.size+=1
			return

		self.tail.next = new_node
		self.tail = new_node
		self.size += 1

	def remove_first(self):
		removedNode = self.head
		self.head = self.head.next
		self.size -= 1
		return removedNode

	def remove_last(self):
		currentNode = self.head
		while currentNode is not None:

			if currentNode.next == self.tail:
				removedNode: LinkedList.Node = self.tail
				currentNode.next = None
				self.tail = currentNode
				return removedNode
			
			currentNode = currentNode.next
		self.size -= 1


	def insert_after(self, node, new_node):
		new_node.next = node.next
		node.next = new_node
		self.size += 1

	def insert_at(self, i, new_node):
		if i >= self.size:
			raise IndexError('index out of bounds')
		
		if i == 0:
			self.insert_first(new_node)
			return

		if i == self.size-1:
			self.insert_last(new_node)
			return

		currentNode = self.head
		for x in range(0, i-1):
			currentNode = currentNode.next

		new_node.next = currentNode.next
		currentNode.next = new_node

		self.size += 1

	def peek_first(self):
		if self.is_empty():
			raise Exception('Linked list is empty')
		return self.head.data

	def peek_last(self):
		if self.is_empty():
			raise Exception('Linked list is empty')
		return self.tail.data

	def find_by_index(self, index):
		if index < 0 or index > self.size:
			raise IndexError('Index out of range')
		if index == 0:
			return self.head
		c = 0
		currentNode = self.head
		while currentNode is not None:
			if c == index:
				return currentNode
			currentNode = currentNode.next
			c += 1

	def find_by_data(self, data):
		currentNode = self.head
		while currentNode is not None:
			if currentNode.data == data:
				return currentNode
			currentNode = currentNode.next

	def __iter__(self):
		self.iterNode = self.head
		return self

	def __next__(self):
		if self.iterNode is not None:
			tmp = self.iterNode.data
			self.iterNode = self.iterNode.next
			return tmp
		else:
			raise StopIteration


class DoublyLinkedList(LinkedList):

	class Node(LinkedList.Node):

		def __init__(self, data, next, previous):
			super().__init__(data, next)
			self.previous = previous

		def set_next(self, next):
			next.previous = self
			self.next = next

		def __str__(self) -> str:
			tmp = super().__str__()
			return "{} <== {}".format(self.previous.data, tmp)

	def __init__(self, head, tail):
		super().__init__(head, tail)
		if self.head is not None:
			currentNode = self.head
			tmp = None
			while currentNode is not None:
				self.size += 1
				tmp = currentNode
				currentNode = currentNode.next
				
			self.tail = tmp

	def __len__(self):
		return self.size

	def insert_first(self, node):
		if self.head is not None:
			self.head.previous = node
			node.next = self.head
			self.head = node
		else:
			self.head = node
		self.size += 1

	def insert_last(self, node):
		if self.head is None and self.tail is None:
			self.head = self.tail = node
		elif self.tail is not None:
			self.tail.next = node
			node.previous = self.tail
			self.tail = node
		self.size += 1

	def insert_after(self, n, new):
		new.previous = n
		new.next = n.next
		(n.next).previous = new
		n.next = new
		self.size += 1

	def remove(self, n):
		currentNode = self.head
		isRemoved = False
		while currentNode is not None and isRemoved == False:
			if currentNode == n:
				(n.next).previous = n.previous
				(n.previous).next = n.next
				isRemoved = True
			currentNode = currentNode.next
		if isRemoved:
			self.size-=1

	def display(self):
		currentNode = self.head
		while currentNode:
			if currentNode.next != None:
				print(currentNode.data, end=" <=> ")
			else:
				print(currentNode.data)
			currentNode = currentNode.next

	
if __name__ == "__main__":
	print('\nSingly Linked List')
	n2 = LinkedList.Node('Hello', None)
	n3 = LinkedList.Node('World', None)
	n4 = LinkedList.Node('Alien', None)
	n2.next = n3
	n3.next = n4
	ll = LinkedList(n2, None)
	print('initial singly linked list')
	ll.display()
	print(len(ll))
	print('insert first Node PP')
	ll.insert_first(LinkedList.Node('PP', None))
	ll.display()
	print(len(ll))
	print('insert last Node YY')
	ll.insert_last(LinkedList.Node('YY', None))
	ll.display()
	print(len(ll))
	print('insert Node F at index 1')
	ll.insert_at(1, LinkedList.Node('F', None))
	ll.display()
	print(len(ll))
	print('insert Node DD at index 0')
	ll.insert_at(0, LinkedList.Node('DD', None))
	ll.display()
	print(len(ll))
	print('insert Node JJ at index {}'.format(len(ll)-1))
	ll.insert_at(len(ll)-1, LinkedList.Node('JJ', None))
	ll.display()
	print(len(ll))
	print('remove first')
	ll.remove_first()
	ll.display()
	print(len(ll))
	print('remove last')
	ll.remove_last()
	ll.display()
	print(len(ll))

	print('linked list iteration implementation')
	for n in ll:
		print(n)
	exit()
	# Doubly Linked List example
	print('\nDoubly Linked List')
	dll_node1 = DoublyLinkedList.Node('A', None, None)
	dll_node2 = DoublyLinkedList.Node('B', None, None)
	dll_node3 = DoublyLinkedList.Node('C', None, None)
	dll_node4 = DoublyLinkedList.Node('D', None, None)
	dll_new_node5 = DoublyLinkedList.Node('E', None, None)

	dll_node1.set_next(dll_node2)
	dll_node2.set_next(dll_node3)
	dll_node3.set_next(dll_node4)

	print(dll_node2)

	dll = DoublyLinkedList(dll_node1, None)
	print('initial DLL:')
	dll.display()
	print(len(dll))
	print('insert Node E after Node B')
	dll.insert_after(dll_node2, dll_new_node5)
	dll.display()
	print(len(dll))
	print('remove Node C')
	dll.remove(dll_node3)
	dll.display()
	print(len(dll))
	print('insert Node JJ as a first')
	dll.insert_first(DoublyLinkedList.Node('JJ', None, None))
	dll.display()
	print(len(dll))
	print('insert Node FF as a last')
	dll.insert_last(DoublyLinkedList.Node('FF', None, None))
	dll.display()
	print(len(dll))
	print('remove Node A')
	dll.remove(dll_node1)
	dll.display()
	print(len(dll))

