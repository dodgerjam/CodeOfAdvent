import unittest
from day21 import day21pt1, day21pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        text_file = open("day21/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day21pt1(x), 5, "Should be 5")

    def testpt2(self):
        text_file = open("day21/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day21pt1(x), 2176, "Should be 2176")

    def testpt3(self):
        text_file = open("day21/input_test.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day21pt2(x), "mxmxvkd,sqjhc,fvjkl", "Should be mxmxvkd,sqjhc,fvjkl")

    def testpt4(self):
        text_file = open("day21/input.txt", "r")
        x = text_file.readlines()
        text_file.close()
        self.assertEqual(day21pt2(x), "lvv,xblchx,tr,gzvsg,jlsqx,fnntr,pmz,csqc", "Should be lvv,xblchx,tr,gzvsg,jlsqx,fnntr,pmz,csqc")
   
if __name__ == "__main__":
    unittest.main()