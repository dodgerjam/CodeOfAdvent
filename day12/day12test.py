import unittest
from day12 import day12pt1, day12pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day12/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day12pt1(x), 25, "Should be 25")

    def testpt2(self):
        text_file = open("day12/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day12pt1(x), 1007, "Should be 1007")
    
    def testpt3(self):
        text_file = open("day12/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day12pt2(x), 286, "Should be 286")

    def testpt4(self):
        text_file = open("day12/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day12pt2(x), 41212, "Should be 41212")
    
   
if __name__ == "__main__":
    unittest.main()