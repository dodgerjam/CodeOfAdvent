import unittest
from day1 import day1pt1, day1pt2
import numpy as np

class TestSum(unittest.TestCase):

    def testpt1(self):
        lines = np.loadtxt("day1/input_test.txt",  delimiter="\n", unpack=False, dtype=np.int32)
        self.assertEqual(day1pt1(lines), 514579, "Should be 514579")

    def part1(self):
        lines = np.loadtxt("day1/input_test.txt",  delimiter="\n", unpack=False, dtype=np.int32)
        self.assertEqual(day1pt1(lines), 889779, "Should be 889779")

    def testpt2(self):
        lines = np.loadtxt("day1/input_test.txt",  delimiter="\n", unpack=False, dtype=np.int32)
        self.assertEqual(day1pt2(lines), 241861950, "Should be 241861950")
    
    def part2(self):
        lines = np.loadtxt("day1/input_test.txt",  delimiter="\n", unpack=False, dtype=np.int32)
        self.assertEqual(day1pt2(lines), 76110336, "Should be 76110336")



if __name__ == "__main__":
    unittest.main()
