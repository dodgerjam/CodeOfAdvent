import itertools
from functools import reduce
import itertools
import numpy as np


def day20pt1(x):
    my_dict = {}
    for row in x:
        if "Tile" in row:
            key = int(row[5:-2])
            data = []
        elif row == "\n":
            my_dict[key] = data
        else:
            data.append(list(row.strip()))
    my_dict[key] = data

    for key, value in my_dict.items():
        my_dict[key] = getEdges(value)
    
    aligned_dict = {key:set() for key in my_dict.keys()}
    for pair in itertools.permutations(my_dict.keys(), 2):
        tile1 = pair[0]
        tile2 = pair[1]
        if len([x for x in my_dict[tile1] if x in my_dict[tile2]]) != 0:
            aligned_dict[tile1].add(tile2)
            aligned_dict[tile2].add(tile1)
    
    corners = [key for key,value in aligned_dict.items() if len(value)==2]
    print(len(corners))
    return reduce(lambda x, y: x * y, corners)

def getTransformations(value):
    possible_values = []
    value = np.array([[int(i=='#') for i in row] for row in value])
    for i in range(4):
        possible_values.append(np.rot90(value, k=i))
        possible_values.append(np.rot90(np.fliplr(value), k=i))
    shape = possible_values[0].shape
    assert len(possible_values) == 8
    return possible_values

def day20pt2(x):
    my_dict = {}
    for row in x:
        if "Tile" in row:
            key = int(row[5:-2])
            data = []
        elif row == "\n":
            my_dict[key] = getTransformations(data)
        else:
            data.append(list(row.strip()))
    my_dict[key] = getTransformations(data)

    aligned_dict = getAlignedDict(my_dict)

    key_grid, perm_grid = solveJigsaw(aligned_dict, my_dict)

    tile_size = my_dict[key_grid[0,0]][0].shape
    
    full_jigsaw = formFullJigsaw(key_grid, perm_grid, my_dict)

    return countRoughWaters(full_jigsaw)

def countRoughWaters(full_jigsaw):
    pattern = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1], 
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]])
    count = 0

    jigsaw = full_jigsaw.copy()
    for flip in range(2):
        jigsaw = np.fliplr(jigsaw)
        for rot in range(4):
            jigsaw = np.rot90(jigsaw)
            for i in range(jigsaw.shape[0]-pattern.shape[0]):
                for j in range(jigsaw.shape[1]-pattern.shape[1]):        
                    subgrid = jigsaw[i:i+pattern.shape[0],j:j+pattern.shape[1]]
                    if findSeaMonster(subgrid):
                        for x,y in np.argwhere(pattern == 1):
                            jigsaw[x+i, y+j] = 2
    return len(np.where(jigsaw==1)[0])


def testFullJigsaw(full_jigsaw):
    text_file = open("day20/fulljigsaw.txt", "r")
    x = text_file.readlines()
    text_file.close()
    data = []
    for row in x:
        data.append(list(row.strip()))
    test_jigsaw = np.array([[int(i=='#') for i in row] for row in data])
    return any([np.array_equal(test_jigsaw, jigsaw) for jigsaw in getTransformations(full_jigsaw, convert=False)])

def findSeaMonster(subgrid):
    pattern = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1], 
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]])
    assert subgrid.shape == pattern.shape
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i,j] == 1 and int(subgrid[i,j]) not in [1,2]:
                return False
    return True

def getTransformations(value, convert = True):
    possible_values = []
    if convert:
        value = np.array([[int(i=='#') for i in row] for row in value])
    for i in range(4):
        possible_values.append(np.rot90(value, k=i))
        possible_values.append(np.rot90(np.fliplr(value), k=i))
    shape = possible_values[0].shape
    return possible_values

def formFullJigsaw(key_grid, perm_grid, my_dict):
    
    tile_size = my_dict[key_grid[0,0]][0].shape
    
    full_size = (tile_size[0]-2)*key_grid.shape[0]
    full_jigsaw = np.zeros((full_size, full_size))
    for i in range(key_grid.shape[0]):
        for j in range(key_grid.shape[1]):
            key = int(key_grid[i,j])
            perm = int(perm_grid[i,j])
            full_jigsaw[8*i:8*i+8, 8*j:8*j+8] = my_dict[key][perm][1:-1,1:-1]
    
    return full_jigsaw


def solveJigsaw(aligned_dict, my_dict):
    for key, value in aligned_dict.items():
        if len(value['Below'])==4 and len(value['Right'])==4:
            corner = key

    perm = set([i[0] for i in aligned_dict[corner]['Right']]).intersection(set([i[0] for i in aligned_dict[corner]['Below']])).pop()

    side_length = int(len(my_dict)**0.5)
    
    key_grid = np.zeros((side_length, side_length))
    perm_grid = np.zeros((side_length, side_length))

    key_grid[0,0] = corner
    perm_grid[0,0] = perm
    # ith row, j column
    for i in range(side_length):
        if i == 0:
            j_start = 1
        else:
            j_start = 0

        for j in range(j_start, side_length):
            if j!=0:
                key = key_grid[i,j-1]
                perm = perm_grid[i,j-1]
                perm, right_key, right_perm = [k for k in aligned_dict[key]['Right'] if k[0]==perm].pop()
                key_grid[i,j] = right_key
                perm_grid[i,j] = right_perm
            elif i!=0:
                key = key_grid[i-1,j]
                perm = perm_grid[i-1,j]
                perm, below_key, below_perm = [k for k in aligned_dict[key]['Below'] if k[0]==perm].pop()
                key_grid[i,j] = below_key
                perm_grid[i,j] = below_perm



    return key_grid, perm_grid

def getAlignedDict(my_dict):
    aligned_dict = {k:{'Left':[], 'Right':[], 'Above':[], 'Below':[]} for k in my_dict.keys()}
    print(len(list(itertools.combinations(my_dict.keys(), 2))))
    for key_pair in itertools.combinations(my_dict.keys(), 2):
        #print(key_pair)
        values1 = my_dict[key_pair[0]]
        values2 = my_dict[key_pair[1]]
        #print(len(list(itertools.product(range(len(values1)), range(len(values2))))))
        for grid_pair in itertools.product(range(len(values1)), range(len(values2))):
            gp_index1, gp_index2 = grid_pair

            gp1 = values1[gp_index1]
            gp2 = values2[gp_index2]

            if checkAbove(gp1, gp2):
               aligned_dict[key_pair[0]]['Below'].append((gp_index1, key_pair[1], gp_index2))
               aligned_dict[key_pair[1]]['Above'].append((gp_index2, key_pair[0], gp_index1))
            if checkBelow(gp1, gp2):
               aligned_dict[key_pair[0]]['Above'].append((gp_index1, key_pair[1],gp_index2))
               aligned_dict[key_pair[1]]['Below'].append((gp_index2, key_pair[0], gp_index1))
            if checkLeft(gp1, gp2):
               aligned_dict[key_pair[0]]['Right'].append((gp_index1, key_pair[1], gp_index2))
               aligned_dict[key_pair[1]]['Left'].append((gp_index2, key_pair[0], gp_index1))
            if checkRight(gp1, gp2):
               aligned_dict[key_pair[0]]['Left'].append((gp_index1, key_pair[1], gp_index2))
               aligned_dict[key_pair[1]]['Right'].append((gp_index2, key_pair[0], gp_index1))

    return aligned_dict

def checkLeft(gp1, gp2):
    # Checks if GP1 is left of GP2
    return (gp1[:,-1]==gp2[:,0]).all()

def checkRight(gp1, gp2):
    # Checks if GP1 is right of GP2
    return (gp1[:,0]==gp2[:,-1]).all()

def checkAbove(gp1, gp2):
    # Checks if GP1 is above of GP2
    return (gp1[-1,:] == gp2[0,:]).all()

def checkBelow(gp1, gp2):
    # Checks if GP1 is above of GP2
    return (gp1[0,:] == gp2[-1,:]).all()


def getEdges(value):
    top = ''.join(value[0])
    bottom = ''.join(value[-1])
    left = ''.join([row[0] for row in value])
    right = ''.join([row[-1] for row in value])
    return [top, top[::-1], left, left[::-1], bottom, bottom[::-1], right, right[::-1]]


if __name__ == "__main__":
    text_file = open("day20/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day20pt1(x))
    print(day20pt2(x))