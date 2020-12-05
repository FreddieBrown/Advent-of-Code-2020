def p1(data):
    highest = 0
    for line in data:
        id = convert(line)
        if id > highest:
            highest = id
    return highest


def convert(id):
    return int(id, 2)


def p2(data):
    numbered = list(map(convert, data))
    numbered.sort()
    prev = numbered[0]
    for seat_id in numbered:
        new = seat_id
        if new-1 > prev:
            return new-1
        else:
            prev = new

    return 1


data = open('data/day5.txt', 'r').read().replace("B", "1").replace("F",
                                                                   "0").replace("R", "1").replace("L", "0").split("\n")
print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))

# B = 1, F = 0
# R = 1, L = 0
