import unittest
from day20 import day20pt1, day20pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day20/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day20pt1(x), 20899048083289, "Should be 20899048083289")

    def testpt2(self):
        text_file = open("day20/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day20pt1(x), 23386616781851, "Should be 23386616781851")
   
    def testpt3(self):
        text_file = open("day20/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day20pt2(x), 273, "Should be 273")

    def testpt4(self):
        text_file = open("day20/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day20pt2(x), 2376, "Should be 2376")

if __name__ == "__main__":
    unittest.main()