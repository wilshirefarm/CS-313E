class BinaryTree():

    def __init__(self, initval):
        self.data = initval
        self.left = None
        self.right = None

    def getRootVal(self):
        return self.data

    def setRootVal(self, value):
        self.data = value

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def insertLeft(self, newValue):
        temp = self.getLeftChild()
        new = BinaryTree(newValue)
        self.left = new
        new.left = temp

    def insertRight(self, newValue):
        temp = self.getRightChild()
        new = BinaryTree(newvalue)
        self.right = new
        new.right = temp
