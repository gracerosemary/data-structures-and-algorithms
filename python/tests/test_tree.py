import pytest
from challenges.tree.tree import Node, BinaryTree, BinarySearchTree

# instantiate an empty tree
def test_instanciate_empty_tree():
    tree = BinaryTree()
    actual = tree.root
    expected = None
    assert actual == expected

# instantiate a tree with a single root node
def test_instantiate_single_root_contains():
    bstree = BinarySearchTree(Node("A"))
    actual = bstree.contains("A")
    expected = True
    assert actual == expected 

def test_instantiate_single_root_add():
    bstree = BinarySearchTree()
    bstree.add("A")
    actual = bstree.contains("A")
    expected = True
    assert actual == expected 

# add a left child and right child to a single root node
def test_add_left_child_to_single():
    bstree = BinarySearchTree(Node(5))
    bstree.add(4)
    actual = bstree.root.left.value
    expected = 4
    assert actual == expected 

def test_add_right_child_to_single():
    bstree = BinarySearchTree(Node(5))
    bstree.add(6)
    actual = bstree.root.right.value
    expected = 6
    assert actual == expected 

# return a collection from a preorder traversal
def test_preoder_one():
    bstree = BinarySearchTree()
    bstree.add(1)
    actual = bstree.preOrder()
    expected = [1]
    assert actual == expected 

def test_preoder_mult():
    bstree = BinarySearchTree()
    bstree.add(1)
    bstree.add(2)
    bstree.add(3)
    actual = bstree.preOrder()
    expected = [1, 2, 3]
    assert actual == expected 

# return a collection from inorder traversal
def test_inorder_one():
    bstree = BinarySearchTree()
    bstree.add(10)
    actual = bstree.inOrder()
    expected = [10]
    assert actual == expected 

def test_inorder_mult():
    bstree = BinarySearchTree()
    bstree.add(20)
    bstree.add(10)
    bstree.add(30)
    actual = bstree.inOrder()
    expected = [10, 20, 30]
    assert actual == expected 

# return a collection frmo a postorder traversal
def test_postorder_one():
    bstree = BinarySearchTree()
    bstree.add(100)
    actual = bstree.postOrder()
    expected = [100]
    assert actual == expected 

def test_postorder_mult():
    bstree = BinarySearchTree()
    bstree.add(200)
    bstree.add(100)
    bstree.add(300)
    actual = bstree.postOrder()
    expected = [100, 300, 200]
    assert actual == expected 