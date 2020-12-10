import copy


def p1(data):
    data.sort()
    one_jolt = 0
    three_jolt = 1
    current = 0
    for item in data:
        diff = item - current
        if diff == 1:
            one_jolt += 1
        if diff == 3:
            three_jolt += 1
        current = item
    return one_jolt * three_jolt


def p2(data):
    data.append(0)
    data.sort()
    data.append(max(data)+3)
    arr = [0] * len(data)
    arr[0] = 1
    arr[1] = 1
    arr[2] = 2
    for i in range(3, len(data)):
        if data[i] - data[i - 1] <= 3:
            arr[i] += arr[i - 1]

        if data[i] - data[i - 2] <= 3:
            arr[i] += arr[i - 2]

        if data[i] - data[i - 3] <= 3:
            arr[i] += arr[i - 3]
    return arr[len(arr) - 1]


data = open('data/day10.txt', 'r').read().split("\n")
data = [int(x) for x in data]

print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
