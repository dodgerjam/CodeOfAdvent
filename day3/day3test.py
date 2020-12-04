import unittest
from day3 import day3pt1, day3pt2

class TestSum(unittest.TestCase):

    def testpt1(self):
        x =["..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"]
        x = [list(y) for y in x]
        self.assertEqual(day3pt1(x), 7, "Should be 7")
    
    def testpt2(self):
        x =["..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#"]

        x = [list(y) for y in x]

        self.assertEqual(day3pt2(x), 336, "Should be 336")


if __name__ == "__main__":
    unittest.main()
