class QueueNode():
    '''A node for a queue structure'''
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Structure:
    ''' Standard Sturcture for data structures '''

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

class Queue(Structure):

    def __init__(self):
        super().__init__()

    def push_back(self, data):
        '''Inserts a new element at the endo fo the queue'''
        node = QueueNode(data)

        if self._tail == None:
            self._front = node
            self._tail = node
        
        else:
            self._tail.next = node
            self._tail = node    
        
        self._size += 1

    def pop(self):
        current = self._front
        if current.next == None:
            self._front = None
            self._tail = None
        else:
            self._front = current.next
            current.next = None
        self._size -= 1

    def search(self, data):
        current = self._front

        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        return False

def dimension():
    n = int(input())
    my_queue = Queue()
    
    for _ in range (0, n):
        op = int(input())

        if op == 1:
            dim = input() 
            on = 0
            for d in my_queue.iter():
                if dim == d:
                    print("LA DIMENSION YA A SIDO AGREGADA")
                    on += 1
                    break
            if on == 0:
                print(my_queue.push_back(dim))
        elif op == 2:
            if my_queue.empty():
                print("-1")
            else:
                my_queue.pop() 
                print(f"VIAJANDO A {my_queue.front()}")
        elif op == 3:
            if my_queue.empty():
                print("-1")
            else: 
                print(my_queue.front())
        elif op == 4:
            if my_queue.empty():
                print("-1")
            else: 
                print(my_queue.back())
        elif op == 5:
            if my_queue.empty():
                print("-1")
            else:
                for dim in my_queue.iter():
                    print(dim)
    
if __name__ == '__main__':
   dimension() 