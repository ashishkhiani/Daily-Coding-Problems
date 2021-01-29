import unittest
from challenges.problem_2.solution import problem_2


class Product(unittest.TestCase):
    def test_example_1(self):
        num_list = [1, 2, 3, 4, 5]
        expected = [120, 60, 40, 30, 24]
        actual = problem_2(num_list)
        self.assertEqual(expected, actual)

    def test_example_2(self):
        num_list = [3, 2, 1]
        expected = [2, 3, 6]
        actual = problem_2(num_list)
        self.assertEqual(expected, actual)

    def test_example_3(self):
        num_list = [0, 1, 3, 5]
        expected = [15, 0, 0, 0]
        actual = problem_2(num_list)
        self.assertEqual(expected, actual)

    def test_example_4(self):
        num_list = [1, 2, 0, 7, 0]
        expected = [0, 0, 0, 0, 0]
        actual = problem_2(num_list)
        self.assertEqual(expected, actual)

    def test_example_5(self):
        num_list = [5, 8]
        expected = [8, 5]
        actual = problem_2(num_list)
        self.assertEqual(expected, actual)

    def test_example_6(self):
        num_list = [9, 0]
        expected = [0, 9]
        actual = problem_2(num_list)
        self.assertEqual(expected, actual)

    def test_example_7(self):
        num_list = [23]

        with self.assertRaises(Exception):
            problem_2(num_list)

    def test_example_8(self):
        num_list = []

        with self.assertRaises(Exception):
            problem_2(num_list)
