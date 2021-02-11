import unittest

from challenges.problem_003.solution import Node, serialize, deserialize


class TreeSerializer(unittest.TestCase):

    def test_example_1(self):
        expected_tree = None
        expected_string = '()'

        actual_string = serialize(expected_tree)
        actual_tree = deserialize(expected_string)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(repr(expected_tree), repr(actual_tree))

    def test_example_2(self):
        expected_tree = Node('root')
        expected_string = '(root()())'

        actual_string = serialize(expected_tree)
        actual_tree = deserialize(expected_string)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(repr(expected_tree), repr(actual_tree))

    def test_example_3(self):
        expected_tree = Node('root', Node('left'))
        expected_string = '(root(left()())())'

        actual_string = serialize(expected_tree)
        actual_tree = deserialize(expected_string)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(repr(expected_tree), repr(actual_tree))

    def test_example_4(self):
        expected_tree = Node('root', None, Node('right'))
        expected_string = '(root()(right()()))'

        actual_string = serialize(expected_tree)
        actual_tree = deserialize(expected_string)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(repr(expected_tree), repr(actual_tree))

    def test_example_5(self):
        expected_tree = Node('root', Node('left'), Node('right'))
        expected_string = '(root(left()())(right()()))'

        actual_string = serialize(expected_tree)
        actual_tree = deserialize(expected_string)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(repr(expected_tree), repr(actual_tree))

    def test_example_6(self):
        expected_tree = Node('root', Node('left', Node('left.left')), Node('right'))
        expected_string = '(root(left(left.left()())())(right()()))'

        actual_string = serialize(expected_tree)
        actual_tree = deserialize(expected_string)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(repr(expected_tree), repr(actual_tree))

    def test_example_8(self):
        expected_tree = Node('root', Node('left'), Node('right', None, Node('right.right')))
        expected_string = '(root(left()())(right()(right.right()())))'

        actual_string = serialize(expected_tree)
        actual_tree = deserialize(expected_string)

        self.assertEqual(expected_string, actual_string)
        self.assertEqual(repr(expected_tree), repr(actual_tree))

    def test_example_9(self):
        expected_tree = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right', Node('right.left'), Node('right.right')))
        expected_string = '(root(left(left.left()())(left.right()()))(right(right.left()())(right.right()())))'

        actual_string = serialize(expected_tree)
        actual_tree = deserialize(expected_string)
        self.assertEqual(expected_string, actual_string)
        self.assertEqual(repr(expected_tree), repr(actual_tree))
