from Node import Node
from RBTree import RBTree
from enum import Enum


class NodeColor(Enum):
    BLACK = 0
    RED = 1

class Node(object):

    def __init__(self, data, parent) -> None:
        self.left = None
        self.right = None
        self.color = None
        self.parent = parent
        self.value = data

    # Inorder traversal (Left -> Root -> Right)
    def Print(self):
        if self is None:
            return
        self.left.Print()
        print(self.value)
        self.right.Print()
