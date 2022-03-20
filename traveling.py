class Node:
    ''' Simple node for linked list '''

    def __init__(self, data):
        self.data = data

class ListNode(Node):
    ''' A Node for singly linked list'''
    def __init__(self,data,next=None):
        super().__init__(data)
        self.next = next

class QueueNode(ListNode):
    '''A node for a queue structure'''
    def __init__(self, data, next=None):
        super().__init__(data, next)

class Structure:
    ''' Standard Sturcture for data structures '''
    ''' Here  we are creating all the setters and getters with the one we are going to manipulate the structure of the nodes'''
    
    def __init__(self):
        self._front = None
        self._tail = None
        self._size = 0

    def size(self):
        return self._size

    def front(self):
        return self._front.data

    def back(self):
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

        #if the tail is None it means that the list is empty and
        #this piece of code make the first element of the list
        if self._tail == None:
            self._front = node
            self._tail = node
        #if the tail is not None it means that the list is not empty
        #and this piece of code make the last element of the list
        #so assign the tail to the new node and assign the new node and linked the previous tail
        else:
            self._tail.next = node
            self._tail = node

        self._size += 1

    def pop_front(self):
        '''Removes the first element of the queue'''
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


if __name__ == '__main__':
    my_q = Queue()
    qnt = int(input())
    data = ""
    
    while qnt != 0:
        i = int(input())
        if i == 1:
            data = input() 
            if my_q.empty() == True:
                my_q.push_back(data)
            else:
                if my_q.search(data):
                    print("ERROR LA DIMENSION YA A SIDO AGREGADA")
                else:
                    my_q.push_back(data)
            qnt-=1
        elif i == 2:
            if my_q.empty() == True:
                print("-1")
            else: 
                print(f"VIAJANDO A {my_q.front()}")
                my_q.pop_front()
            qnt-=1
        elif i == 3:
            if my_q.empty() == True:
                print("-1")
            else: 
                print(my_q.front())
            qnt-=1
        elif i == 4:
            if my_q.empty() == True:
                print("-1")
            else: 
                print(my_q.back())
            qnt-=1
        elif i == 5:
            if my_q.empty() == True:
                print("-1")
            else:
                for name in my_q.iter():
                    print(name)
            qnt-=1
        else:
            print("No existe esa instruccion.")



                
