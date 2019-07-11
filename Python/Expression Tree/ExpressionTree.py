#  File: ExpressionTree.py
#  Description: Reads in datafile with expressions, outputs expression, evaluates it, puts it in a binary tree, and outputs the values in prefix and postfix notation

class BinaryTree(object):
     
    def __init__(self, initData, parent=None):          #creates a node with a data, left, right, points back to parent
        self.data = initData
        self.left = None
        self.right = None
        self.parent = parent

    def getRootVal(self):               #returns the value of the node
        return self.data

    def setRootVal(self, data):         #sets the node's value to data
        self.data = data

    def getLeftChild(self):             #returns the left child of the node
        return self.left

    def getRightChild(self):            #returns the right child of the node
        return self.right

    def getParent(self):                #returns the parent of the node
        return self.parent
    
    def insertLeft(self, newNode):                  #creates a left child for the node
        self.left = BinaryTree(newNode, self)

    def insertRight(self, newNode):                 #creates a right child for the node
        self.right = BinaryTree(newNode, self)

    def createTree(self, expr):
        expr = expr.split()                                     #puts the expr tokens into a list
        currentNode = self                                      #sets current node to self first
        for i in expr:                                          #loop through list of tokens
            if i == "(":                                        #if token is a ( then create a left child and set the current node to that node
                currentNode.insertLeft(None)
                currentNode = currentNode.getLeftChild()
            elif i == ")":                                      #if token is a ( then set the current node to the current node's parent
                currentNode = currentNode.getParent()
            elif i in "+-*/":                                   #if token is an operator then set current node's value to the operator,
                currentNode.setRootVal(i)                       #create a right child, and set the current node to that node
                currentNode.insertRight(None)
                currentNode = currentNode.getRightChild()
            else:                                               #if token is an operand, set the node's value to operand and set the current node to that node
                currentNode.setRootVal(i)
                currentNode = currentNode.getParent()
                
    def evaluate(self):
        if self.left == None:                               #base case for left side: if leaf node, return the value (operand)
            return eval(self.getRootVal())
        else:                                               #recurse on the left side, and return the left side's data
            leftData = self.left.evaluate()

        if self.right == None:                              #base case for right side: if leaf node, return the value (operand)
            return eval(self.getRootVal())
        else:
            rightData = self.right.evaluate()               #recurse on the right side, and return the right side's data
        
        if self.getRootVal() == "+":                        #if the node's value is a + then return the left data + the right data
            return leftData + rightData
        elif self.getRootVal() == "-":                      #if the node's value is a - then return the left data - the right data
            return leftData - rightData
        elif self.getRootVal() == "*":                      #if the node's value is a * then return the left data * the right data
            return leftData * rightData
        elif self.getRootVal() == "/":                      #if the node's value is a / then return the left data / the right data
            return leftData / rightData

    def preOrder(self):
        if self.left == None:                               #base case for left side: if leaf node, left data to be returned in nothing
            leftData = ""
        else:                                               #if internal node, recurse on the left child
            leftData = self.left.preOrder()

        if self.right == None:                              #base case for right side: if leaf node, right data to be returned is nothing
            rightData = ""
        else:                                               #if internal node after left subtree is processed, recurse on the right side
            rightData = self.right.preOrder()

        return (self.data + " " + leftData + rightData)

    def postOrder(self):                                    #same as preOrder, except returns left data, right data, and then the root value
        if self.left == None:
            leftData = ""
        else:                                               #space has to be added within the recursion
            leftData = self.left.postOrder() + " "

        if self.right == None:
            rightData = ""
        else:
            rightData = self.right.postOrder() + " "        #space has to be added within the recursion

        return (leftData + rightData + self.data)

def main():

    file = open("treedata.txt", "r")                            #open the file
    expr = file.readline()                                      #read in a line
    while (expr != ""):                                         #while the line is not blank (not EOF)
        myTree = BinaryTree(None)                               #create first node
        myTree.createTree(expr)                                 #create the tree
        print("Infix expression: ", expr)                       #print out the line
        print("   Value:  ", myTree.evaluate())                 #evaluate the tree's value
        print("   Prefix expression:  ", myTree.preOrder())     #print out preOrder
        print("   Postfix expression:  ", myTree.postOrder())   #print out postOrder
        print()
        expr = file.readline()                                  #read the next line in the file

main()
