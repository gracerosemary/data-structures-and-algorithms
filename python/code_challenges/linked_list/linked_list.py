class Node:
    """Node Class
    """

    def __init__(self, value, next=None):
        """Properties for the value stored and pointer to the next Node.

        Args:
            value (int): value of the node.
            next (next node, optional): reference to next Node. Defaults to None.
        """
        self.value = value
        self.next = next


class LinkedList:
    """Linked List Class
    """
    def __init__(self, head=None):
        """An empty Linked List is created upon instantiation. 

        Args:
            head (int, optional): first node. Defaults to None.
            values (int, optional): node value. Defaults to 0.
        """
        self.head = head

    def insert(self, value):
        """Insert method. Adds a new node with that value to the head of the list.

        Args:
            value (int): node value
        """
        node = Node(value)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def includes(self, value):
        """Returns a boolean result depending on whether that value exists as a Node's value somewhere in the list.

        Args:
            value (int): any value
        """
        current = self.head
        while current != None:
            if current.value == value:
                return True
            current = current.next
        return False
        
    def __str__(self):
        """Takes no arguments. Returns a string representing all the values in the Linked List.
        """
        current = self.head
        string_values = ""
        while current:
            string_values += f"{{{current.value}}}->"
            current = current.next
        string_values += "NULL"
        return string_values

