from lib.Node import Node


class RBTree(object):

    def __init__(self, data):
        self.root = Node(data, None)

    def AddNode(self, value):
        from lib.RBT import RBInsert
        RBInsert(self, Node(value, None))
        return self

    def GetPrint(self, arr):
        self.root.GetPrint(arr)

    def Print(self):
        self.root.Print()

    def Search(self, value):
        from lib.RBT import RBTSearch
        return RBTSearch(self, value)

    def IsValid(self):
        from lib.RBT import RBTValid
        return RBTValid(self)
