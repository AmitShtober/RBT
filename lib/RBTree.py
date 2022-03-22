from lib.Node import Node


class RBTree(object):

    def __init__(self, data):
        self.root = Node(data, None)

    def AddNode(self, value):
        RBInsert(self, value)

    def GetPrint(self, arr):
        self.root.GetPrint(arr)

    def Print(self):
        self.root.Print()
