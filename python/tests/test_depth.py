from challenges.depth_first.depth_first import Graph

def test_one_node():
    g = Graph()
    a = g.add_node('a')
    actual = g.depth_first(a)
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
    actual = g.depth_first(a)
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
    actual = g.depth_first(a)
    expected = ['a', 'b', 'c', 'd']
    assert actual == expected

def test_long():
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

    actual = graph.depth_first(a)
    expected = ['a', 'b', 'c', 'g', 'd', 'e', 'h', 'f']
    assert actual == expected