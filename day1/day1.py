import numpy as np 


def day1pt1(lines):
    """Returns the product of the two integers in lines that sum to 2020 by 
    iterating through every combination.

    Args:
        lines (array type): list of integers

    Returns:
        int: the product of the two integers in lines that sum to 2020
    """
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            if lines[i]+lines[j]==2020:
                return lines[i] * lines[j]

def day1pt2(lines):
    """Returns the product of the three integers in lines that sum to 2020 by 
    iterating through every combination.

    Args:
        lines (array type): list of integers

    Returns:
        int: the product of the three integers in lines that sum to 2020
    """

    for i in range(len(lines)-2):
        for j in range(i+1, len(lines)-1):
            for k in range(j+1, len(lines)):
                if lines[i]+lines[j]+lines[k]==2020:
                    return lines[i] * lines[j] * lines[k]

if __name__ == "__main__":
    lines = np.loadtxt("day1/input.txt",  delimiter="\n", unpack=False, dtype=np.int32)
    print(day1pt1(lines))
    print(day1pt2(lines))