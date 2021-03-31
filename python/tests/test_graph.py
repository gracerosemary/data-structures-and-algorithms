import pytest
from challenges.graph.graph import Graph, Vertex

# An empty graph properly returns null
def test_empty_graph():
    g = Graph()
    actual = g._adjacency_list
    expected = {}
    assert actual == expected

# Node can be successfully added to the graph
def test_add_vertex_pass():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'a'
    assert actual == expected 

def test_add_vertex_fail():
    vertex = Vertex('a')
    actual = vertex.value
    expected = 'A'
    assert actual != expected 

# An edge can be successfully added to the graph
def test_add_edge_pass():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    g.add_edge(a, b)
    assert True

# A graph with only one node and edge can be properly returned
def test_add_edge_fail():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    with pytest.raises(KeyError):
        g.add_edge(a, 'b')

# A collection of all nodes can be properly retrieved from the graph
def test_get_nodes_pass():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    actual = g.get_nodes()
    expected = ['a', 'b', 'c']
    assert actual == expected 

def test_get_nodes_fail():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    actual = g.get_nodes()
    expected = ['a', 'b', 'c']
    assert actual != expected 

# All appropriate neighbors can be retrieved from the graph
def test_get_neighbors_and_weight_pass():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    g.add_edge(a, b)
    actual = g.get_neighbors(a)
    expected = ('b', 1)
    assert actual == expected

def test_get_neighbors_and_weight_fail():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    g.add_edge(a, b)
    actual = g.get_neighbors(b)
    expected = ('a', 1)
    assert actual != expected

# The proper size is returned, representing the number of nodes in the graph
def test_size_pass():
    g = Graph()
    a = g.add_node('a')
    actual = g.size()
    expected = 1
    assert actual == expected 

def test_size_fail():
    g = Graph()
    a = g.add_node('a')
    actual = g.size()
    expected = 2
    assert actual != expected 
    
