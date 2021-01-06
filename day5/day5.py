def day5pt1(x):
    return max(map(getSeatID, x))

def day5pt2(x):
    seats = list(map(getSeatID, x))
    min_seat_id = min(seats)
    max_seat_id = max(seats)
    all_seats = range(min_seat_id, max_seat_id)
    return [s for s in all_seats if s not in seats][0]

def getRowID(x):
    return int(x[:7].replace("F", "0").replace("B", "1"), 2)

def getColumnID(x):   
    return int(x[7:].replace("L", "0").replace("R", "1"), 2)

def getSeatID(x):
    return getRowID(x)*8 + getColumnID(x)


    


if __name__ == "__main__":
    text_file = open("day5/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day5pt1(x))
    print(day5pt2(x))