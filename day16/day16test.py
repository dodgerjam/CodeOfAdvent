import unittest
from day16 import day16pt1, day16pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day16/input_test1.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day16pt1(x), 71)
    
    def testpt2(self):
        text_file = open("day16/input_test2.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day16pt2(x), 12*11)
    
   
if __name__ == "__main__":
    unittest.main()