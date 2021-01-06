import unittest
from day11 import day11pt1, day11pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day11/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day11pt1(x), 37)
    
    def testpt2(self):
        text_file = open("day11/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day11pt2(x), 26)
    
   
if __name__ == "__main__":
    unittest.main()
