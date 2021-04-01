class Graph:
    """Graph class
    """
    def __init__(self):
        self._adjacency_list = {}

    def size(self):
        """Total number of nodes in the graph.

        Returns:
            [int]: length of adjacency list.
        """
        return len(self._adjacency_list)

    def add_node(self, value):
        """Adds a new node to the graph. 

        Args:
            value: value of the node

        Returns:
            added node: node that was just added
        """
        vertex = Vertex(value)
        self._adjacency_list[vertex] = []
        return vertex

    def add_edge(self, start, end, weight=1):
        """Adds a new edge between two nodes in a graph.

        Args:
            start: node that is already in the graph that will be connected by the edge.
            end: node that is already in the graph that will be connected by the edge.
            weight (int, optional): Defaults to 1.

        Raises:
            KeyError: 'Starting Vertex not found in Graph'
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

    def get_neighbors(self, node):
        """Returns a collection of edges connected to the given node. Takes in a given node. Includes the weight of the connection in the returned collection. 
        """
        if self._adjacency_list.get(node):
            return self._adjacency_list.get(node)[0].vertex.value, self._adjacency_list.get(node)[0].weight
        else:
            return f"{node.value} has no neighbors"
       
class Vertex:
    """Vertex class
    """
    def __init__(self, value):
        self.value = value

class Edge:
    """Edge class - vertex is ending vertex
    """
    def __init__(self, vertex, weight=1):
        self.vertex = vertex
        self.weight = weight

if __name__ == "__main__":
    # g = Graph()
    # a = g.add_node('a')
    # b = g.add_node('b')
    # c = g.add_node('c')
    # d = g.add_node('d')
    # # print(d.value)
    # print('size', g.size())

    # g.add_edge(a, b)
    # g.add_edge(c, d)

    # # print(g._adjacency_list.keys())
    # # print(g._adjacency_list[a][0].vertex.value)
    # # print(g.get_nodes())

    # print(g._adjacency_list[a][0].vertex.value)
    # print(g.get_neighbors(a))
    # print(g.get_neighbors(c))
    # print(g.get_neighbors(d))
    pass
    
