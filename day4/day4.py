def day4pt1(string):
    score = 0
    for dict1 in splitString(string):
        if checkCorrectness(dict1):
            score += 1
    return score


def splitString(string):
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

    Args:
        dict1 ([type]): [description]

    Returns:
        [type]: [description]
    """
    if not all(x in dict1.keys() for x in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']):
        return False
    #print([byr(dict1), iyr(dict1), eyr(dict1), hgt(dict1), hcl(dict1), ecl(dict1), pid(dict1)], all([byr(dict1), iyr(dict1), eyr(dict1), hgt(dict1), hcl(dict1), ecl(dict1), pid(dict1)]))
    return all([byr(dict1), iyr(dict1), eyr(dict1), hgt(dict1), hcl(dict1), ecl(dict1), pid(dict1)])

def byr(dict1):      
    """
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    """
    if dict1['byr'].isnumeric():
        if int(dict1['byr']) in range(1920,2003):
            return True
    return False
    
def iyr(dict1):
    """ 
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    """
    if dict1['iyr'].isnumeric():
        if int(dict1['iyr']) in range(2010, 2021):
            return True
    return False

def eyr(dict1):
    """ 
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
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
    """
    if dict1['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    else:
        return False

def pid(dict1):
    """ 
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    """
    if len(dict1['pid']) == 9 and dict1['pid'].isnumeric():
        return True
    else:
        return False


def day4pt2(string):
    score = 0
    data = []
    for dict1 in splitString(string):

        if checkCorrectnessPt2(dict1):
            score += 1
            dict1['PASS'] = True
        data.append(dict1)
    return score

if __name__ == "__main__":
    with open("day4/input.txt", 'r') as file:
        data = file.read()
    print(day4pt1(data))
    print(day4pt2(data))