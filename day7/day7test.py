import unittest
from day7 import day7pt1, day7pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day7/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        expected_result = ['bright white bag', 'muted yellow bag', 'dark orange bag', 'light red bag']
        self.assertCountEqual(day7pt1(x), expected_result)
    
    def testpt2(self):
        text_file = open("day7/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day7pt2(x), 32)
    
   
if __name__ == "__main__":
    unittest.main()
