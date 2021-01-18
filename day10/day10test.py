import unittest
from day10 import day10pt1, day10pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day10/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day10pt1(x), 220, "Should be 220")

    def testpt2(self):
        text_file = open("day10/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day10pt1(x), 2484, "Should be 2484")
    
    def testpt3(self):
        text_file = open("day10/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day10pt2(x), 19208, "Should be 19208")

    def testpt4(self):
        text_file = open("day10/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day10pt2(x), 15790581481472, "Should be 15790581481472")
    
   
if __name__ == "__main__":
    unittest.main()
