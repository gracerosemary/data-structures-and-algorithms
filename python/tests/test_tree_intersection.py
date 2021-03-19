import pytest
from challenges.tree_intersection.tree_intersection import tree_intersection, BinaryTree, Node

def test_instanciate_empty_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected

def test_find_one_common():
    bt = BinaryTree(Node(5))
    bt.root.left = Node(3)
    bt.root.right = Node(6)

    bt2 = BinaryTree(Node(4))
    bt2.root.left = Node(3)
    bt2.root.right = Node(7)

    actual = tree_intersection(bt, bt2)
    expected = [3]
    assert actual == expected 

def test_find_two_common():
    bt = BinaryTree(Node(5))
    bt.root.left = Node(3)
    bt.root.right = Node(6)

    bt2 = BinaryTree(Node(4))
    bt2.root.left = Node(3)
    bt2.root.right = Node(5)

    actual = tree_intersection(bt, bt2)
    expected = [3, 5]
    assert actual == expected 