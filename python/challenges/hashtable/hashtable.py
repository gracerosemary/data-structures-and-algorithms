from .linkedlist import LinkedList 
# from linkedlist import LinkedList

class Hashtable:
    def __init__(self, size=1024):
        self.size = size
        self._buckets = [None] * size

    def _hash(self, key):
        """Takes in an arbitrary key and returns an index in the colelction. 
        """
        sum = 0

        for ch in key:
            # ord() - returns an integer representing the unicode char
            sum += ord(ch)

        primed = sum * 19
        index = primed % self.size
        return index 

    def add(self, key, value):
        """Takes both key and value. Hashes the key and adds the key and value pair to the table, handling conditions as needed.
        """
        # hash the key
        hashed_key_index = self._hash(key)

        if not self._buckets[hashed_key_index]:
            self._buckets[hashed_key_index] = LinkedList()

        self._buckets[hashed_key_index].append_node([key, value])

    def get(self, key):
        """Takes in the key and returns the value from the table
        """
        hashed_key_index = self._hash(key)
        bucket = self._buckets[hashed_key_index]
        current = bucket.head.value

        while current:
            if current[0] == key:
                return current[1]

    def contains(self, key):
        """Takes in the key and returns a boolean, indicating if the key exisits in the table already.
        """
        hashed_key_index = self._hash(key)
        bucket = self._buckets[hashed_key_index]
        if bucket:
            current = bucket.head.value
            while current:
                if current[0] == key:
                    return True
                current = current.next 
            return False
        return False

if __name__ == "__main__":
    # hashtable = Hashtable()
    # print('hash: ', hashtable._hash('cab'))
    # print('hash: ', hashtable._hash('bab'))
    # print('hash: ', hashtable._hash('five'))
    # print('hash: ', hashtable._hash('four'))
    # print('add: ', hashtable.add('addition', 54))
    # print('add: ', hashtable.add('five', 5))
    # print('add: ', hashtable.add('four', 4))
    # hashtable.contains('addition')
    # hashtable.contains('five')
    # print(hashtable.contains('four'))
    # print(hashtable.get('addition'))
    pass

