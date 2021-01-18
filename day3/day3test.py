import unittest
from day3 import day3pt1, day3pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day3/input_test.txt", "r")
        x = [list(x.strip()) for x in text_file.readlines()]
        text_file.close()
        self.assertEqual(day3pt1(x), 7, "Should be 7")

    def testpt2(self):
        text_file = open("day3/input.txt", "r")
        x = [list(x.strip()) for x in text_file.readlines()]
        text_file.close()
        self.assertEqual(day3pt1(x), 280, "Should be 280")
    
    def testpt3(self):
        text_file = open("day3/input_test.txt", "r")
        x = [list(x.strip()) for x in text_file.readlines()]
        text_file.close()
        self.assertEqual(day3pt2(x), 336, "Should be 336")
    
    def testpt4(self):
        text_file = open("day3/input.txt", "r")
        x = [list(x.strip()) for x in text_file.readlines()]
        text_file.close()
        self.assertEqual(day3pt2(x), 4355551200, "Should be 4355551200")


if __name__ == "__main__":
    unittest.main()
