from typing_extensions import Self
from lib.Node import Node


class RBTree(object):

    def __init__(self, data):
        self.root = Node(data, None)

    def AddNode(self, value) -> Self:
        """
            Add a new node to the tree with the given value
        """
        from lib.RBT import RBInsert
        RBInsert(self, Node(value, None))
        return self

    def GetPrint(self, arr) -> None:
        """
            Flatten the tree into arr (Inorder traversal (Left -> Root -> Right)
        """
        self.root.GetPrint(arr)

    def Print(self) -> None:
        """
            Print the tree (Inorder traversal (Left -> Root -> Right)
        """
        self.root.Print()

    def Search(self, value) -> bool:
        """
            Return True if value is in the tree, False otherwise
        """
        from lib.RBT import RBTSearch
        return RBTSearch(self, value)

    def IsValid(self) -> bool:
        """
            Return True if the tree is Red-Black valid, False otherwise
        """
        from lib.RBT import RBTValid
        return RBTValid(self)
