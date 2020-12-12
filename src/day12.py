def p1(data):
    vector = [0, 0, 0, 0]
    facing = "E"
    for ins in data:
        direction = ins[0]
        val = int(ins[1:])
        if direction == "F":
            direction = facing
        elif direction == "R" or direction == "L":
            facing = change(facing, val, direction)
            continue

        if direction == "N":
            add_to_vector([val, 0, 0, 0], vector)
        elif direction == "S":
            add_to_vector([0, 0, val, 0], vector)
        elif direction == "E":
            add_to_vector([0, val, 0, 0], vector)
        elif direction == "W":
            add_to_vector([0, 0, 0, val], vector)

    return abs(vector[0]-vector[2]) + abs(vector[1]-vector[3])


def add_to_vector(add, vector):
    for i in range(0, len(add)):
        vector[i] += add[i]


def change(facing, deg, rot):
    vals = {"N": 0, "E": 90, "S": 180, "W": 270}
    if rot == "R":
        new_dir = vals[facing] + deg
    else:
        new_dir = vals[facing] - deg
    if new_dir >= 360:
        new_dir -= 360
    elif new_dir < 0:
        new_dir += 360
    for direction, degs in vals.items():
        if degs == new_dir:
            return direction


def p2(data):
    vector = [0, 0, 0, 0]
    waypoint = [1, 10, 0, 0]
    for ins in data:
        direction = ins[0]
        val = int(ins[1:])
        if direction == "F":
            add_to_vector([x * val for x in waypoint], vector)
        elif direction == "R" or direction == "L":
            waypoint = change_waypoint(waypoint, val, direction)
            continue

        if direction == "N":
            add_to_vector([val, 0, 0, 0], waypoint)
        elif direction == "S":
            add_to_vector([0, 0, val, 0], waypoint)
        elif direction == "E":
            add_to_vector([0, val, 0, 0], waypoint)
        elif direction == "W":
            add_to_vector([0, 0, 0, val], waypoint)
    return abs(vector[0]-vector[2]) + abs(vector[1]-vector[3])


def change_waypoint(waypoint, deg, rot):
    iters = int(deg/90)
    for i in range(0, iters):
        if rot == "R":
            waypoint = [waypoint[3]] + waypoint[:3]
        else:
            waypoint = waypoint[1:] + [waypoint[0]]
    return waypoint


data = open('data/day12.txt', 'r').read().split("\n")

print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
