def day17pt1(x, cycles = 6):
    grid = [list(i.strip()) for i in x]
    my_dict = {}
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            my_dict[(x,y,0)] = grid[x][y]
    """
    If a cube is active and exactly 2 or 3 of its neighbors are also active, the cube remains active. 
    Otherwise, the cube becomes inactive.
    If a cube is inactive but exactly 3 of its neighbors are active, the cube becomes active. 
    Otherwise, the cube remains inactive.
    """
    for i in range(cycles):
        # add additional points
        my_dict = addAdditionalPointsPt1(my_dict)
        # get adjacent points
        adjacent_dict = {}
        for key in my_dict.keys():
            adjacent_dict[key] = getAdjacentPointsPt1(key, my_dict)
        # update points
        for key in my_dict.keys():
            if my_dict[key] == '#':
                if adjacent_dict[key].count('#') in [2,3]:
                    my_dict[key] = '#'
                else:
                    my_dict[key] = '.'
            else:
                if adjacent_dict[key].count('#') == 3:
                    my_dict[key] = '#'
                else:
                    my_dict[key] = '.'
    return list(my_dict.values()).count('#')

def day17pt2(x, cycles=6):
    grid = [list(i.strip()) for i in x]

    active = []                
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '#':
                active.append((x,y,0,0))
    
    for i in range(cycles):
        neighbours = {}
        new = {a:0 for a in active}
        for a in active:
            x,y,z,w = a
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    for k in [-1,0,1]:
                        for l in [-1,0,1]:
                            if (i,j,k,l) != (0,0,0,0):
                                if (x+i,y+j,z+k,w+l) in active:
                                    new[a] += 1
                                else:
                                    try:
                                        neighbours[(x+i,y+j,z+k,w+l)] += 1
                                    except:
                                        neighbours[(x+i,y+j,z+k,w+l)] = 1
        # If a cube is active and exactly 2 or 3 of its neighbors are also active, 
        # the cube remains active. Otherwise, the cube becomes inactive.
        # If a cube is inactive but exactly 3 of its neighbors are active, 
        # the cube becomes active. Otherwise, the cube remains inactive.   
        active = []
        for key, value in neighbours.items():
            if value == 3:
                active.append(key)
        
        for key, value in new.items():
            if value in [2,3]:
                active.append(key)        
    return len(active)             
                            

                
        

def addAdditionalPointsPt1(my_dict):
    keys = list(my_dict.keys())
    for key in keys:
        x,y,z = key
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                for k in [-1,0,1]:
                    if (x+i, y+j, z+k) not in keys:
                        my_dict[(x+i, y+j, z+k)] = '.'
    return my_dict         


def getAdjacentPointsPt1(key, my_dict):
    adjacent = []
    x,y,z = key
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            for k in [-1,0,1]:
                if (x+i, y+j, z+k) in my_dict.keys() and not (i==0 and j==0 and k==0):
                    adjacent.append(my_dict[(x+i, y+j, z+k)])
    return adjacent         

if __name__ == "__main__":
    text_file = open("day17/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    #print(day17pt1(x))
    print(day17pt2(x))
