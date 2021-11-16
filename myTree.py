
class BinarySearchTree:


	class Node:
		def __init__(self, data, left=None, right=None):
			self.data = data
			self.left: BinarySearchTree.Node = left
			self.right: BinarySearchTree.Node = right

		def isLeaf(self):
			return True if (self.left is None and self.right is None) else False

		def hasLeft(self):
			return True if self.left is not None else False

		def hasRight(self):
			return True if self.right is not None else False

	def __init__(self, root):
		self.size = 0
		self.root = root
		if self.root:
			self.size += 1

	def __len__(self):
		return self.size

	def isEmpty(self):
		return self.size == 0


	def insert(self, newNode):
		self.insert(self.root, newNode)

	def insert(self,newNode, node=None):
		if self.isEmpty():
			self.root = newNode
			self.size += 1
			return

		if node is None:
			self.insert(newNode, self.root)
			return

		currentNode = node
		if newNode.data > currentNode.data:
			if currentNode.hasRight():
				self.insert(newNode, currentNode.right)
			else:
				currentNode.right = newNode
				self.size += 1
		else:
			if currentNode.hasLeft():
				self.insert(newNode, currentNode.left)
			else:
				currentNode.left = newNode
				self.size += 1
		return

	def preorder(self, node=None):
		
		if node is None:
			print('Pre-order: ', end=" ")
			self.preorder(self.root)
			print('\n')
			return
		currentNode = node
		print(currentNode.data, end=" ")
		if currentNode.hasLeft():
			self.preorder(currentNode.left)
		if currentNode.hasRight():
			self.preorder(currentNode.right)

	def inorder(self, node=None):
		
		if node is None:
			print('In-order: ', end=" ")
			self.inorder(self.root)
			print('\n')
			return
		currentNode = node
		if currentNode.hasLeft():
			self.inorder(currentNode.left)
		print(currentNode.data, end=" ")
		if currentNode.hasRight():
			self.inorder(currentNode.right)

	def postorder(self, node=None):
		
		if node is None:
			print('Post-order: ', end=" ")
			self.postorder(self.root)
			print('\n')
			return
			
		currentNode = node
		if currentNode.hasLeft():
			self.postorder(currentNode.left)
		if currentNode.hasRight():
			self.postorder(currentNode.right)
		print(currentNode.data, end=" ")
		

if __name__ == "__main__":

	root = BinarySearchTree.Node(25)
	bst = BinarySearchTree(root)
	bst.insert(BinarySearchTree.Node(15))
	bst.insert(BinarySearchTree.Node(50))
	bst.insert(BinarySearchTree.Node(10))
	bst.insert(BinarySearchTree.Node(22))
	bst.insert(BinarySearchTree.Node(35))
	bst.insert(BinarySearchTree.Node(70))
	bst.insert(BinarySearchTree.Node(4))
	bst.insert(BinarySearchTree.Node(12))
	bst.insert(BinarySearchTree.Node(18))
	bst.insert(BinarySearchTree.Node(24))
	bst.insert(BinarySearchTree.Node(31))
	bst.insert(BinarySearchTree.Node(44))
	bst.insert(BinarySearchTree.Node(66))
	bst.insert(BinarySearchTree.Node(90))
	bst.inorder()
	bst.preorder()
	bst.postorder()
	