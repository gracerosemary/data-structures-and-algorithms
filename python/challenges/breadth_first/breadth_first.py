class Vertex:
    """Vertex class
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Edge:
    """Edge class
    """
    def __init__(self, end, weight=1):
        self.end = end
        self.weight = weight

class Queue():
    def __init__(self, front = None):
        self.front = None
        self.rear = None

    def enqueue(self, vertex):
        vertex = Vertex(vertex)
        if self.is_empty():
            self.front = vertex
            self.rear = vertex
        self.rear.next = vertex
        self.rear = vertex

    def dequeue(self):
        while not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

class Graph:
    """Graph class
    """
    def __init__(self):
        self._adjacency_list = {}

    def size(self):
        """Total number of nodes in the graph.
        """
        return len(self._adjacency_list)

    def add_node(self, value):
        """Adds a new node to the graph and returns node that was just added.
        """
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start, end, weight=1):
        """Adds a new edge between two nodes in a graph.
        """
        if start not in self._adjacency_list:
            raise KeyError('Starting Vertex not found in Graph')
        if end not in self._adjacency_list:
            raise KeyError('Ending Vertex not found in Graph')
        edge = Edge(end, weight)
        adjacencies = self._adjacency_list[start]
        adjacencies.append(edge)

    def get_nodes(self):
        """Returns all of the nodes in the graph as a collection.
        """
        if self.size():
            node_collection = []
            for node in self._adjacency_list.keys():
                node_collection.append(node.value)
            return node_collection
        return "No nodes found"

    def get_neighbors(self, vertex):
        """Returns a collection of edges connected to the given node. Takes in a given node. Includes the weight of the connection in the returned collection. 
        """
        if self._adjacency_list.get(vertex):
            return self._adjacency_list[vertex]

    def breadth_first(self, vertex):
        """Accepts a starting node and returns a collection of nodes in the order they were visited. 
        """
        nodes = []
        nodes.append(vertex.value)
        breadth = Queue()
        breadth.enqueue(vertex)

        while not breadth.is_empty():
            front = breadth.dequeue()
            neighbors = self.get_neighbors(front)
            if neighbors:
                for neighbor in neighbors:
                    if neighbor.end.value not in nodes:
                        nodes.append(neighbor.end.value)
                        breadth.enqueue(neighbor.end)
        return nodes

if __name__ == "__main__":
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    e = g.add_node('e')

    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(c, d)
    g.add_edge(d, e)

    print(g.breadth_first(a))

    pass
