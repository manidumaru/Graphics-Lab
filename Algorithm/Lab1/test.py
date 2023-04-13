import unittest
from search import linear_search, binary_search

class searchTest(unittest.TestCase):

    # def test_linearSearch(self):
    #     print("linear_search")
    #     values = [2,4,3,1,0,7]
    #     self.assertEqual(linear_search(values, 4), 1)
    #     self.assertEqual(linear_search(values, 0), 4)
    
    def test_binarySearch(self):
        print("binary_search")
        values = [4,8,11,12,17,34,46]
        self.assertEqual(binary_search(values, 8, 0, len(values)), 1)
        self.assertEqual(binary_search(values, 12, 0, len(values)), 3)


if __name__ == "__main__":
    unittest.main()