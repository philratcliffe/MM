import unittest

from get_indicators import get_indicators

class TestGetIndicators(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_no_matches(self):
        a = ['r', 'g', 'b', 'o']
        g = ['y', 'v', 't', 'w']

        r = get_indicators(g, a)
        self.assertListEqual(r, [0, 0, 0, 0])

    def test_case_one_exact_matche(self):
        a = ['r', 'g', 'b', 'o']
        g = ['r', 'v', 't', 'w']

        r = get_indicators(g, a)
        self.assertListEqual(r, [2, 0, 0, 0])


    def test_case_four_exact_matches(self):
        a = ['r', 'g', 'b', 'o']
        g = ['r', 'g', 'b', 'o']

        r = get_indicators(g, a)
        self.assertListEqual(r, [2, 2, 2, 2])


if __name__ == '__main__':
    unittest.main()



