class Structure:
    ''' Standard Sturcture for data structures'''
    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def front(self):
        if self._front == None:
            return None
        else:
            return self._front.data

    def back(self):
        if self._tail == None:
            return None
        else:
            return self._tail.data

    def empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def clear(self):
        self._front = None
        self._tail = None
        self._size = 0

    def iter(self):
        current = self._front

        while current:
            data = current.data
            current = current.next
            yield data
    