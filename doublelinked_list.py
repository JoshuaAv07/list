from node import DoubleLinkedListNode as Node
from structure import Structure

class DoubleLinkedList(Structure):
    ''' Class that define a doubly linked list '''

    def __init__(self):
        super().__init__()

    def append(self, data):
        new_node = Node(data)

        if self._tail == None:
            self._front = new_node
            self._tail = new_node
        else: 
            self._tail.next = new_node
            new_node.prev = self._tail
            self._tail = new_node
        
        self._size+=1

    def reverse(self):
        current = self._tail
        while current:
            data = current.data
            current = current.prev
            yield data

    def delete(self,data):
        current = self._front
        __next = self._front
        __prev = self._front

        while current:
            if current.data == data:
                if current == self._tail:
                    __prev = current.prev
                    current.prev = None
                    __prev.next = None
                    self._tail = __prev
                else:
                    __next = current.next
                    __prev = current.prev
                    current.next = None
                    current.prev = None

                    __prev.next = __next
                    __next.prev = __prev

                self._size-=1
                return True
            else: 
                current = current.next

        return False

    def insert(self, data, next_to):
        current = self.search(next_to)
        
        if current:
            new_node = Node(data)

            if current == self._tail:
                current.next = new_node
            else:
                new_node.next = current.next
                current.next = new_node

            self._size += 1
        else:
            raise ValueError("Positional element is not in the list")

    def insert2(self, data, next_to, next):
        current = self.search(next_to)
        
        if current:
            new_node = Node(data)

            if current == self._tail:
                current.next = new_node
            else:
                new_node.next = current.next
                current.next = new_node
            

            self._size += 1

        else:
            raise ValueError("Positional element is not in the list")

    def search(self,data):
        current = self._front

        while current:
            if current.data == data:
                return current
            else:
                current = current.next

        return False

    def searchR(self, data):
        current = self._tail

        while current:
            if current.data == data:
                return current
            else:
                current = current.prev
