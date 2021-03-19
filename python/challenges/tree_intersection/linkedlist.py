class Node:
    """Node Class
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """Linked List Class
    """
    def __init__(self, head=None):
        self.head = None

        
    def __str__(self):
        current = self.head
        string_values = ""
        while current:
            string_values += f"{{{current.value}}}"
            current = current.next
        return string_values

    def append_node(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def display(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return values

    
if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    new_linked1 = LinkedList(new_node)

    # test 
    new_linked2 = LinkedList(new_node)
    new_linked2.append_node(5) 
    new_linked2.append_node(3) 
    new_linked2.append_node(9) 
    new_linked2.append_node(7) 
    # print(new_linked2.kthFromEnd(5))
    # print(new_linked2)  
    # print(new_linked2.evens(new_linked1))

    pass
