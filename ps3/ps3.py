class BinarySearchTree:
    # left: BinarySearchTree
    # right: BinarySearchTree
    # key: string
    # size: int
    def __init__(self, debugger = None):
        self.left = None
        self.right = None
        self.key = None
        self.item = None
        self._size = 1
        self.debugger = debugger

    @property
    def size(self):
         return self._size
       
     # a setter function
    @size.setter
    def size(self, a):
        debugger = self.debugger
        if debugger:
            debugger.inc_size_counter()
        self._size = a

    ####### Problem 1 #######
    '''
    Calculates the size of the tree
    returns the size at a given node
    '''
    def calculate_sizes(self, debugger = None):
        # Debugging code
        # No need to modify
        # Provides counts
        if debugger is None:
            debugger = self.debugger
        if debugger:
            debugger.inc()

        # Implementation
        self.size = 1
        if self.right is not None:
            self.size += self.right.calculate_sizes(debugger)
        if self.left is not None:
            self.size += self.left.calculate_sizes(debugger)
        return self.size

    '''
    Select the ind-th key in the tree
    
    ind: a number between 0 and n-1 (the number of nodes/objects)
    returns BinarySearchTree/Node or None
    '''
    def select(self, ind):
        left_size = 0
        if self.left is not None:
            left_size = self.left.size
        if ind == left_size:
            return self
        if left_size > ind and self.left is not None:
            return self.left.select(ind)
        if left_size < ind and self.right is not None:
            return self.right.select(ind - left_size - 1)
        return None


    '''
    Searches for a given key
    returns a pointer to the object with target key or None (Roughgarden)
    '''
    def search(self, key):
        if self is None:
            return None
        elif self.key == key:
            return self
        elif self.key < key and self.right is not None:
            return self.right.search(key)
        elif self.left is not None:
            return self.left.search(key)
        return None
    

    '''
    Inserts a key into the tree

    key: the key for the new node; 
        ... this is NOT a BinarySearchTree/Node, the function creates one
    
    returns the original (top level) tree - allows for easy chaining in tests
    '''
    def insert(self, key):
        if self.key is None:
            self.key = key
        elif self.key > key: 
            self.size += 1
            if self.left is None:
                self.left = BinarySearchTree(self.debugger)
            self.left.insert(key)
        elif self.key < key:
            self.size += 1
            if self.right is None:
                self.right = BinarySearchTree(self.debugger)
            self.right.insert(key)
        return self

    
    ####### Problem 2 #######

    '''
    Deletes a key from the tree
    Returns the root of the tree or None if the tree has no nodes   
    '''
    def delete(self, key):
        if self is None:
            return self

        found = self.search(key)
        if not found:
            print("key does not exist")
            return self

        return self.deleteHelper(key)

    def deleteHelper(self, key):
        self.size -= 1

        if key < self.key:
            self.left = self.left.deleteHelper(key)
        elif key > self.key:
            self.right = self.right.deleteHelper(key)

        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                temp = self.left.select(self.left.size - 1)
                self.key = temp.key
                self.left = self.left.deleteHelper(temp.key)

        return self

    '''
    Performs a `direction`-rotate the `side`-child of (the root of) T (self)

    direction: "L" or "R" to indicate the rotation direction
    child_side: "L" or "R" which child of T to perform the rotate on

    Returns: the root of the tree/subtree

    Example:

    Original Graph
      10
       \
        11
          \
           12
    
    Execute: NodeFor10.rotate("L", "R") -> Outputs: NodeFor10

    Output Graph
      10
        \
        12
        /
       11 
    '''
    def rotate(self, direction, child_side):
        if child_side == "R":
            ogRight = self.right
            if direction == "L":
                newRight = self.right.right
                self.right.right = self.right.right.left
                self.right = newRight
                self.right.left = ogRight
                b = 0 if newRight.left is None else newRight.left.size
            else:
                newRight = self.right.left
                self.right.left = self.right.left.right
                self.right = newRight
                self.right.right = ogRight
                b = 0 if newRight.right is None else newRight.right.size
            a = newRight.size 
            c = ogRight.size
            self.right.size = c
            if direction == "L":
                self.right.left.size = c - a + b
            else: 
                self.right.right.size = c - a + b
            
        else:
            ogLeft = self.left
            if direction == "R":
                newLeft = self.left.left
                self.left.left = self.left.left.right
                self.left = newLeft
                self.left.right = ogLeft
                b = 0 if newLeft.right is None else newLeft.right.size
            else:
                newLeft = self.left.right
                self.left.right = self.left.right.left
                self.left = newLeft
                self.left.left = ogLeft
                b = 0 if newLeft.left is None else newLeft.left.size
            a = newLeft.size 
            c = ogLeft.size
            self.left.size = c
            if direction == "L":
                self.left.left.size = c - a + b
            else: 
                self.left.right.size = c - a + b
    
        return self

    def print_bst(self):
        if self.left is not None:
            self.left.print_bst()
        print( self.key),
        if self.right is not None:
            self.right.print_bst()
        return self

