""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBSTMnMx(root, mn, mx):
    if root is None:
        return True
    
    leftBST = root.left is None
    if not leftBST:
        if mn is not None:
            leftBST = (mn < root.left.data < root.data)
        else:
            leftBST = (root.left.data < root.data)
        
    if not leftBST:
        return False
    
    rightBST = root.right is None
    if not rightBST:
        if mx is not None:
            rightBST = (root.data < root.right.data < mx)
        else:
            rightBST = (root.data < root.right.data)
            
        
    if not rightBST:
        return False
    
    return checkBSTMnMx(root.left, mn, root.data) and checkBSTMnMx(root.right, root.data, mx)

def checkBST(root):
    if root is None:
        return True
    
    leftBST = (root.left is None) or (root.left.data < root.data)
    rightBST = (root.right is None) or (root.data < root.right.data)
    
    if not leftBST or not rightBST:
        return False
    
    return checkBSTMnMx(root.left, None, root.data) and checkBSTMnMx(root.right, root.data, None)
    