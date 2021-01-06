import unittest
from day10 import day10pt1, day10pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day10/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day10pt1(x), 220)
    
    def testpt2(self):
        text_file = open("day10/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day10pt2(x), 19208)
    
   
if __name__ == "__main__":
    unittest.main()
