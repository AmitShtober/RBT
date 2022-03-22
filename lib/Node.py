from enum import Enum


class NodeColor(Enum):
    BLACK = 0
    RED = 1


class Node(object):

    def __init__(self, data, parent) -> None:
        self.left = None
        self.right = None
        self.color = NodeColor.RED
        self.parent = parent
        self.value = data

    # Inorder traversal (Left -> Root -> Right)
    def GetPrint(self, arr):
        if self.left is not None: self.left.GetPrint(arr)
        arr.append((self.value,self.color))
        if self.right is not None: self.right.GetPrint(arr)

    # Inorder traversal (Left -> Root -> Right)
    def Print(self):
        if self.left is not None: self.left.Print()
        print((self.value,self.color))
        if self.right is not None: self.right.Print()
