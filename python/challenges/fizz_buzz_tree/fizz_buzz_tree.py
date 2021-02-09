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

class BinaryTree:
    """Binary Tree Class
    """
    def __init__(self, root=None):
        """Instantiate Binary Tree class

        Args:
            root (str|int, optional): Root of the tree. Defaults to None.
        """
        self.root = root  

    def change_vals(self, root=None):
        """changes the value of the node based on if it's divisible by 3, 5, or both. 

        Args:
            root (int, optional): root. Defaults to None.

        Returns:
            string: Fizz, Buzz, FizzBuzz, or string version
        """
        if root % 15 == 0:
            return "FizzBuzz"
        if root % 3 == 0:
            return "Fizz"
        if root % 5 == 0:
            return "Buzz"
        else: 
            return str(root)

    def fizzbuzztree(self, tree=None):
        """Traverses the tree and appends new values to a list

        Args:
            tree (BT, optional): Binary Tree. Defaults to None.

        Raises:
            TypeError: if tree is empty, return error message

        Returns:
            tree: list of new values
        """
        if not self.root:
            raise TypeError("No nodes found")
        else:
            tree = []
            def traverse(root):
                change_vals = self.change_vals
                node = Node(change_vals(root.value))
                tree.append(node.value)
                if root.left:
                    traverse(root.left)
                if root.right:
                    traverse(root.right)
            traverse(self.root)
            return tree
        
# if __name__ == "__main__":
#     tree = BinaryTree(Node(10))
#     b = Node(11)
#     c = Node(12)
#     d = Node(15)
#     tree.root.left = b
#     tree.root.right = c
#     tree.root.left.left = d
#     print(tree.root.value)
#     print(tree.root.left.value)
#     print(tree.root.right.value)
#     print(tree.root.left.left.value)
#     print(tree.fizzbuzztree())