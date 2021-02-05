class Node:
    """Node Class
    """
    def __init__(self, value, left = None, right = None):
        """Instantiate Node class 

        Args:
            value (str|int, optional): Value of the node.
            left (str|int, optional): Left of node. Defaults to None.
            right (str|int, optional): Right of node. Defaults to None.
        """
        self.value = value
        self.left = left
        self.right = right
        self.next = None

class Queue():
    def __init__(self, front = None):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node 

    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp.value

    def peek(self):
        if not self.is_empty():
            return self.front.value

    def is_empty(self):
        if self.front is None:
            return True
        else:
            return False

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

    def findMaximumValue(self):
        """Find the max value in the tree

        Returns:
            int: max value
        """
        maximum = 0
        def traverse(root):
            nonlocal maximum
            if root.value > maximum:
                maximum = root.value
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(self.root)
        return maximum

    def breadth_first(self):
        final_list = []
        queue = Queue()
        queue.enqueue(self.root)
        while not queue.is_empty():
            current = queue.dequeue()
            final_list.append(current.value)
            if current.left:
                queue.enqueue(current.left)
            if current.right:
                queue.enqueue(current.right)
        return final_list

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
            if root.value > value:
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

if __name__ == "__main__":
    # b = Node("B")
    # c = Node("C")
    # d = Node("D")
    # e = Node("E")
    # f = Node("F")

    tree = BinaryTree(Node(10))
    b = Node(11)
    c = Node(2)
    d = Node(100)
    tree.root.left = b
    tree.root.right = c
    tree.root.left.left = d
    print(tree.breadth_first())

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


    # pass
