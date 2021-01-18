import unittest
from day8 import day8pt1, day8pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day8/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day8pt1(x), 5, "Should be 5")
    
    def testpt2(self):
        text_file = open("day8/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day8pt1(x), 1930, "Should be 1930")
    
    def testpt3(self):
        text_file = open("day8/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day8pt2(x), 8, "Should be 8")
    
    def testpt4(self):
        text_file = open("day8/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day8pt2(x), 1688, "Should be 1688")
    
   
if __name__ == "__main__":
    unittest.main()
