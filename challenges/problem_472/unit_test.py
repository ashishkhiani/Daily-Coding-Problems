import unittest

from challenges.problem_472.solution import decode_message


class DecodedMessageCounter(unittest.TestCase):

    def test_example_1(self):
        """Tests given example"""
        _input = '111'
        expected = ['aaa', 'ka', 'ak']
        actual = decode_message(_input)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_example_2(self):
        """Tests another example"""
        _input = '1847'
        expected = ['ahdg', 'rdg']
        actual = decode_message(_input)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_example_3(self):
        """Tests another example"""
        _input = '2361510'
        expected = ['bcfaej', 'wfaej', 'bcfoj', 'wfoj']
        actual = decode_message(_input)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_example_4(self):
        """Tests another example"""
        _input = '1221113'
        expected = [
            'abbaaac',
            'abuaac',
            'avaaac',
            'lbaaac',
            'luaac',
            'abbkac',
            'avkac',
            'lbkac',
            'abbakc',
            'abukc',
            'avakc',
            'lbakc',
            'lukc',
            'abbaam',
            'abuam',
            'avaam',
            'lbaam',
            'luam',
            'abbkm',
            'avkm',
            'lbkm'
        ]
        actual = decode_message(_input)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_example_5(self):
        """Tests another example"""
        _input = '1010101010'
        expected = ['jjjjj']
        actual = decode_message(_input)
        self.assertEqual(sorted(expected), sorted(actual))
