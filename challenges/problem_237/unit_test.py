import unittest

from challenges.problem_237.Node import Node
from challenges.problem_237.solution import is_symmetric


class SymmetricTree(unittest.TestCase):

    def test_example(self):
        """
        Tests the given example

             4
           / | \
          3  5  3
         /       \
        9        9

        """
        a = Node("4")
        b = Node("3")
        c = Node("5")
        d = Node("3")
        e = Node("9")
        f = Node("9")

        a.set_children([b, c, d])
        b.set_children([e])
        d.set_children([f])

        self.assertTrue(is_symmetric(a))

    def test_tree1(self):
        """
        Tests a symmetric tree

                1
          /     |     \
          2     3     2
        /   \   |   /   \
        5   6   7   6   5

        """
        a = Node("1")
        b = Node("2")
        c = Node("3")
        d = Node("2")
        e = Node("5")
        f = Node("6")
        g = Node("7")
        h = Node("6")
        i = Node("5")

        a.set_children([b, c, d])
        b.set_children([e, f])
        c.set_children([g])
        d.set_children([h, i])

        self.assertTrue(is_symmetric(a))
