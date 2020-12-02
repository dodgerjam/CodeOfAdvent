def isValidPt1(key):
    """Returns whether the count of a char in a string is in a certain range, all defined by a 
    string of the form "<int1>-<int2> <char>: <string>".

    Args:
        key (string): string of the form "<int1>-<int2> <char>: <string>" e.g. "1-3 a: abcde"

    Returns:
        bool: True if the count of <char> in <string> is in the range [<int1>, <int2>]
    """
    keysplit = key.split(' ')
    # e.g. Convert '16-17' to [16, 17]
    min_char, max_char = tuple(int(x) for x in keysplit[0].split('-'))
    # Convert 'm:' to 'm'
    char = keysplit[1][0]
    # E.g 'jnlntbblbbqbkqmbbb'
    string = keysplit[2]

    if string.count(char) in range(min_char, max_char + 1):
        return True
    else:
        return False


def day2pt1(x):
    """Counts the number of strings in a list which is valid

    Args:
        x (list): list of strings of the form "<int1>-<int2> <char>: <string>"

    Returns:
        int: the count of the strings in the list which are valid (defined by isValidPt1)
    """
    score = 0
    for key in x:
        if isValidPt1(key):
            score += 1
    return score 

def isValidPt2(key):
    """Returns whether only one of certain indexes of a string is a certain char with a
    string of the form "<int1>-<int2> <char>: <string>".

    Args:
        key (string): string of the form "<int1>-<int2> <char>: <string>" e.g. "1-3 a: abcde"

    Returns:
        bool: True if either <string><int1 - 1> = <char> or <string><int2 - 1> = <char> but not both.
    """
    keysplit = key.split(' ')
    # e.g. Convert '16-17' to [16, 17]
    ind1, ind2 = tuple(int(x) for x in keysplit[0].split('-'))
    # Convert 'm:' to 'm'
    char = keysplit[1][0]
    # E.g 'jnlntbblbbqbkqmbbb'
    string = keysplit[2]


    if (string[ind1-1] == char) and (string[ind2-1] != char):
        return True
    elif (string[ind1-1] != char) and (string[ind2-1] == char):
        return True
    else:
        return False


def day2pt2(x):
    """Counts the number of strings in a list which is valid

    Args:
        x (list): list of strings of the form "<int1>-<int2> <char>: <string>"

    Returns:
        int: the count of the strings in the list which are valid (defined by isValidPt2)
    """
    score = 0
    for key in x:
        if isValidPt2(key):
            score += 1
    return score 



if __name__ == "__main__":
    text_file = open("input.txt", "r")
    x = [x.strip() for x in text_file.readlines()]
    text_file.close()
    print(day2pt1(x))
    print(day2pt2(x))