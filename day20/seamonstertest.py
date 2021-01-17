import numpy as np

def findSeaMonster(subgrid):
    pattern = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1], 
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]])
    assert subgrid.shape == pattern.shape
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            if pattern[i,j] == 1 and int(subgrid[i,j])!=1:
                return False
    return True

if __name__ == "__main__":
    text_file = open("day20/seamonster.txt", "r")
    x = text_file.readlines()
    text_file.close()
    data = []
    for row in x:
        data.append(list(row.strip()))
    print(data)
    full_jigsaw = np.array([[int(i=='#' or i=='O') for i in row] for row in data])
    
    pattern = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0], 
                [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1], 
                [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]])

    count = 0
    print(full_jigsaw)
    for i in range(full_jigsaw.shape[0]-pattern.shape[0]):
            for j in range(full_jigsaw.shape[1]-pattern.shape[1]):
                
                subgrid = full_jigsaw[i:i+pattern.shape[0],j:j+pattern.shape[1]]
                if i==2 and j==2:
                    print(i,i+pattern.shape[0],j,j+pattern.shape[1])
                    print(subgrid)
                if findSeaMonster(subgrid):
                    count += 1
    print(count)
