def day12pt1(x):
    position = [0,0]
    angle = 0
    for velocity in x:
        direction = velocity[0]
        distance = int(velocity[1:])
        if direction == 'E':
            position[0] += distance
        elif direction == 'W':
            position[0] -= distance
        elif direction == 'N':
            position[1] += distance
        elif direction == 'S':
            position[1] -= distance
        elif direction == 'R':
            angle -= distance
            angle %= 360
        elif direction == 'L':
            angle += distance
            angle %= 360
        elif direction == 'F':
            if angle == 0:
                position[0] += distance
            elif angle == 90:
                position[1] += distance
            elif angle == 180:
                position[0] -= distance
            elif angle == 270:
                position[1] -= distance
    return abs(position[0]) + abs(position[1])


def day12pt2(x):
    position = [0,0]
    waypoint = [10, 1]
    for velocity in x:
        direction = velocity[0]
        distance = int(velocity[1:])
        if direction == 'E':
            waypoint[0] += distance
        elif direction == 'W':
            waypoint[0] -= distance
        elif direction == 'N':
            waypoint[1] += distance
        elif direction == 'S':
            waypoint[1] -= distance
        elif direction == 'R':
            for i in range(distance//90):
                x = waypoint[0]
                y = waypoint[1]
                waypoint[0] = y
                waypoint[1] = -x
        elif direction == 'L':
            for i in range(distance//90):
                x = waypoint[0]
                y = waypoint[1]
                waypoint[0] = -y
                waypoint[1] = x
        elif direction == 'F':
            x = waypoint[0]
            y = waypoint[1]
            position[0] = (x*distance) + position[0]
            position[1] = (y*distance) + position[1]
        
    return abs(position[0]) + abs(position[1])


if __name__ == "__main__":
    text_file = open("day12/input.txt", "r")
    x = text_file.readlines()
    text_file.close()
    print(day12pt1(x))
    print(day12pt2(x))
