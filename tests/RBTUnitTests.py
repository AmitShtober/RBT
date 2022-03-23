import unittest

from lib.Node import NodeColor
from lib.RBTree import RBTree


class RBT_Tests(unittest.TestCase):

    def test_init_rbt_with_only_root(self):
        tree = RBTree(4)
        arr = []
        tree.GetPrint(arr)
        self.assertEqual(arr, [(4, NodeColor.RED)])
        self.assertGreaterEqual(tree.IsValid(), 0)

    def test_build_rbt(self):
        tree = RBTree(11)
        tree.AddNode(2).AddNode(14).AddNode(1).AddNode(7).AddNode(5).AddNode(8).AddNode(15)

        arr = []
        tree.GetPrint(arr)
        exp = [(1, NodeColor.BLACK), (2, NodeColor.RED), (5, NodeColor.RED), (7, NodeColor.BLACK), (8, NodeColor.RED),
               (11, NodeColor.BLACK), (14, NodeColor.BLACK), (15, NodeColor.RED)]
        self.assertEqual(arr, exp)
        self.assertGreaterEqual(tree.IsValid(), 0)

    def test_build_rbt2(self):
        tree = RBTree(11)
        tree.AddNode(2).AddNode(14).AddNode(1).AddNode(7).AddNode(5).AddNode(8).AddNode(4).AddNode(15)

        self.assertGreaterEqual(tree.IsValid(), 0)

    def test_add_to_rbt(self):
        tree = RBTree(11)
        tree.AddNode(2).AddNode(14).AddNode(1).AddNode(7).AddNode(5).AddNode(8).AddNode(15)

        # adding
        tree.AddNode(4)

        self.assertTrue(tree.Search(4) is True)
        self.assertGreaterEqual(tree.IsValid(), 0)


if __name__ == '__main__':
    unittest.main()
