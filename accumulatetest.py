import unittest
from accumulate import accumulate


class AccumulateTest(unittest.TestCase):
    def test_empty_sequence(self):
        self.assertEqual(accumulate([], lambda x: x / 2), [])

    def test_pow(self):
        self.assertEqual(accumulate([1,2,3,4],lambda x:x*x),[1,4,9,16])




if __name__ == '__main__':
    unittest.main()
