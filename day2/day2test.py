import unittest
from day2 import day2pt1, day2pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day2/input_test.txt", "r")
        x = [x.strip() for x in text_file.readlines()]
        text_file.close()
        self.assertEqual(day2pt1(x), 2, "Should be 2")

    def testpt2(self):
        text_file = open("day2/input.txt", "r")
        x = [x.strip() for x in text_file.readlines()]
        text_file.close()
        self.assertEqual(day2pt1(x), 469, "Should be 469")

    def testpt3(self):
        text_file = open("day2/input_test.txt", "r")
        x = [x.strip() for x in text_file.readlines()]
        text_file.close()
        self.assertEqual(day2pt2(x), 1, "Should be 1")
    
    def testpt4(self):
        text_file = open("day2/input.txt", "r")
        x = [x.strip() for x in text_file.readlines()]
        text_file.close()
        self.assertEqual(day2pt2(x), 267, "Should be 267")

if __name__ == "__main__":
    unittest.main()
