from node import BstNode as Node

class BinarySearchTree:

    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, data):
        node = Node(data)
        if self._root:
            current = self._root
            while current:
                if node.data > current.data:
                    if current.right:
                        current = current.right
                    else:
                        current.right = node
                        self._size+=1
                        return current.right.data
                else:
                    if current.left:
                        current = current.left
                    else:
                        current.left = node
                        self._size+=1
                        return current.left.data
        else:
            self._root = node
            self._size+=1
            return self._root.data
            

    def inorder(self, current):
        if current:
            self.inorder(current.left)
            print(current.data, end=' ')
            self.inorder(current.right)

    def preorder(self, current):
        if current:
            print(current.data, end=' ')
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self, current):
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data, end=' ')


    def root(self):
        if self._root:
            return self._root
        else:
            return None

    def size(self):
        return self._size

    def min(self, current):
        ''' The leaf with the minimum value '''
        while current:
            current = current.left
        return current  

    def max(self, current):
        ''' The leaf with the maximum value '''
        while current:
            current = current.right
        return current   