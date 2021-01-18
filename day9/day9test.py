import unittest
from day9 import day9pt1, day9pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day9/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day9pt1(x, prev=5), 127, "Should be 127")
    
    def testpt2(self):
        text_file = open("day9/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day9pt1(x), 1309761972, "Should be 1309761972")
    
    def testpt3(self):
        text_file = open("day9/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day9pt2(x, prev=5), 62, "Should be 62")
    
    def testpt4(self):
        text_file = open("day9/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day9pt2(x), 177989832, "Should be 177989832")
    
   
if __name__ == "__main__":
    unittest.main()
