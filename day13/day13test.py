import unittest
from day13 import day13pt1, day13pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day13/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day13pt1(x), 295, "Should be 295")
    
    def testpt2(self):
        text_file = open("day13/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day13pt1(x), 2045, "Should be 2045")
    
    def testpt3(self):
        text_file = open("day13/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day13pt2(x), 1068781, "Should be 1068781")
    
    def testpt4(self):
        text_file = open("day13/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day13pt2(x), 402251700208309, "Should be 402251700208309")
    
   
if __name__ == "__main__":
    unittest.main()