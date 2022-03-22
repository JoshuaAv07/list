class Node:
    ''' Simple node for linked list '''

    def __init__(self, data, prev = None):
        self.data = data
        self.prev = prev

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

class Stack(Structure):
    ''' Class that describes a Stack '''

    def __init__(self):
        self._top = None
        self._size = 0

    def top(self):
        if self._top:
            return self._top.data
        else:
            return None

    def clear(self):
        self._top = None
        self._size = 0

    def iter(self):
        current = self._top
        while current:
            data = current.data
            current = current.prev
            yield data

    def push(self, data):
        node = Node(data)

        if self._top == None:
            self._top = node
        else:
            node.prev = self._top
            self._top = node

        self._size+=1

    def pop(self):
        top = self._top
        new_node = self._top.prev
        self._top = new_node
        self._size-=1
        
        return top.data

def if_its_correct(parentesis):
    my_stack = Stack()

    arr = []

    for element in parentesis:
        arr.append(element)

    if len(arr)%2 == 0:
        for parentesis in arr:
            if parentesis == '(' or parentesis == '[' or parentesis == '{':
                my_stack.push(parentesis)
            else:
                element = my_stack.top()
                if element == '(':
                    if parentesis == ')':
                        my_stack.pop()
                    else:
                        return False
                elif element == '[':
                    if parentesis == ']':
                        my_stack.pop()
                    else:
                        return False
                elif element == '{':
                    if parentesis == '}':
                        my_stack.pop()
                    else:
                        return False
                else:
                    return False
        
        return my_stack.empty()  
    else:
        return False

if __name__ == '__main__':
    parentesis = input()
    print(if_its_correct(parentesis))
