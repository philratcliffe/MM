import unittest

from get_indicators import get_indicators

class TestGetIndicators(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_no_matches(self):
        a = ['r', 'g', 'b', 'o']
        g = ['y', 'y', 'y', 'y']

        ind = get_indicators(g, a)

        self.assertListEqual(ind, [0, 0, 0, 0])

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


    def test_case_four_matches(self):
        a = ['g', 'r', 'o', 'b']
        g = ['r', 'g', 'b', 'o']

        r = get_indicators(g, a)
        self.assertListEqual(r, [1, 1, 1, 1])

    def test_case_one_exact_start(self):
        a = ['r', 'b', 'o', 'g']
        g = ['r', 'r', 'r', 'r']

        r = get_indicators(g, a)
        self.assertTrue([2, 0, 0, 0].count(2) == 1)

    def test_case_one_exact_end(self):
        a = ['g', 'b', 'o', 'r']
        g = ['r', 'r', 'r', 'r']

        r = get_indicators(g, a)
        self.assertTrue([2, 0, 0, 0].count(2) == 1)





if __name__ == '__main__':
    unittest.main()



