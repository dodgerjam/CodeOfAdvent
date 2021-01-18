import unittest
from day14 import day14pt1, day14pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day14/input_test1.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day14pt1(x), 165, "Should be 165")

    def testpt2(self):
        text_file = open("day14/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day14pt1(x), 10885823581193, "Should be 10885823581193")
    
    def testpt3(self):
        text_file = open("day14/input_test2.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day14pt2(x), 208, "Should be 208")
    
    def testpt4(self):
        text_file = open("day14/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day14pt2(x), 3816594901962, "Should be 3816594901962")
    
   
if __name__ == "__main__":
    unittest.main()