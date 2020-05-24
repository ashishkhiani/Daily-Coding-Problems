import unittest

from challenges.problem_470.solution import find_nearest_larger_number, find_nearest_larger_number_constant_time


class NearestLargerNumber(unittest.TestCase):

    def validate(self, _input, expected):
        actual = find_nearest_larger_number(_input[0], _input[1])
        self.assertEqual(expected, actual)

    def test_example_1(self):
        """Tests given example"""
        _input = [4, 1, 3, 5, 6], 0
        expected = 3
        self.validate(_input, expected)

    def test_example_2(self):
        """Tests the case where nearest larger numbers are equal"""
        _input = [11, 5, 4, 6, 1, 4, 11, 9, 33, 18], 3
        expected = 0
        self.validate(_input, expected)

    def test_example_3(self):
        """Tests the case where there isn't a nearest larger number"""
        _input = [0, 1, 2, 1, 0], 2
        expected = None
        self.validate(_input, expected)

    def test_example_4(self):
        """Tests another example"""
        _input = [34, 5, 4, 6, 1, 4, 11, 9, 33, 18], 8
        expected = 0
        self.validate(_input, expected)