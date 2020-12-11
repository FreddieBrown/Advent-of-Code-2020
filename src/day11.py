def p1(data):
    change = 1
    while change != 0:
        change, data = p1_fuel(data)

    occupied = 0
    for line in data:
        for seat in line:
            if seat == '#':
                occupied += 1

    return occupied


def p1_fuel(data):
    change = 0
    new_plan = []
    # rows
    for i in range(0, len(data)):
        line = []
        for j in range(0, len(data[i])):
            # seat conditions
            if data[i][j] == 'L' and adjacent(data, i, j) == 0:
                line.append("#")
                change += 1
            elif data[i][j] == '#' and adjacent(data, i, j) >= 4:
                line.append("L")
                change += 1
            else:
                line.append(data[i][j])

        new_plan.append(line)

    return change, new_plan


def adjacent(data, y, x):
    points = [(y+1, x), (y-1, x), (y, x+1), (y, x-1),
              (y+1, x+1), (y+1, x-1), (y-1, x+1), (y-1, x-1)]
    full_seats = 0
    for point in points:
        if point[0] < 0 or point[0] >= len(data) or point[1] < 0 or point[1] >= len(data[0]):
            continue
        elif data[point[0]][point[1]] == '#':
            full_seats += 1
    return full_seats


def p2(data):
    change = 1
    while change != 0:
        change, data = p2_fuel(data)

    occupied = 0
    for line in data:
        for seat in line:
            if seat == '#':
                occupied += 1

    return occupied


def p2_fuel(data):
    change = 0
    new_plan = []
    # rows
    for i in range(0, len(data)):
        line = []
        for j in range(0, len(data[i])):
            # seat conditions
            if data[i][j] == 'L' and new_adjacent(data, i, j) == 0:
                line.append("#")
                change += 1
            elif data[i][j] == '#' and new_adjacent(data, i, j) >= 5:
                line.append("L")
                change += 1
            else:
                line.append(data[i][j])

        new_plan.append(line)

    return change, new_plan


def new_adjacent(data, y, x):
    points = [(1, 0), (-1, 0), (0, +1), (0, 0-1),
              (+1, +1), (+1, -1), (-1, +1), (-1, -1)]
    full_seats = 0
    for point in points:
        i = 1
        while True:
            if y+(point[0]*i) < 0 or y+(point[0]*i) >= len(data) or x+(point[1]*i) < 0 or x+(point[1]*i) >= len(data[0]):
                break
            elif data[y+(point[0]*i)][x+(point[1]*i)] == 'L':
                break
            elif data[y+(point[0]*i)][x+(point[1]*i)] == '#':
                full_seats += 1
                break
            i += 1
    return full_seats


data = open('data/day11.txt', 'r').read().split("\n")
data = [list(x) for x in data]

print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
