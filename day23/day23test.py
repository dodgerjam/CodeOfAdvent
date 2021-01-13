import unittest
from day23 import day23pt1, day23pt2

class TestSum(unittest.TestCase):

    def testpt1(self):

        self.assertEqual(day23pt1("389125467"), "67384529")
    
    def testpt2(self):

        self.assertEqual(day23pt2("389125467"), 149245887792)
   
if __name__ == "__main__":
    unittest.main()