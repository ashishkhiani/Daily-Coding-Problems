import unittest

from challenges.problem_180.solution import interleave


class InterleaveTest(unittest.TestCase):

    def test_example_1(self):
        """Tests the given example"""
        _input = [1, 2, 3, 4, 5]
        expected = [1, 5, 2, 4, 3]
        actual = interleave(_input)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        """Tests the given example"""
        _input = [1, 2, 3, 4]
        expected = [1, 4, 2, 3]
        actual = interleave(_input)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        """Tests the given example"""
        _input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        expected = [1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]
        actual = interleave(_input)
        self.assertEqual(expected, actual)

    def test_empty_input(self):
        """Tests the case where the input is an empty array"""
        _input = []
        expected = []
        actual = interleave(_input)
        self.assertEqual(expected, actual)

    def test_null_input(self):
        """Tests the case where the input is null"""
        _input = None
        expected = []
        actual = interleave(_input)
        self.assertEqual(expected, actual)
