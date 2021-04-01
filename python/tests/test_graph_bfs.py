from challenges.breadth_first.breadth_first import Graph, Queue

def test_one_node():
    g = Graph()
    a = g.add_node('a')
    actual = g.breadth_first(a)
    expected = ['a']
    assert actual == expected 

def test_multiple():
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
    actual = g.breadth_first(a)
    expected = ['a', 'b', 'c', 'd', 'e']
    assert actual == expected 

def test_island():
    g = Graph()
    a = g.add_node('a')
    b = g.add_node('b')
    c = g.add_node('c')
    d = g.add_node('d')
    island = g.add_node('e')
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(c, d)
    actual = g.breadth_first(a)
    expected = ['a', 'b', 'c', 'd']
    assert actual == expected