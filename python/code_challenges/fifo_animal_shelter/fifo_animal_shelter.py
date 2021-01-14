class InvalidOperationError(BaseException):
    pass

class Node():
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class Cat(): 
    # def __init__(self, type):
	#     self.type = "cat"
    type = "cat"

class Dog():
    # def __init__(self, type): 
	#     self.type = "dog"
    type = "dog"

class AnimalShelter():
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, animal):
        """Adds animal to the shelter (either cat or dog)
        """
        for a in [Cat, Dog]:
        # for a in animal:
            # print(a.type) # output: cat / dog
            if a.type == "cat" or a.type == "dog":
            # if a == "cat" or "dog":
                node = Node(animal)
                if self.is_empty():
                    self.front = node
                    self.rear = node
                self.rear.next = node
                self.rear = node 
            else:
                raise InvalidOperationError("Please choose cat or dog")

    def dequeue(self, pref=None):
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
        if self.front is None:
            return True
        else:
            return False

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue("cat")
    shelter.enqueue("dog")
    shelter.enqueue("panda")
    print(shelter.front.value)
    print(shelter.front.next.value)
    print(shelter.front.next.next.value)
    print(shelter.front.next.next.next.value)
    
    # pass
