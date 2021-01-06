def day11pt1(x):
    seating_plan = [list(i.strip()) for i in x]
    unchanged = False
    while not unchanged:
        seating_plan, unchanged = rules(seating_plan)
    return sum([row.count('#') for row in seating_plan])

def rules(seating_plan):
    new_seating_plan = [['.' for j in range(len(seating_plan[0]))] for i in range(len(seating_plan))]
    unchanged = True
    for i in range(len(seating_plan)):
        for j in range(len(seating_plan[0])):
            adjacent = getAdjacentSeats(i,j,seating_plan)
            if seating_plan[i][j] == 'L' and '#' not in adjacent:
                new_seating_plan[i][j] = '#'
                unchanged = False
            elif seating_plan[i][j] == '#' and adjacent.count('#') >= 4:
                new_seating_plan[i][j] = 'L'
                unchanged = False
            else:
                new_seating_plan[i][j] = seating_plan[i][j]
    return new_seating_plan, unchanged

def day11pt2(x):
    seating_plan = [list(i.strip()) for i in x]
    unchanged = False
    while not unchanged:
        seating_plan, unchanged = rules2(seating_plan)
    return sum([row.count('#') for row in seating_plan])

def rules2(seating_plan):
    new_seating_plan = [['.' for j in range(len(seating_plan[0]))] for i in range(len(seating_plan))]
    unchanged = True
    for i in range(len(seating_plan)):
        for j in range(len(seating_plan[0])):
            adjacent = getVisibleSeats(i,j,seating_plan)
            if seating_plan[i][j] == 'L' and '#' not in adjacent:
                new_seating_plan[i][j] = '#'
                unchanged = False
            elif seating_plan[i][j] == '#' and adjacent.count('#') >= 5:
                new_seating_plan[i][j] = 'L'
                unchanged = False
            else:
                new_seating_plan[i][j] = seating_plan[i][j]
    return new_seating_plan, unchanged

def getVisibleSeats(i,j,seating_plan):
    # get vertical
    adjacent = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if x == 0 and y == 0:
                continue
            p = i + x
            q = j + y
            while p in range(len(seating_plan)) and q in range(len(seating_plan[0])):
                if seating_plan[p][q] != '.':
                    adjacent.append(seating_plan[p][q])
                    break
                p += x
                q += y
    return adjacent


def getAdjacentSeats(i,j,seating_plan):
    adjacent = []
    for p in range(i-1,i+2):
        if p in range(len(seating_plan)):
            for q in range(j-1, j+2):
                  if q in range(len(seating_plan[0])):
                      if not (p == i and q == j):
                        adjacent.append(seating_plan[p][q])
    return adjacent


if __name__ == "__main__":
    text_file = open("day11/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day11pt1(x))
    print(day11pt2(x))
