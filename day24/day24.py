from collections import Counter

def day24pt1(x):
    points = []
    for row in x:
        directions = splitRow(row.strip())
        coordinates = getCoordinates(directions)
        points.append(coordinates)
    return len([v for k,v in Counter(points).items() if v%2 == 1])

def day24pt2(x):
    points = []
    for row in x:
        directions = splitRow(row.strip())
        coordinates = getCoordinates(directions)
        points.append(coordinates)
    
    my_dict = {}
    for k,v in Counter(points).items():
        if v%2 == 1:
            my_dict[k] = True
        else:
            my_dict[k] = False
            
    for i in range(100):
        # add adjacent pairs
        new_dict = {}
        for key, value in my_dict.items():
            adjacent_values = getAdjacentValues(key)
            new_dict[key] = value
            for ap in adjacent_values:
                if ap not in my_dict.keys():
                    new_dict[ap] = False
        
        for key, value in new_dict.items():
            count = 0
            for ap in getAdjacentValues(key):
                if ap in my_dict.keys():
                    if my_dict[ap]:
                        count += 1
            if value and (count == 0 or count>2):
                new_dict[key] = False
            elif not value and count == 2:
                new_dict[key] = True
            else:
                new_dict[key] = value

        for key, value in new_dict.items():
            my_dict[key] = value
        
    return len([v for v in my_dict.values() if v])


def getAdjacentValues(key):
    """Returns all 6 adjacent co-ordinates to a point on a hexagonal grid

    Args:
        key (list): list of 2 integers. 1st element represents 
        the x co-ordinate, 2nd element represents the y

    Returns:
        list: list of tuples of the 6 adjacent values.
    """
    x = key[0]
    y = key[1]
    return [(x+2,y),(x-2,y),(x+1,y+1),(x+1,y-1),(x-1,y+1),(x-1,y-1)]

def getCoordinates(directions):
    coordinates = [0, 0]
    for d in directions:
        if d == 'e':
            coordinates[0] += 2
        if d == 'w':
            coordinates[0] -= 2
        if d == 'ne':
            coordinates[0] += 1
            coordinates[1] += 1
        if d == 'nw':
            coordinates[0] -= 1
            coordinates[1] += 1
        if d == 'se':
            coordinates[0] += 1
            coordinates[1] -= 1
        if d == 'sw':
            coordinates[0] -= 1
            coordinates[1] -= 1

    return tuple(coordinates)


def splitRow(row):
    # e, se, sw, w, nw, and ne
    directions = []
    i = 0
    while i < len(row):
        if row[i] in ['n', 's']:
            directions.append(row[i:i+2])
            i += 2
        else:
            directions.append(row[i])
            i += 1
    return directions

if __name__ == "__main__":
    text_file = open("day24/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day24pt1(x))
    print(day24pt2(x))
