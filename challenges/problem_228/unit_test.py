import unittest

from challenges.problem_228.solution import largest_int


class LargestIntegerTest(unittest.TestCase):

    def test_example(self):
        _input = [10, 7, 76, 415]
        expected = 77641510
        actual = largest_int(_input)
        self.assertEqual(expected, actual)

    def test_duplicate_number(self):
        _input = [20, 15, 23, 89, 23]
        expected = 8923232015
        actual = largest_int(_input)
        self.assertEqual(expected, actual)

    def test_identical_first_two_digits(self):
        _input = [23, 234, 2367, 23897, 230987]
        expected = 23897236723423230987
        actual = largest_int(_input)
        self.assertEqual(expected, actual)
