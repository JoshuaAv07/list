from node import BstNode as Node

class BinarySearchTree:
    #initial state of the bst
    def __init__(self):
        self._root = None
        self._size = 0

    def insert(self, data):
        node = Node(data) #generates a new node to be added
        if self._root: #if there is something in the root it searches to where it is supossed to go
            current = self._root #declares the current root
            while current:
                if node.data > current.data: #if the data of the new node is greater than current it goes to the right root
                    if current.right: #if current is equals to right it changes current to the right position
                        current = current.right
                    else: # if the current right is different it declares the node as the new right node and adds 1 to the size
                        current.right = node
                        self._size+=1
                        return current.right.data #returns the data of the new right root
                else: #if the data of the new node is not greater than current it goes to the left root
                    if current.left: #if current is equals to left it changes current to the left position
                        current = current.left
                    else: # if the current left is different it declares the node as the new left node and adds 1 to the size
                        current.left = node
                        self._size+=1
                        return current.left.data #returns the data of the new left root
        else: #if it is empty it only inserts a new node and adds one to the size value an returns the data of the new root
            self._root = node
            self._size+=1
            return self._root.data
            

    def inorder(self, current): #this order shows all numbers from the lower to the highest (including the main root)
        if current:
            self.inorder(current.left)
            print(current.data, end=' ')
            self.inorder(current.right)

    def preorder(self, current): #this order shows the main root number an the the rest numbers from the lower to the highest
        if current:
            print(current.data, end=' ')
            self.preorder(current.left)
            self.preorder(current.right)

    def postorder(self, current): #this order first shows the numbers from the lower to the highest and at the end goes the main root
        if current:
            self.postorder(current.left)
            self.postorder(current.right)
            print(current.data, end=' ')

    #root function that returns if it exists and if not exists returns none
    def root(self):
        if self._root:
            return self._root
        else:
            return None

    def size(self): #size counter for the number of values within the BST
        return self._size

    def min(self, current):
        # The leaf with the minimum value
        while current:
            current = current.left
        return current  

    def max(self, current):
        # The leaf with the maximum value
        while current:
            current = current.right
        return current

    def delete(self, current, data):

        if current is None:
            return current

        if data < current.data:
            current.left = self.delete(current.left, data)
        elif data > current.data:
            current.right = self.delete(current.right, data)
        else:

            if current.left is None:
                temp = current.right
                current = None
                return temp

            elif current.right is None:
                temp = current.left
                current = None
                return temp
            
            temp = self.min(current.right)

            current.data = temp.data

            current.right = self.delete(current.right, temp.data)

        return current