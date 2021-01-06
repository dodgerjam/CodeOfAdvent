import unittest
from day4 import day4pt1, day4pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        with open("day4/input_test1.txt", 'r') as file:
            data = file.read()
        self.assertEqual(day4pt1(data), 2, "Should be 2")

    def testpt2(self):
        with open("day4/input_test2.txt", 'r') as file:
            data = file.read()
        self.assertEqual(day4pt2(data), 4, "Should be 4")

if __name__ == "__main__":
    unittest.main()
