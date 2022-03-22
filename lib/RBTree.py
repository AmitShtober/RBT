from Node import Node


class RBTree(object):

    def __init__(self, data):
        self.root = Node(data, None)
