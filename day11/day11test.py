import unittest
from day11 import day11pt1, day11pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day11/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day11pt1(x), 37, "Should be 37")

    def testpt2(self):
        text_file = open("day11/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day11pt1(x), 2321, "Should be 2321")
    
    
    def testpt3(self):
        text_file = open("day11/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day11pt2(x), 26, "Should be 37")
    
    def testpt4(self):
        text_file = open("day11/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day11pt2(x), 2102, "Should be 2102")
    
   
if __name__ == "__main__":
    unittest.main()
