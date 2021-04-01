from challenges.get_edge.get_edge import Graph

def test_false():
    g = Graph()
    a = g.add_node('Seattle')
    b = g.add_node('Tacoma')
    g.add_edge(a, b)
    actual = g.get_edge([b, a])
    expected = False, 0
    assert actual == expected

def test_true_one_edge():
    g = Graph()
    a = g.add_node('Seattle')
    b = g.add_node('Tacoma')
    g.add_edge(a, b)
    actual = g.get_edge([a, b])
    expected = True, 1
    assert actual == expected

def test_true_two_edges():
    g = Graph()
    a = g.add_node('Seattle')
    b = g.add_node('Tacoma')
    c = g.add_node('Portland')
    g.add_edge(a, b)
    g.add_edge(a, c)
    actual = g.get_edge([a, b, c])
    expected = True, 2
    assert actual == expected