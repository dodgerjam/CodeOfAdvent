import unittest
from day7 import day7pt1, day7pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day7/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day7pt1(x), 4)
    
    # def testpt2(self):
    #     text_file = open("day7/input.txt", "r")
    #     x = text_file.readlines()
    #     text_file.close()
    #     print(day7pt1(x))
    #     self.assertEqual(day7pt1(x), 139, "Should be 139")
    
    def testpt3(self):
        text_file = open("day7/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day7pt2(x), 32, "Should be 32")

    def testpt4(self):
        text_file = open("day7/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day7pt2(x), 58175, "Should be 58175")
    
   
if __name__ == "__main__":
    unittest.main()

    
   
if __name__ == "__main__":
    unittest.main()
