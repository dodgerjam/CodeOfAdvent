import unittest
from day21 import day21pt1, day21pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day21/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day21pt1(x), 5)

    def testpt2(self):
        text_file = open("day21/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day21pt2(x), "mxmxvkd,sqjhc,fvjkl")
   
if __name__ == "__main__":
    unittest.main()