from node import QueueNode as Node
from structure import Structure


class Queue(Structure):

    def __init__(self):
        super().__init__()

    def push_back(self, data):
        ''' Inserts a new element at the end of the queue '''
        new_node = Node(data)

        if self._tail == None:
            self._front = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def pop(self):
        ''' Deleted the first element in the queue '''
        current = self._front
        if current.next == None:
            self._front = None
            self._tail = None
        else:
            self._front = current.next
            current.next = None

        self._size-= 1 