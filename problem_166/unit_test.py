import unittest

from problem_166.solution import Iterator


class IteratorTest(unittest.TestCase):

    def test_example(self):
        _input = [[1, 2], [3], [], [4, 5, 6]]
        iterator = Iterator(_input)

        expected = [1, 2, 3, 4, 5, 6]
        actual = []

        while iterator.has_next():
            actual.append(iterator.next())

        self.assertEqual(expected, actual)

    def test_exception_raised(self):
        _input = [[1, 2], [3], [], [4, 5, 6]]
        iterator = Iterator(_input)

        while iterator.has_next():
            iterator.next()

        with self.assertRaises(StopIteration):
            iterator.next()
