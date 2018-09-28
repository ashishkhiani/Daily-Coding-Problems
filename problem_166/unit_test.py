import unittest

from problem_166.solution import Iterator


class IteratorTest(unittest.TestCase):

    def test_example(self):
        """Tests the given example"""
        _input = [[1, 2], [3], [], [4, 5, 6]]
        iterator = Iterator(_input)

        expected = [1, 2, 3, 4, 5, 6]
        actual = []

        while iterator.has_next():
            actual.append(iterator.next())

        self.assertEqual(expected, actual)

    def test_exception_raised(self):
        """Tests the case where next() is called when there are no more elements"""
        _input = [[1, 2], [3], [], [4, 5, 6]]
        iterator = Iterator(_input)

        while iterator.has_next():
            iterator.next()

        self.assertFalse(iterator.has_next())

        with self.assertRaises(StopIteration):
            iterator.next()

    def test_empty_input(self):
        """Tests the case when the input given is an empty array"""
        _input = []
        iterator = Iterator(_input)

        self.assertFalse(iterator.has_next())

        with self.assertRaises(StopIteration):
            iterator.next()

    def test_double_empty_input(self):
        """Tests the case where the input is an array containing an empty array -> [[]]"""

        _input = [[]]
        iterator = Iterator(_input)

        self.assertFalse(iterator.has_next())

        with self.assertRaises(StopIteration):
            iterator.next()

    def test_input_with_empty_array(self):
        """Tests the case when there is an empty array with other arrays"""
        _input = [[], [1], [], [2], [], [3, 4], []]

        iterator = Iterator(_input)

        self.assertEqual(iterator.next(), 1)
        self.assertEqual(iterator.next(), 2)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 4)

        self.assertFalse(iterator.has_next())

        with self.assertRaises(StopIteration):
            iterator.next()

    def test_input_with_one_array(self):
        """Tests the case where the input is an array that contains one array of values"""
        _input = [[1, 2, 3, 4]]

        iterator = Iterator(_input)

        self.assertEqual(iterator.next(), 1)
        self.assertEqual(iterator.next(), 2)
        self.assertEqual(iterator.next(), 3)
        self.assertEqual(iterator.next(), 4)

        self.assertFalse(iterator.has_next())

        with self.assertRaises(StopIteration):
            iterator.next()

