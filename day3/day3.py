def day3pt1(x):
    """Assumes 3 Across one down and counts the number 
    of trees (#) in the path

    Args:
        x (list): 2-d list containing '.' and '#'.
        '#' indicates a tree
 
    Returns:
        int: sum of trees (#) hit in path
    """
    mod = len(x[0])
    tree_count = 0
    for i in range(len(x)):
        if x[i][3*i % mod] == '#':
            tree_count += 1
    return tree_count


def day3pt2a(x, ratio = 1):
    """Performs a count of trees (#) in a path for a given ratio

    Args:
        x (list): 2-d list containing '.' and '#'.
        ratio (float, optional): defines the angle of the path, i.e if = 3 
        then path goes 3 across and 1 down

    Returns:
        int: sum of trees (#) hit in path
    """
    mod = len(x[0])
    tree_count = 0
    for i in range(0, len(x)):
        if int(ratio*i) == ratio*i:
            if x[i][int(ratio*i) % mod] == '#':
                tree_count += 1
    return tree_count

def day3pt2(x):
    """Returns the product of trees hit of different paths.

    Args:
        x (list): 2-d list containing '.' and '#'.

    Returns:
        int: Product of trees hit of different paths.
    """
    score = 1
    for ratio in [1,3,5,7,0.5]:
        score *= day3pt2a(x, ratio = ratio)
    return score


if __name__ == "__main__":
    text_file = open("day3/input.txt", "r")
    x = [list(x.strip()) for x in text_file.readlines()]
    text_file.close()
    print(day3pt1(x))
    print(day3pt2(x))
