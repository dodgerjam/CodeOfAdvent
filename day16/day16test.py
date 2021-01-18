import unittest
from day16 import day16pt1, day16pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day16/input_test1.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day16pt1(x), 71, "Should be 71")

    def testpt2(self):
        text_file = open("day16/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day16pt1(x), 26026, "Should be 26026")
    
    def testpt3(self):
        text_file = open("day16/input_test2.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day16pt2(x), 132, "Should be 132")
    
    def testpt4(self):
        text_file = open("day16/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day16pt2(x), 1305243193339, "Should be 1305243193339")
    
   
if __name__ == "__main__":
    unittest.main()