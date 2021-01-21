def day4pt1(string):
    """Checks how many passports have the expected fields.
    The expected fields are as follows:
    byr (Birth Year)
    iyr (Issue Year)
    eyr (Expiration Year)
    hgt (Height)
    hcl (Hair Color)
    ecl (Eye Color)
    pid (Passport ID)
    cid (Country ID)
    
    cid does not have to be present

    Args:
        string (str): Input text

    Returns:
        int: Number of valid passports
    """
    score = 0
    for dict1 in splitString(string):
        if checkCorrectness(dict1):
            score += 1
    return score


def splitString(string):
    """Parses the input string into a list of dictionaries
    where each dictionary represents the value of one ticket


    Args:
        string (str): Input text

    Returns:
        list: list of dicts where each dict represents one ticket
    """
    dictlist = []
    for data in string.split('\n\n'): 
        dict1 = {}
        for pair in data.replace('\n', ' ').split(' '):
            if len(pair)>0:
                pair = pair.split(":")
                key = pair[0]
                value = pair[1]
                dict1[key] = value
        dictlist.append(dict1)
    return dictlist


def checkCorrectness(dict1):
    """Checks whether all the required fields are in the dictionary keys

    Args:
        dict1 (dict): a dictionary representing a ticket

    Returns:
        boolean: returns True if all the required fields are present in dictionary keys
    """
    return all(x in dict1.keys() for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def checkCorrectnessPt2(dict1):
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    returns true if all keys are valid.

    Args:
        dict1 (dict): a passport of the dictionary form

    Returns:
        bool: True if all values are of the right form
    """
    if not all(x in dict1.keys() for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        return False
    #print([byr(dict1), iyr(dict1), eyr(dict1), hgt(dict1), hcl(dict1), ecl(dict1), pid(dict1)], all([byr(dict1), iyr(dict1), eyr(dict1), hgt(dict1), hcl(dict1), ecl(dict1), pid(dict1)]))
    return all([byr(dict1), iyr(dict1), eyr(dict1), hgt(dict1), hcl(dict1), ecl(dict1), pid(dict1)])

def byr(dict1): 
    """
    returns true if    
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    
    Args:
        dict1 (dict): a passport of the dictionary form

    Returns:
        bool: returns true if value meets requirement
    """
    if dict1['byr'].isnumeric():
        if int(dict1['byr']) in range(1920,2003):
            return True
    return False
    
def iyr(dict1):
    """    
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.

    Args:
        dict1 (dict): a passport of the dictionary form

    Returns:
        bool: returns true if value meets requirement
    """
    if dict1['iyr'].isnumeric():
        if int(dict1['iyr']) in range(2010, 2021):
            return True
    return False

def eyr(dict1):
    """ 
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.

    Args:
        dict1 (dict): a passport of the dictionary form

    Returns:
        bool: returns true if value meets requirement
    """
    if dict1['eyr'].isnumeric():
        if int(dict1['eyr']) in range(2020, 2031):
            return True
    return False

def hgt(dict1):
    """ 
    hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.

    Args:
        dict1 (dict): a passport of the dictionary form

    Returns:
        bool: returns true if value meets requirement
    """
    if dict1['hgt'][-2:] == 'in':
        if dict1['hgt'][:-2].isnumeric():
            if int(dict1['hgt'][:-2]) in range(59,77):
                return True
    if dict1['hgt'][-2:] == 'cm':
        if dict1['hgt'][:-2].isnumeric():
            if int(dict1['hgt'][:-2]) in range(150,194):
                return True
    return False


def hcl(dict1):
    """ 
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.

    Args:
        dict1 (dict): a passport of the dictionary form

    Returns:
        bool: returns true if value meets requirement
    """
    if dict1['hcl'][0] == '#' and len(dict1['hcl']) == 7:
        for char in list(dict1['hcl'][1:]):
            if char not in 'abcdef1234567890':
                return False
        return True
    return False

def ecl(dict1):
    """ 
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.

    Args:
        dict1 (dict): a passport of the dictionary form

    Returns:
        bool: returns true if value meets requirement
    """
    if dict1['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False

def pid(dict1):
    """ 
    pid (Passport ID) - a nine-digit number, including leading zeroes.

    Args:
        dict1 (dict): a passport of the dictionary form

    Returns:
        bool: returns true if value meets requirement
    """
    if len(dict1['pid']) == 9 and dict1['pid'].isnumeric():
        return True
    else:
        return False


def day4pt2(string):
    """Counts the number of passports that have all the required fields
    and the fields meet their required results.

    Args:
        string (str): Input text

    Returns:
        int: Number of passports that are valid
    """
    score = 0
    data = []
    for dict1 in splitString(string):
        if checkCorrectnessPt2(dict1):
            score += 1
    return score

if __name__ == "__main__":
    with open("day4/input.txt", 'r') as file:
        data = file.read()
    print(day4pt1(data))
    print(day4pt2(data))