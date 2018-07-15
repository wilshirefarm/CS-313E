def BinaryTree(initdata):
   return [ initdata, [], [] ]

def getRootVal(root):
   return root[0]

def setRootVal(root, newVal):
   root[0] = newVal

def getLeftChild(root):
   return root[1]

def getRightChild(root):
   return root[2]

def insertLeft(root,newBranch):
   t = root.pop(1)                       # temporarily break the tree	
   if len(t) > 1:                        # if something already
      root.insert(1,[newBranch,t,[] ] )  # there, push it down as
   else:                                 # the new left child
      root.insert(1,[newBranch,[],[] ] )

def insertRight(root,newBranch):
   t = root.pop(2)
   if len(t) > 1:                        # if something already
      root.insert(2,[newBranch,[],t ] )  # there, push it down as
   else:                                 # the new right child
      root.insert(2,[newBranch,[],[] ] )
      
def preorder(tree):
     if tree != []:
         print(getRootVal(tree))
         preorder(getLeftChild(tree))
         preorder(getRightChild(tree))

def inorder(tree):
     if tree != []:
         preorder(getLeftChild(tree))
         print(getRootVal(tree))
         preorder(getRightChild(tree))

def postorder(tree):
     if tree != []:
         preorder(getLeftChild(tree))
         preorder(getRightChild(tree))
         print(getRootVal(tree))
