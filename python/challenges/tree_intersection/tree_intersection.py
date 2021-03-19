from hashtable import Hashtable

class Node:
    """Node Class
    """
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
        self.next = None

class BinaryTree:
    """Binary Tree Class
    """
    def __init__(self, root = None):
        self.root = root

    def preOrder(self):
        """Root >> Left >> Right

        Returns:
            List: list of nodes in pre-order format
        """
        collection = []
        def traverse(root):
            print(root.value)
            collection.append(root.value)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return collection

def tree_intersection(tree_one, tree_two):
    tree_one = tree_one.preOrder()
    tree_two = tree_two.preOrder()
    
    # without using hashtable:
    # common = [x for x in tree_one if x in tree_two]
    # return common

    hashtable = Hashtable()
    common = []
    for x in tree_one:
        x = str(x)
        if hashtable.contains(x):
            common.append(int(x))
        else: 
            hashtable.add(x, x)
    for y in tree_two:
        y = str(y)
        if hashtable.contains(y):
            common.append(int(y))
        else:
            hashtable.add(y, y)
    return common

if __name__ == "__main__":
    # bt = BinaryTree(Node(5))
    # bt.root.left = Node(3)
    # bt.root.right = Node(6)

    # bt2 = BinaryTree(Node(4))
    # bt2.root.left = Node(3)
    # bt2.root.right = Node(5)

    # print(tree_intersection(bt, bt2))

    # print(bt.preOrder())
    pass
