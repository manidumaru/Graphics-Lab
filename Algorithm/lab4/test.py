import unittest

from bruteForce import _01knapsackBrute
from bruteFactional import FractionalBrute
from greedy import greedyKnapsack


class KnapSackTestCase(unittest.TestCase):
    # test case for fractional and 0/1 Knapsack using brute-force
    def test_brute01(self):
        # data elements with profit and weight value
        data = [
            {"profit": 5, "weight": 2},
            {"profit": 13, "weight": 5},
            {"profit": 15, "weight": 4},
            {"profit": 8, "weight": 6},
        ]
        # total size of a bag
        size = 16
        fractionalKnapsack = FractionalBrute(len(data), data, size, 0)
        # profit for a fractionalKnapsack by brute-force method should be 39.66666666666667
        self.assertEqual(fractionalKnapsack, 39.66666666666667)

    def test_brute02(self):
        # data elements with profit and weight value
        data = [
            {"profit": 5, "weight": 2},
            {"profit": 13, "weight": 5},
            {"profit": 15, "weight": 4},
            {"profit": 8, "weight": 6},
        ]
        # total size of a bag
        size = 16
        zeroOneKnapsack = _01knapsackBrute(len(data), data, size, 0)
        # profit for a 0/1 Knapsack by brute-force method should be 36
        self.assertEqual(zeroOneKnapsack, 36)

    # test case for greedy method for fractional Knapsack
    def test_greedy(self):
        # data elements with profit and weight value
        data = [
            {"profit": 5, "weight": 2},
            {"profit": 13, "weight": 7},
            {"profit": 15, "weight": 9},
            {"profit": 8, "weight": 4},
        ]
        # maximum capacity of a bag
        size = 16

        profit = greedyKnapsack(data, size)
        # profit for fractional knapsack by greedy method must be 31
        self.assertEqual(profit, 31)


if __name__ == "__main__":
    unittest.main()