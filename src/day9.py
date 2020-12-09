def p1(data, size):
    for i in range(size, len(data)):
        flag = True
        window = set(data[i-size:i])
        for elem in window:
            if (data[i] - elem) in window:
                flag = False
        if flag:
            return data[i]
    return 1


def p2(data, target):
    return find_sub(data, target, 5, 0)


def find_sub(data, target, maxi, mini):
    while True:
        window = data[mini:maxi]
        diff = sum(window) - target
        if diff == 0:
            return max(window)+min(window)
        elif diff > 0:
            mini += 1
        else:
            maxi += 1


data = open('data/day9.txt', 'r').read().split("\n")
data = [int(x) for x in data]

part1 = p1(data, 25)
print("Part 1: "+str(part1))
print("Part 2: "+str(p2(data, part1)))
