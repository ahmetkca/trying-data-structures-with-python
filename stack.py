from main import LinkedList


class Stack(LinkedList):

	def __init__(self, head=None, tail=None):
		super().__init__(head, tail)

	def push(self, node):
		self.insert_first(node)
	
	def pop(self):
		return self.remove_first()

def getOpposite(a):
	if a == ']':
		return '['
	elif a == ')':
		return '('
	elif a == '}':
		return '{'


openings = ('[', '(', '{')
closings = (']', ')', '}')

def checkValidity(inp: str):
	s = Stack()
	for i in inp:
		if i in openings:
			s.push(LinkedList.Node(i))
		elif i in closings:
			if s.is_empty():
				return False
			if getOpposite(i) != s.pop().data:
				return False
	if s.is_empty():
		return True
	else:
		return False

if __name__ == "__main__":

	a = '[2+((3*4)+{2-4})][]'
	print(checkValidity(a))
	exit()
	s = Stack(None, None)
	s.display()
	s.push(LinkedList.Node(12, None))
	s.push(LinkedList.Node(7, None))
	s.push(LinkedList.Node(79, None))
	s.display()
	print('\nPopped: {}'.format(s.pop()))
	s.display()
	print('\n')
	print('\nPopped: {}'.format(s.pop()))
	s.display()
	print('\n')
	print('\nPopped: {}'.format(s.pop()))
	s.display()
	print('\n')