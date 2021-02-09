import pytest
from challenges.fizz_buzz_tree.fizz_buzz_tree import Node, BinaryTree

def test_fizz():
    tree = BinaryTree(Node(3))
    b = Node(6)
    c = Node(9)
    d = Node(12)
    tree.root.left = b
    tree.root.right = c
    tree.root.left.left = d
    actual = tree.fizzbuzztree()
    expected = ["Fizz", "Fizz", "Fizz", "Fizz"]
    assert actual == expected 

def test_buzz():
    tree = BinaryTree(Node(5))
    b = Node(10)
    c = Node(20)
    d = Node(25)
    tree.root.left = b
    tree.root.right = c
    tree.root.left.left = d
    actual = tree.fizzbuzztree()
    expected = ["Buzz", "Buzz", "Buzz", "Buzz"]
    assert actual == expected 

def test_fizz_buzz():
    tree = BinaryTree(Node(15))
    b = Node(30)
    tree.root.left = b
    actual = tree.fizzbuzztree()
    expected = ["FizzBuzz", "FizzBuzz"]
    assert actual == expected 

def test_string():
    tree = BinaryTree(Node(1))
    b = Node(2)
    tree.root.left = b
    actual = tree.fizzbuzztree()    
    expected = ["1", "2"]
    assert actual == expected 

def test_empty():
    tree = BinaryTree()  
    with pytest.raises(TypeError) as e:
        tree.fizzbuzztree()
    assert str(e.value) == "No nodes found"