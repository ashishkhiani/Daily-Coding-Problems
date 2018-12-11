import unittest

from challenges.problem_241.solution import calculate_h_index


class IndexCalculatorTest(unittest.TestCase):

    def test_example(self):
        """Tests the given example"""
        _input = [4, 3, 0, 1, 5]
        expected = 3
        actual = calculate_h_index(_input)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        """Tests the case where some papers have the same number of citations"""
        _input = [17, 33, 30, 7, 8, 20, 15, 7, 6, 5, 4]
        expected = 7
        actual = calculate_h_index(_input)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        """Tests the case where only one paper has a citation"""
        _input = [0, 0, 0, 1, 0, 0]
        expected = 1
        actual = calculate_h_index(_input)
        self.assertEqual(expected, actual)

    def test_example_4(self):
        """Tests the case where all the citations are the same number"""
        _input = [0, 0, 0, 2, 0, 2, 0, 2]
        expected = 2
        actual = calculate_h_index(_input)
        self.assertEqual(expected, actual)

