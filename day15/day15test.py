import unittest
from day15 import day15pt1, day15pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        start = [0,3,6]
        self.assertEqual(day15pt1(start), 436, "Should be 436")
        start = [1,3,2]
        self.assertEqual(day15pt1(start), 1, "Should be 1")
        start = [2,1,3]
        self.assertEqual(day15pt1(start), 10, "Should be 10")
        start = [1,2,3]
        self.assertEqual(day15pt1(start), 27, "Should be")
        start = [2,3,1]
        self.assertEqual(day15pt1(start), 78)
        start = [3,2,1]
        self.assertEqual(day15pt1(start), 438)
        start = [3,1,2]
        self.assertEqual(day15pt1(start), 1836)
    
    def testpt2a(self):
        start = [0,3,6]
        self.assertEqual(day15pt2(start, n_number=2020), 436, "Should be 436")
        start = [1,3,2]
        self.assertEqual(day15pt2(start, n_number = 2020), 1)
        start = [2,1,3]
        self.assertEqual(day15pt2(start, n_number = 2020), 10)
        start = [1,2,3]
        self.assertEqual(day15pt2(start, n_number = 2020), 27)
        start = [2,3,1]
        self.assertEqual(day15pt2(start, n_number = 2020), 78)
        start = [3,2,1]
        self.assertEqual(day15pt2(start, n_number = 2020), 438)
        start = [3,1,2]
        self.assertEqual(day15pt2(start, n_number = 2020), 1836)   
    
    # def testpt2(self):
    #     start = [0,3,6]
    #     self.assertEqual(day15pt2(start), 175594)
    #     start = [1,3,2]
    #     self.assertEqual(day15pt2(start), 2578)
    #     start = [2,1,3]
    #     self.assertEqual(day15pt2(start), 3544142)
    #     start = [1,2,3]
    #     self.assertEqual(day15pt2(start), 261214)
    #     start = [2,3,1]
    #     self.assertEqual(day15pt2(start), 6895259)
    #     start = [3,2,1]
    #     self.assertEqual(day15pt2(start), 18)
    #     start = [3,1,2]
    #     self.assertEqual(day15pt2(start), 362)
    
   
if __name__ == "__main__":
    unittest.main()