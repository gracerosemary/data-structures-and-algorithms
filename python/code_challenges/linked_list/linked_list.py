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
        """Adds a new node with the given value to the end of the list

        Args:
            value (int): value of new node
        """
        new_node = Node(value, next=None)
        if self.head is not None:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insertBefore(self, value, newVal):
        """Adds a new node with the given newVal immediately before the first value node

        Args:
            value (int): value of the node after the new node
            newVal (int): value of the new node

        Returns:
            list: linked list with new node inserted
        """
        current_node = self.head
        ll = LinkedList(current_node)
        if current_node is None:
            return "No Node Available"
        if ll.includes(value) is False:
            return "Value does not exist!"
        if current_node.value is value:
            ll.insert(newVal)
            return None
        while current_node is not None:
            if current_node.next.value is value:
                current_node.next = Node(newVal, current_node.next)
                return None
            current_node = current_node.next

    def insertAfter(self, value, newVal):
        """Adds a new node with the given newVal immediately after the first value node.

        Args:
            value (int): value of the node preceeding the new node
            newVal (int): value of the new node

        Returns:
            list: linked list with new node inserted
        """
        current_node = self.head
        ll = LinkedList(current_node)
        if ll.includes(value) is False:
            return "Value does not exist!"
        while current_node is not None:
            if current_node.value == value:
                current_node.next = Node(newVal, current_node.next) 
                return None
            current_node = current_node.next

        # # roger's solution:
        # current = self.head
        # # do i have a current?
        # while current:
        #     if current.value == value:
        #         node = Node(newVal, current_node.next)
        #         current.next = node 
        #         return
        #     current = current.next
        # return "Not in list"


    def kthFromEnd(self, k):
        """Takes a number(k) and returns the node's value that is k from the end of the list.

        Args:
            k (int): number that represents x from the end of the list

        Raises:
            ValueError: negative numbers
            IndexError: values exceeding length of the list

        Returns:
            int: node's value that is k from the end of the list
        """
        count = -1
        follower = self.head
        leader = self.head

        if k < 0:
            raise ValueError
        if k == 0:
            return self.head.value
        if self.head is not None:
            while count < k:
                if leader is None:
                    raise IndexError('Value is greater than the length of the list')
                leader = leader.next
                count += 1
        if leader is None:
            self.head = self.head.next
            if self.head is not None:
                return follower.value
        else:
            while leader is not None:
                leader = leader.next
                follower = follower.next
            return follower.value

        # # Logan's solution:
        # current = self.head
        # newList = []
        # while current:
        #     newList.append(current.value)
        #     current = current.next
        # size = len(newList)
        # if k < size:
        #     return newList[size -k -1].value
        # raise Exception()

        # # Dario's solution 1:
        # current = self.head
        # newList = []
        # while current:
        #     newList.append(current.value)
        #     current = current.next
        # if len(newList) < k:
        #     print("Index out of bounds")
        # else: 
        #     newList[-k -1]

        # # Dario's solution 2 - doesnt work when testing:
        # paces_behind = 0
        # leader = self.head
        # follower = None
        # while leader: # we have not hit None
        #     leader = leader.next # we need to move the leader forward one node to eventually get to the tail
        #     if follower: # only move the follower if it is not a None value
        #         follower = follower.next
        #     elif paces_behind == k: # once the leader has reached the paces_behind count, we can start moving the follower
        #         follower = self.head 
        #     else: # increment the paces_behind count for the iteration
        #         paces_behind += 1
        # if not follower:
        #     raise ValueError
        # return follower.value

if __name__ == "__main__":
    new_node = Node(1)
    new_linked = LinkedList()
    new_linked1 = LinkedList(new_node)

    # test 
    new_linked2 = LinkedList(new_node)
    new_linked2.insert(2) 
    new_linked2.insert(3) 
    new_linked2.insert(4) 
    new_linked2.insert(6) 
    print(new_linked2.kthFromEnd(5))
    print(new_linked2)  
