from main import LinkedList


class myQueue(LinkedList):

    def __init__(self, head: LinkedList.Node = None, tail: LinkedList.Node = None):
        super().__init__(head, tail)

    def enqueue(self, node: LinkedList.Node):
        self.insert_last(node)

    def dequeue(self):
        return self.remove_first()

    def peek_front(self):
        return self.peek_first()

    def peek_back(self):
        return self.peek_last()


if __name__ == "__main__":
    queue = myQueue()
    queue.enqueue(LinkedList.Node('Fuck'))
    queue.enqueue(LinkedList.Node('You'))
    queue.enqueue(LinkedList.Node('Sharyar and Majid'))

    queue.display()
    queue.dequeue()
    queue.display()
