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
        self.assertEqual(day15pt1(start), 27, "Should be 27")
        start = [2,3,1]
        self.assertEqual(day15pt1(start), 78, "Should be 78")
        start = [3,2,1]
        self.assertEqual(day15pt1(start), 438, "Should be 438")
        start = [3,1,2]
        self.assertEqual(day15pt1(start), 1836, "Should be 1836")
    
    def testpt2(self):
        start = [14,8,16,0,1,17]
        self.assertEqual(day15pt1(start), 240, "Should be 240")
    
    def testpt3(self):
        start = [0,3,6]
        self.assertEqual(day15pt2(start, n_number=2020), 436, "Should be 436")
        start = [1,3,2]
        self.assertEqual(day15pt2(start, n_number = 2020), 1, "Should be 1")
        start = [2,1,3]
        self.assertEqual(day15pt2(start, n_number = 2020), 10, "Should be 10")
        start = [1,2,3]
        self.assertEqual(day15pt2(start, n_number = 2020), 27, "Should be 27")
        start = [2,3,1]
        self.assertEqual(day15pt2(start, n_number = 2020), 78, "Should be 78")
        start = [3,2,1]
        self.assertEqual(day15pt2(start, n_number = 2020), 438, "Should be 438")
        start = [3,1,2]
        self.assertEqual(day15pt2(start, n_number = 2020), 1836, "Should be 1836")   

    def testpt4(self):
        start = [14,8,16,0,1,17]
        self.assertEqual(day15pt2(start), 505, "Should be 505")
    
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