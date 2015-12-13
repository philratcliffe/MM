import unittest

from get_indicators import get_indicators

class TestGetIndicators(unittest.TestCase):

    def setUp(self):
        pass

    def test_case_no_matches(self):
        c = ['1', '3', '7', '8']
        g = ['2', '2', '5', '6']

        ind = get_indicators(g, c)

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

    def test_case_difficult(self):
        a = ['g', 'g', 'o', 'b']
        g = ['r', 'g', 'b', 'o']

        r = get_indicators(g, a)
        self.assertListEqual(r, [2, 1, 1, 0])


    def test_case_one_exact_start(self):
        a = ['r', 'b', 'o', 'g']
        g = ['r', 'r', 'r', 'r']

        r = get_indicators(g, a)
        self.assertTrue(r.count(2) == 1)
        self.assertTrue(r.count(0) == 3)

    def test_case_one_exact_end(self):
        a = ['g', 'b', 'o', 'r']
        g = ['r', 'r', 'r', 'r']

        r = get_indicators(g, a)
        self.assertTrue(r.count(2) == 1)
        self.assertTrue(r.count(0) == 3)


    def test_case_bug_1(self):
        c = [6, 3, 1, 2]
        g = [1, 6, 1, 6]

        # looking at the guess in order:
        # 1 -> 0 (later 1 gets the 2)
        # 6 -> 1 (right num wrong location)
        # 1 -> 2 (right num right location)
        # 6 -> 0 (alredy done)
        r = get_indicators(g, c)
        self.assertListEqual(r, [2, 1, 0, 0])




if __name__ == '__main__':
    unittest.main()



