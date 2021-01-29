import unittest

from challenges.problem_001.solution import problem_1


class SumsToK(unittest.TestCase):
    def test_example_1(self):
        num_list = [10, 15, 3, 7]
        k = 17
        actual = problem_1(num_list, k)
        self.assertTrue(actual)

    def test_example_2(self):
        num_list = [10, -15, 3, 7]
        k = -5
        actual = problem_1(num_list, k)
        self.assertTrue(actual)

    def test_example_3(self):
        num_list = [1]
        k = 1
        actual = problem_1(num_list, k)
        self.assertFalse(actual)

    def test_example_4(self):
        num_list = []
        k = 1
        actual = problem_1(num_list, k)
        self.assertFalse(actual)

    def test_example_5(self):
        num_list = [10, -15, 3, 7]
        k = 10
        actual = problem_1(num_list, k)
        self.assertTrue(actual)

    def test_example_6(self):
        num_list = [10, -15, 3, 7, 10, 9, 15, -23, 49, 8, 16, 33]
        k = 49
        actual = problem_1(num_list, k)
        self.assertTrue(actual)

    def test_example_7(self):
        num_list = [20, 10, 10, 40, 40, 30]
        k = 50
        actual = problem_1(num_list, k)
        self.assertTrue(actual)
