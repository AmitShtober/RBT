import unittest

from lib.Node import NodeColor
from lib.RBTree import RBTree


class RBT_Tests(unittest.TestCase):

    def test_init_rbt_with_only_root(self):
        tree = RBTree(4)
        arr = []
        tree.GetPrint(arr)
        self.assertEqual(arr, [(4, NodeColor.RED)])


if __name__ == '__main__':
    unittest.main()
