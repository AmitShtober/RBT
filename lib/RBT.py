from lib.Node import Node, NodeColor
from lib.RBTree import RBTree


def RBInsert(T: RBTree, x: Node):
    # Insert in the tree in the usual way (BT)
    __Insert(T, x)

    # when you only have root in the tree
    if x.parent.parent is None and x.color == NodeColor.RED:
        x.color = NodeColor.BLACK
        return

    # let's restore RB properties to our tree
    x.color = NodeColor.RED
    while (x is not T.root) and (x.parent.color == NodeColor.RED):
        if x.parent == x.parent.parent.left:
            # If x's parent is a left, y is x's right 'uncle'
            y = x.parent.parent.right
            if y.color == NodeColor.RED:
                # case 1 - change the colours
                x.parent.color = NodeColor.BLACK
                y.color = NodeColor.BLACK
                x.parent.parent.color = NodeColor.RED
                # Move x up the tree
                x = x.parent.parent
            else:
                # y is a black node
                if x == x.parent.right:
                    # and x is to the right
                    # case 2 - move x up and rotate
                    x = x.parent
                    __LeftRotate(T, x)
                x.parent.color = NodeColor.BLACK
                x.parent.parent.color = NodeColor.RED
                __RightRotate(T, x.parent.parent)
        else:
            if x.parent == x.parent.parent.right:
                # If x's parent is a right, y is x's left 'uncle'
                y = x.parent.parent.left
                if y.color == NodeColor.RED:
                    # case 1 - change the colours
                    x.parent.color = NodeColor.BLACK
                    y.color = NodeColor.BLACK
                    x.parent.parent.color = NodeColor.RED
                    # Move x up the tree
                    x = x.parent.parent
                else:
                    # y is a black node
                    if x == x.parent.left:
                        # and x is to the right
                        # case 2 - move x up and rotate
                        x = x.parent
                        __RightRotate(T, x)
                    x.parent.color = NodeColor.BLACK
                    x.parent.parent.color = NodeColor.RED
                    __LeftRotate(T, x.parent.parent)

    T.root.color = NodeColor.BLACK


def RBTSearch(T: RBTree, value):
    return __Search(T.root, value)


def __Search(node: Node, value):
    if node is None:
        return False
    if node.value == value:
        return True
    if node.value < value:
        return __Search(node.right, value)
    else:
        return __Search(node.left, value)


def __Insert(T: RBTree, x):
    if T is None or T.root is None:
        raise Exception("T is not Valid!")
    __NodeInsert(T.root, x)


# TODO: what should I do if it's equal?
def __NodeInsert(node: Node, x):
    if x.value < node.value:
        if node.left is None:
            node.left = x
            x.parent = node
        else:
            __NodeInsert(node.left, x)
    elif x.value > node.value:
        if node.right is None:
            node.right = x
            x.parent = node
        else:
            __NodeInsert(node.right, x)


def __LeftRotate(T: RBTree, x: Node):
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


def __RightRotate(T: RBTree, x: Node):
    if x.left is None:
        raise Exception("RightRotate: x.left should not be None!")

    y = x.left
    # Turn y's left sub-tree into x's right sub-tree
    x.left = y.right
    if y.right is not None:
        y.right.parent = x
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


def RBTValid(T: RBTree):
    return __InnerRBTValid(T.root)


def __InnerRBTValid(node: Node):
    black_path_from_top = []

    try:
        __DFS(node, 0, black_path_from_top)
    except:
        return -1

    return black_path_from_top[0]


def __DFS(node: Node, black_path: int, black_path_from_top):
    if node.color == NodeColor.RED:
        if node.left is not None and node.left.color != NodeColor.BLACK:
            raise Exception("bad RBT")
        if node.right is not None and node.right.color != NodeColor.BLACK:
            raise Exception("bad RBT")

    current_black_path = black_path
    if node.color == NodeColor.BLACK:
        current_black_path += 1

    if node.left is None and node.right is None:
        if len(black_path_from_top) == 0:
            black_path_from_top.append(current_black_path)
        elif black_path_from_top[0] != current_black_path:
            raise Exception("bad RBT")

    if node.left is not None:
        __DFS(node.left, current_black_path, black_path_from_top)
    if node.right is not None:
        __DFS(node.right, current_black_path, black_path_from_top)
