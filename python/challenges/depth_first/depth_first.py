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

    def depth_first(self, vertex):
        """Accepts a starting node and returns a collection of nodes in the order they were visited. 
        """

        visited, stack = [vertex.value], [vertex]

        while stack:
            top = stack[-1]
            neighbors = self.get_neighbors(top)
            unvisited = []
            if neighbors:
                for child in neighbors:
                    if child.end.value not in visited:
                        unvisited.append(child.end)
            if unvisited:
                child = unvisited[0]
                visited.append(child.value)
                stack.append(child)
            else:
                stack.pop() 
        return visited

if __name__ == "__main__":
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    g = graph.add_node('g')
    h = graph.add_node('h')

    graph.add_edge(a, b)
    graph.add_edge(a, d)
    graph.add_edge(b, c)
    graph.add_edge(c, g)
    graph.add_edge(d, e)
    graph.add_edge(d, h)
    graph.add_edge(d, f)

    expected = [a, b, c, g, d, e, h, f]

    print(graph.depth_first(a))

    pass
