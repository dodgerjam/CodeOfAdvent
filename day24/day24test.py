import unittest
from day24 import day24pt1, day24pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day24/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day24pt1(x), 10, "Should be 10")
    
    def testpt2(self):
        text_file = open("day24/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day24pt1(x), 434, "Should be 434")
    
    def testpt3(self):
        text_file = open("day24/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day24pt2(x), 2208, "Should be 2208")

    def testpt4(self):
        text_file = open("day24/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day24pt2(x), 3955, "Should be 3955")

if __name__ == "__main__":
    unittest.main()