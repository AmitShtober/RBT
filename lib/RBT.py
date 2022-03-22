from Node import Node
from RBTree import RBTree


def LeftRotate(T: RBTree, x: Node):
    if x.right is None:
        raise Exception("LeftRotate: x.right should not be None!")

    y = x.right
    # Turn y's left sub-tree into x's right sub-tree
    x.right = y.left
    if y.left is not None:
        y.left.parent = x
    # y's new parent was x's parent
    y.parent = x.parent

    # Set the parent to point to y instead of x
    # First see whether we're at the root
    if x.parent is None:
        T.root = y
    else:
        if x == x.parent.left:
            # x was on the left of its parent
            x.parent.left = y
        else:
            # x must have been on the right
            x.parent.right = y
    y.left = x
    x.parent = y


def RightRotate(T: RBTree, x: Node):
    if x.left is None:
        raise Exception("RightRotate: x.left should not be None!")

    y = x.left
    # Turn y's left sub-tree into x's right sub-tree
    x.left = y.right
    if y.right is not None:
        y.left.parent = x
    # y's new parent was x's parent
    y.parent = x.parent

    # Set the parent to point to y instead of x
    # First see whether we're at the root
    if x.parent is None:
        T.root = y
    else:
        if x == x.parent.left:
            # x was on the left of its parent
            x.parent.left = y
        else:
            # x must have been on the right
            x.parent.right = y
    y.right = x
    x.parent = y
