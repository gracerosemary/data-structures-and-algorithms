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
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        if self.top:
            node = self.top
            self.top = self.top.next
            node.next = None
            return node.value

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.top.value

class Queue():
    def __init__(self, front = None):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.rear = node
        self.rear.next = node
        self.rear = node 

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        temp = self.front
        self.front = self.front.next
        temp.next = None
        return temp.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        else:
            return self.front.value

    def is_empty(self):
        # return self.front == None
        if self.front is None:
            return True
        else:
            return False

if __name__ == "__main__":
    # new_node = Node("apple")
    # stack = Stack(new_node)
    # print(stack)
    pass
