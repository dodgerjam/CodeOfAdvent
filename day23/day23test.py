import unittest
from day23 import day23pt1, day23pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        self.assertEqual(day23pt1("389125467"), 67384529, "Should be 67384529")

    def testpt2(self):
        self.assertEqual(day23pt1("586439172"), 28946753, "Should be 28946753")
    
    def testpt3(self):
        self.assertEqual(day23pt2("389125467"), 149245887792, "Should be 149245887792")
    
    def testpt4(self):
        self.assertEqual(day23pt2("586439172"), 519044017360, "Should be 519044017360")
   
if __name__ == "__main__":
    unittest.main()