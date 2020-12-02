import unittest
from day1 import day1pt1, day1pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        lines = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(day1pt1(lines), 514579, "Should be 514579")

    def testpt2(self):
        lines = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(day1pt2(lines), 241861950, "Should be 241861950")



if __name__ == "__main__":
    unittest.main()
