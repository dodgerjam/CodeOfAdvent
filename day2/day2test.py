import unittest
from day2 import day2pt1, day2pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        str1 = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(day2pt1(str1), 2, "Should be 2")

    def testpt2(self):
        str1 = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
        self.assertEqual(day2pt2(str1), 1, "Should be 1")

if __name__ == "__main__":
    unittest.main()
