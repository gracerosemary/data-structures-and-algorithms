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

    def append_node(self, value):
        new_node = Node(value, next=None)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insert_before(self, value, newVal):
        current_node = self.head
        if current_node.next is None:
            return "No Node Available"
        ll = LinkedList(current_node)
        if ll.includes(value) is False:
            return "Value does not exist!"
        while current_node.next is True:
            if current_node.next.value == value:
                current_node.next = Node(newVal, current_node.next)
            else:
                current_node = current_node.next
            

        

if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    # print(new_linked)

    new_linked1 = LinkedList(new_node)
    # print(new_linked1.head.value) # to see the value of 1

    # test insert method
    new_linked2 = LinkedList(new_node)
    new_linked2.insert(2) 
    new_linked2.insert(3) 
    new_linked2.insert(4) 
    print(new_linked2.includes(3))
    print(new_linked2.insert_before(3, 10))
    print(new_linked2) # to see the value of inserted value 2

    # # test includes
    # new_linked1 = LinkedList(new_node)
    # new_linked1.insert(2) 
    # # print(new_linked1.includes(2))
    # # print(new_linked1.includes(5))
    # print(new_linked1.head.value) # to see if it includes values (boolean)

    # new_linked2 = LinkedList(new_node)
    # print(new_linked2.insert_before(1, 10))
    # print(new_linked2) 
