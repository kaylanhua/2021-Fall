#################
#               #
# Problem Set 0 #
#               #
#################



#
# Setup
#

class BinaryTree:
    # left : BinaryTree
    # right : BinaryTree
    # key : string
    # temp : int
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.temp = None



#
# Problem 1
#

# Sets the temp of each node in the tree T
# ... to the size of that subtree
def calculate_size(T):
    # Set the temp for each node in the tree
    # The return value is up to you
    
    # Your code goes here
    if not T.left and not T.right:
        T.temp = 1
        return 1
        
    else:
        temp = 1
        if T.left:
            temp += calculate_size(T.left)
        if T.right:
            temp += calculate_size(T.right)
        T.temp = temp
        return temp


#
# Problem 3
#

# Outputs a subtree subT of T of size in the interval [L,U] 
# ... and removes subT from T by replacing the pointer 
# ... to subT in its parent with `None`
def FindSubtree(T, L, U): 
    # Instructions:
    # Implement your Part 2 proof in O(n)-time
    # The return value is a subtree that meets the constraints

    if not T or (not T.left and not T.right):
        return None

    if not T.temp: 
        calculate_size(T)

    if T.left:
        if T.left.temp <= U and T.left.temp >= L:
            temp = T.left
            T.left = None
            return temp
        else:
            return FindSubtree(T.left, L, U)
    else:
        if T.right.temp <= U and T.right.temp >= L:
            temp = T.right
            T.right = None
            return temp
        else:
            return FindSubtree(T.right, L, U)