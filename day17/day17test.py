import unittest
from day17 import day17pt1, day17pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day17/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day17pt1(x), 112)
    
    def testpt2(self):
        text_file = open("day17/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day17pt2(x), 848)
    
   
if __name__ == "__main__":
    unittest.main()