def changep1(active):
    counter = dict()
    for key in active:
        for x in [0, 1, -1]:
            for y in [0, 1, -1]:
                for z in [0, 1, -1]:
                    if x == 0 and y == 0 and z == 0:
                        continue
                    evaluate = (key[0]+x, key[1]+y, key[2]+z)
                    if evaluate not in counter:
                        counter[evaluate] = 1
                    else:
                        counter[evaluate] += 1

    new_active = []
    for key, value in counter.items():
        if key in active and (value == 2 or value == 3):
            new_active.append(key)
        elif key not in active and (value == 3):
            new_active.append(key)
    return new_active


def changep2(active):
    counter = dict()
    for key in active:
        for x in [0, 1, -1]:
            for y in [0, 1, -1]:
                for z in [0, 1, -1]:
                    for w in [0, 1, -1]:
                        if x == 0 and y == 0 and z == 0 and w == 0:
                            continue
                        evaluate = (key[0]+x, key[1]+y, key[2]+z, key[3]+w)
                        if evaluate not in counter:
                            counter[evaluate] = 1
                        else:
                            counter[evaluate] += 1

    new_active = []
    for key, value in counter.items():
        if key in active and (value == 2 or value == 3):
            new_active.append(key)
        elif key not in active and (value == 3):
            new_active.append(key)
    return new_active


def p1(data):
    active = []
    for i in range(len(data)):
        data[i] = list(data[i])
        for j in range(len(data[i])):
            if data[i][j] == "#":
                active.append((i, j, 0))
    for i in range(6):
        active = changep1(active)

    return len(active)


def p2(data):
    active = []
    for i in range(len(data)):
        data[i] = list(data[i])
        for j in range(len(data[i])):
            if data[i][j] == "#":
                active.append((i, j, 0, 0))
    for i in range(6):
        active = changep2(active)
    return len(active)


data = open('data/day17.txt', 'r').read().split("\n")


print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
