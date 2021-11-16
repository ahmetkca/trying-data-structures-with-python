from myTree import BinarySearchTree
from myQueue import myQueue
from main import LinkedList

class Heap(BinarySearchTree):

	class Node(BinarySearchTree.Node):
		def __init__(self, data, left=None, right=None, parent=None):
			super().__init__(data, left, right)
			self.parent = parent

		def hasParent(self):
			return True if self.parent is not None else False

		def isLeftChild(self):
			if self.parent is None:
				return
			return True if self.parent.left == self else False
		
		def isRightChild(self):
			if self.parent is None:
				return
			return True if self.parent.right == self else False

	def __init__(self, root):
		 super().__init__(root)

	def isRoot(self, node):
		return node == self.root

	def findInsertLocation(self):
		if self.isEmpty():
			return self.root
		q = myQueue(LinkedList.Node(self.root))

		while q.is_empty() == False:
			n: BinarySearchTree.Node = q.dequeue().data
			if n.hasLeft() and n.hasRight():
				q.enqueue(LinkedList.Node(n.left))
				q.enqueue(LinkedList.Node(n.right))
			else:
				return n
	
	def swap(self, parent, child):
		tmpChildLeft = child.left
		tmpChildRight = child.right
		
		if parent.left == child:
			child.parent = parent.parent
			child.left = parent
			child.right = parent.right
			if parent.isLeftChild():
				parent.parent.left = child
			elif parent.isRightChild():
				parent.parent.right = child
			parent.parent = child
			parent.left = tmpChildLeft
			parent.right = tmpChildRight
			
		elif parent.right == child:
			child.parent = parent.parent
			child.right = parent
			child.left = parent.left
			if parent.isLeftChild():
				parent.parent.left = child
			elif parent.isRightChild():
				parent.parent.right = child
			parent.parent = child
			parent.left = tmpChildLeft
			parent.right = tmpChildRight
		else:
			tmpParentParent = parent.parent
			parent.parent = child.parent
			child.parent = tmpParentParent
			child.left = parent.left
			child.right = parent.right
			parent.left = tmpChildLeft
			parent.right = tmpChildRight


	# it will swap the given node and its parent recursively until given node is greater than parent
	def swapMinHeap(self, node):
		# if given node doesn't have parent we can assume we swaped with the root node
		# so need to change the root
		if node.parent is None:
			self.root = node
			return
			# if self.isRoot(node):
			# 	self.root = node
			# 	return
			# raise Exception('you cannot swap given node unless it has parent')

		if node.data < node.parent.data:
			self.swap(node.parent, node)
			self.swapMinHeap(node)
		
		return
			

	def insert(self, newNode: BinarySearchTree.Node, startNode=None):
		# use swap and findInsertLocation methods to implement insertion for heap
		if startNode is None:
			self.insert(newNode, self.findInsertLocation())
			return

		# if size is even then use right of the startNode
		# if size is odd then use left of the startNode
		if self.size % 2 == 0:
			# put newNode as a right child of foundNode
			startNode.right = newNode
			newNode.parent = startNode
			self.size +=1
			self.swapMinHeap(newNode)
			
		else:
			# put newNode as a left child of foundNode
			startNode.left = newNode
			newNode.parent = startNode
			self.size +=1
			self.swapMinHeap(newNode)
			
		
		


if __name__ == "__main__":
	root = Heap.Node(100)
	nd1 = Heap.Node(1)
	nd2 = Heap.Node(2)
	nd3 = Heap.Node(30)
	nd4 = Heap.Node(40)
	nd5 = Heap.Node(500)
	nd6 = Heap.Node(600)
	hp = Heap(root)
	hp.preorder()
	hp.insert(nd1)
	hp.preorder()
	hp.insert(nd2)
	hp.preorder()
	nd7 = Heap.Node(0)
	hp.insert(nd7)
	hp.preorder()
	hp.insert(nd3)
	hp.preorder()
	hp.insert(nd4)
	hp.preorder()
	hp.insert(nd5)
	hp.preorder()
	hp.insert(nd6)
	hp.preorder()
	hp.inorder()
	hp.postorder()
	# root.left = nd1
	# root.right = nd2
	# nd1.parent = root
	# nd2.parent = root
	# nd1.left = nd3
	# nd1.right = nd4
	# nd3.parent = nd1
	# nd4.parent = nd1
	# nd3.left = nd5
	# nd3.right = nd6
	# nd5.parent = nd3
	# nd5.parent = nd3
	# hp.swap(root, nd3)
	# v = hp.findInsertLocation()