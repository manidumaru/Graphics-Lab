import unittest
from algorithm import mergeSort, insertion

class searchTest(unittest.TestCase):

    def test_insertion(self):
        arr = [6,9,4,2,0,3,1,8,5,7]
        expected_output = [0,1,2,3,4,5,6,7,8,9]

        sorted = insertion(arr)
        self.assertListEqual(sorted, expected_output)

    def test_merge(self):
        arr = [6,9,4,2,0,3,1,8,5,7]
        expected_output = [0,1,2,3,4,5,6,7,8,9]
        # self.assertListEqual(arr, expected_output)
        mergeSort(arr)
        self.assertListEqual(arr, expected_output)


if __name__ == "__main__":
    unittest.main()