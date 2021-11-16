from myQueue import myQueue
from main import LinkedList


class UndirectedGraph:
    class Vertex(LinkedList.Node):

        def __init__(self, data, next=None):
            super().__init__(data, next=next)
            self.visited = False

    class Edge(LinkedList.Node):

        def __init__(self, data, origin, dest, next=None):
            super().__init__(data, next=next)
            self.origin: UndirectedGraph.Vertex = origin
            self.dest: UndirectedGraph.Vertex = dest

    def __init__(self):
        self.edges = LinkedList()
        self.vertices = LinkedList()

    def add_vertex(self, vertex):
        self.vertices.insert_last(vertex)

    def add_edge(self, edge):
        self.edges.insert_last(edge)

    def neighbours(self, vertex):
        neighbours = []
        currentEdge = self.edges.head
        while currentEdge is not None:
            if str(currentEdge.origin.data) == str(vertex.data):
                neighbours.append(currentEdge.dest)
            if str(currentEdge.dest.data) == str(vertex.data):
                neighbours.append(currentEdge.origin)
            currentEdge = currentEdge.next
        return neighbours

    def bfs(self, start_vertex: Vertex):
        q = myQueue()
        q.enqueue(start_vertex)
        start_vertex.visited = True

        while not q.is_empty():
            vertex = q.dequeue()
            print(vertex.data, end=" ")
            for neighbour in self.neighbours(vertex):
                if not neighbour.visited:
                    neighbour.visited = True
                    q.enqueue(neighbour)
        print('\n')

    def display(self):
        currentVertex = self.vertices.head
        while currentVertex is not None:
            print("({})\n \\\n  \\__".format(currentVertex.data),end="")
            for c, neighbour in enumerate(self.neighbours(currentVertex)):
                if c == 0:
                    print(neighbour.data)
                    continue
                print('  |\n  |\n  \\__{}'.format(neighbour.data))
            currentVertex = currentVertex.next
        print('\n')



if __name__ == "__main__":
    graph = UndirectedGraph()
    vertices = []
    for i in range(13):
        vertex = UndirectedGraph.Vertex(i)
        vertices.append(vertex)
        graph.add_vertex(vertex)

    edges = []
    edge1 = UndirectedGraph.Edge(0, vertices[0], vertices[1])
    edge2 = UndirectedGraph.Edge(1, vertices[0], vertices[9])
    edge3 = UndirectedGraph.Edge(2, vertices[9], vertices[8])
    edge4 = UndirectedGraph.Edge(3, vertices[1], vertices[8])
    edge5 = UndirectedGraph.Edge(4, vertices[8], vertices[7])
    edge6 = UndirectedGraph.Edge(5, vertices[7], vertices[10])
    edge7 = UndirectedGraph.Edge(6, vertices[7], vertices[11])
    edge8 = UndirectedGraph.Edge(7, vertices[7], vertices[6])
    edge9 = UndirectedGraph.Edge(8, vertices[7], vertices[3])
    edge10 = UndirectedGraph.Edge(9, vertices[3], vertices[4])
    edge11 = UndirectedGraph.Edge(10, vertices[3], vertices[2])
    edge12 = UndirectedGraph.Edge(11, vertices[6], vertices[5])
    edges.append(edge1)
    edges.append(edge2)
    edges.append(edge3)
    edges.append(edge4)
    edges.append(edge5)
    edges.append(edge6)
    edges.append(edge7)
    edges.append(edge8)
    edges.append(edge9)
    edges.append(edge10)
    edges.append(edge11)
    edges.append(edge12)
    for edge in edges:
        graph.add_edge(edge)
    graph.display()
    graph.bfs(vertices[0])
