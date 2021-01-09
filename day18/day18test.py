import unittest
from day18 import day18pt1, day18pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day18/input_test1.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day18pt1(x), 187465)


    def testpt2(self):
        text_file = open("day18/input_test2.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day18pt2(x), 694173)
    
   
if __name__ == "__main__":
    unittest.main()