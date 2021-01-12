import unittest
from day22 import day22pt1, day22pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day22/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day22pt1(x), 306)
    
    def testpt2(self):
        text_file = open("day22/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day22pt2(x), 291)
   
if __name__ == "__main__":
    unittest.main()