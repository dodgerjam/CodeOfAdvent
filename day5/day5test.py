import unittest
from day5 import getRowID, getColumnID, getSeatID, day5pt1, day5pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        x =["BFFFBBFRRR",
            "FFFBBBFRRR",
            "BBFFBBFRLL"]
       
        self.assertEqual(getRowID(x[0]), 70, "Should be 70")
        self.assertEqual(getColumnID(x[0]), 7, "Should be 7")
        self.assertEqual(getSeatID(x[0]), 567, "Should be 567")

        # FFFBBBFRRR: row 14, column 7, seat ID 119.
        self.assertEqual(getRowID(x[1]), 14, "Should be 14")
        self.assertEqual(getColumnID(x[1]), 7, "Should be 7")
        self.assertEqual(getSeatID(x[1]), 119, "Should be 119")
        # BBFFBBFRLL: row 102, column 4, seat ID 820.
        self.assertEqual(getRowID(x[2]), 102, "Should be 102")
        self.assertEqual(getColumnID(x[2]), 4, "Should be 4")
        self.assertEqual(getSeatID(x[2]), 820, "Should be 7")
    
    def testpt2(self):
        text_file = open("day5/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day5pt1(x), 838, "Should be 838")

    def testpt3(self):
        text_file = open("day5/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day5pt2(x), 714, "Should be 714")
   
if __name__ == "__main__":
    unittest.main()
