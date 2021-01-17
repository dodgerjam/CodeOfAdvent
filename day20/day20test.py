import unittest
from day20 import day20pt1, day20pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day20/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day20pt1(x), 20899048083289)
   
    def testpt2(self):
        text_file = open("day20/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day20pt2(x), 273)

if __name__ == "__main__":
    unittest.main()