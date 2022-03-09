class Node:
    ''' Simple node for linked list '''

    def __init__(self, data):
        self.data = data


class ListNode(Node):
    ''' A Node for singly linked list'''

    def __init__(self,data,next=None):
        super().__init__(data)
        self.next = next
        
class StackNode(Node):
    ''' A Node for a Queue structure '''
    def __init__(self, data, prev=None):
        super().__init__(data)
        self.prev = prev

class QueueNode(ListNode):
    ''' A Node for a Queue structure '''
    def __init__(self, data, next=None):
        super().__init__(data, next)

class DoubleLinkedListNode(ListNode):
    ''' A Node for a doubly linked list '''
    def __init__(self, data, next=None, prev=None):
        super().__init__(data, next)
        self.prev = prev
