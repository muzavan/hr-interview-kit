# Passed because the node height is relatively low
# Can utilize Memoization as well to speed it up

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def isIn(root, v1):
    if root is None:
        return False
    
    if root.info == v1:
        return True
    
    return isIn(root.left, v1) or isIn(root.right, v1)

def lca(root, v1, v2):
  #Enter your code here
  if root is None:
    return None

  v1Left = isIn(root.left, v1)
  v2Left = isIn(root.left, v2)
  v1Right = isIn(root.right, v1)
  v2Right = isIn(root.right, v2)
  
  if not v1Left and not v1Right and not v2Left and not v2Right:
    return None

  if v1Left and v2Right:
    return root

  if v1Right and v2Left:
    return root

  if root.info == v1 and (v2Left or v2Right):
    return root
    
  if root.info == v2 and (v1Left or v1Right):
    return root

  if v1Left and v2Left:
    return lca(root.left, v1, v2)

  return lca(root.right, v1, v2)
  

tree = BinarySearchTree()