import unittest
from day6 import day6pt2, day6pt1

class TestSum(unittest.TestCase):

    def testpt1(self):
        with open("day6/input_test.txt", 'r') as file:
                data = file.read()
        self.assertEqual(day6pt1(data), 11, "Should equal 11")

    def testpt2(self):
        with open("day6/input_test.txt", 'r') as file:
                data = file.read()
        self.assertEqual(day6pt2(data), 6, "Should equal 6")
   
if __name__ == "__main__":
    unittest.main()
