def elves_game(data, finish):
    numbers = dict()
    next = len(data)+1
    last = data.pop()
    for i, e in enumerate(data):
        numbers[e] = i+1

    while next != finish+1:
        spoken = 0
        if last in numbers:
            spoken = next-1 - numbers[last]
        numbers[last] = next-1
        last = spoken
        next += 1

    return last


def p1(data):
    put_in = [x for x in data]
    return elves_game(put_in, 2020)


def p2(data):
    put_in = [x for x in data]
    return elves_game(put_in, 30000000)


data = open('data/day15.txt', 'r').read().split(",")
data = [int(x) for x in data]

print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
