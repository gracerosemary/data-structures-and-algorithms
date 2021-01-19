class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Stack():
    def __init__(self, node = None):
        self.top = node

    def push(self, value):
        """pushes value to the top of the stack
        """
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        """Pops the top of the stack

        Raises:
            InvalidOperationError: error if stack is empty

        Returns:
            [value]: value of the popped node
        """
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        if self.top:
            node = self.top
            self.top = self.top.next
            node.next = None
            return node.value

    def is_empty(self):
        """Boolean that checks if stack is empty

        Returns:
            [Boolean]: empty returns True
        """
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        """Checks the top value of the Stack

        Raises:
            InvalidOperationError: error if empty

        Returns:
            [value]: value of the top node
        """
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

class PseudoQueue:
    def __init__(self, restack = Stack(), destack = Stack()):
        self.restack = Stack()
        self.destack = Stack()
        self.count = 0

    def __str__(self):
        """Returns a string representing values in the PseudoQueue
        """
        string_values = ""
        front = self.restack.top
        while front:
            print(front.value)
            string_values += f"->{[front.value]}"
            front = front.next
        return string_values

    def enqueue(self, value):
        """Inserts value into the PseudoQueue, using FIFO approach.

        Args:
            value (node value): value to add to queue
        """
        self.count += 1
        self.restack.push(value)

    def dequeue(self):
        """extracts a value from the PseudoQueue within FIFO approach.
        """
        while self.count > 0:
            popped = self.restack.pop()
            self.destack.push(popped)
            self.count -= 1
        return self.destack.pop()

if __name__ == "__main__":
    # q = PseudoQueue()
    # q.enqueue(20)
    # q.enqueue(15)
    # q.enqueue(10)
    # q.enqueue(5)

    # print(q)
    pass
