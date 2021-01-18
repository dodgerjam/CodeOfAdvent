import unittest
from day25 import day25pt1

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day25/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day25pt1(x), 14897079, "Should be 14897079")

    def testpt1(self):
        text_file = open("day25/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day25pt1(x), 18293391, "Should be 18293391")

if __name__ == "__main__":
    unittest.main()