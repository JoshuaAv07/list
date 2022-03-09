class Structure:
    ''' Standard Sturcture for data structures'''
    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def front(self):
        if self.front:
            return self._front.data
        else:
            raise Exception("This method does not exist")

    def back(self):
        if self.tail:
            return self._tail.data
        else:
            raise Exception("This method does not exist")

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

    