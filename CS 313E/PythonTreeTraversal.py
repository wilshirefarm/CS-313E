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
      inorder(getLeftChild(tree))
      print(getRootVal(tree))
      inorder(getRightChild(tree))

def postorder(tree):
   if tree != []:
      postorder(getLeftChild(tree))
      postorder(getRightChild(tree))
      print(getRootVal(tree))

def main():
   
   myTree = BinaryTree(3)
   insertLeft(myTree,4)
   insertLeft(myTree,5)
   insertRight(myTree,6)
   insertRight(myTree,7)
   lsub = getLeftChild(myTree)
   rsub = getRightChild(myTree)
   insertRight(lsub,8)
   insertLeft(rsub,9)

   # print traversals
   print("inorder:")	# 4 5 8 3 9 7 6
   inorder(myTree)
   print("preorder:")	# 3 5 4 8 7 9 6
   preorder(myTree)
   print("postorder:")	# 4 8 5 9 6 7 3
   postorder(myTree)

main()




