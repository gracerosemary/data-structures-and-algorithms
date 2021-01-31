class Node:
    """Node Class
    """
    def __init__(self, value = None, left = None, right = None):
        """Instantiate Node class 

        Args:
            value (str|int, optional): Value of the node. Defaults to None.
            left (str|int, optional): Left of node. Defaults to None.
            right (str|int, optional): Right of node. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    """Binary Tree Class
    """
    def __init__(self, root = None):
        """Instantiate Binary Tree class

        Args:
            root (str|int, optional): Root of the tree. Defaults to None.
        """
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

    def inOrder(self):
        """Left >> Root >> Right

        Returns:
            List: list of nodes in in-order format
        """
        collection = []
        def traverse(root):
            if root.left:
                traverse(root.left)            
            print(root.value)
            collection.append(root.value)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return collection

    def postOrder(self):
        """Left >> Right >> Root

        Returns:
            list: list of nodes in post-order format
        """
        collection = []
        def traverse(root):
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
            print(root.value)
            collection.append(root.value)
        traverse(self.root)
        return collection

class BinarySearchTree(BinaryTree):
    """Binary Search Tree Class that inherits from Binary Tree Class

    Args:
        BinaryTree (Super Class): contains preOrder, inOrder, and postOrder methods
    """
    def contains(self, value):
        """Returns True if value is in the tree, otherwise False

        Args:
            value (str|int): value specified by user

        Returns:
            Boolean: true if Tree contains value, otherwise False
        """
        if not self.root:
            return False
        root = self.root
        while root:
            if root.value == value:
                return True
            if root.value < value:
                root = root.left
            else:
                root = root.right
        return False

    def add(self, value):
        """Accepts a value and adds a new node with the specified value in the correct location

        Args:
            value (int): value of the new node
        """
        node = Node(value)
        if not self.root:
            self.root = node
            return
        root = self.root
        while root:
            if root.value > node.value:
                if root.left:
                    root = root.left
                else:
                    root.left = node
                    print(node.value)
                    return
            else:
                if root.right:
                    root = root.right
                else:
                    root.right = node
                    print(node.value)
                    return

# if __name__ == "__main__":
    # b = Node("B")
    # c = Node("C")
    # d = Node("D")
    # e = Node("E")
    # f = Node("F")

    # tree = BinaryTree(Node("A"))
    # tree.root.left = b
    # tree.root.right = c
    # b.left = d
    # b.right = e
    # c.left = f
    # print(tree.root.value)
    # print(tree.root.left.value)
    # print(tree.root.right.value)
    # print(tree.root.left.left.value)
    # tree.inOrder()
    # tree.preOrder()
    # tree.postOrder()

    # bstree = BinarySearchTree(Node("A"))
    # print(bstree.contains("B"))

    # bstree = BinarySearchTree(Node(5))
    # print(bstree.add(4))
    # print(bstree.add(6))
    # print(bstree.add(3))
    # print(bstree.contains(5))
