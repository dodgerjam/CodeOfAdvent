import unittest
from day12 import day12pt1, day12pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day12/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day12pt1(x), 25)
    
    def testpt2(self):
        text_file = open("day12/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day12pt2(x), 286)
    
   
if __name__ == "__main__":
    unittest.main()