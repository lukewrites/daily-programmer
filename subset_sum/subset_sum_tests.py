from subset_sum import sum_finder
import unittest


class testSums(unittest.TestCase):

    def setUp(self):
        self.empty_list = []
        self.zero_no_pair = [-1, 0, 2]
        self.no_zero_no_pair = [-1, 2]
        self.zero_and_pair = [-1, 0, -1]
        self.no_zero_pair = [-2, -1, 2, 3]

    def test_if_i_catch_zero(self):
        self.assertTrue(sum_finder(self.zero_no_pair), msg='No 0 found!')
        self.assertTrue(sum_finder(self.zero_and_pair), msg='No 0 found!')

    def test_if_i_catch_a_pair(self):
        self.assertTrue(sum_finder(self.no_zero_pair), msg='Pair where?')

    def test_empty_list(self):
        self.assertFalse(sum_finder(self.empty_list))

    def test_reddit_examples(self):
        self.assertFalse(sum_finder([-5, -3, -1, 2, 4, 6]), msg=None)
        self.assertTrue(sum_finder([-1, 1]), msg=None)
        self.assertTrue(sum_finder([-97364, -71561, -69336, 19675, 71561, 97863]), msg=None)
        self.assertTrue(sum_finder([-53974, -39140, -36561, -23935, -15680, 0]), msg=None)


if __name__ == '__main__':
    unittest.main()
