import re


def clean(x): return x.strip()


def p1(data):
    bag_types = {}
    for line in data:
        regex = re.compile('[^a-zA-Z ]')
        line = regex.sub('', line).replace("contain", "").split("bag")
        line = list(map(clean, line))
        line.pop()
        main = line[0]
        if main in bag_types.keys():
            bag_types[main] = bag_types[main].union(set(line[1:]))
        else:
            bag_types[main] = set(line[1:])
        for i in range(1, len(line)):
            if line[i] not in bag_types.keys():
                bag_types[line[i]] = set([])
    gold_bags = p1_finder(bag_types, "shiny gold")
    return len(gold_bags)


def p1_finder(types, type):
    gold_bags = set([])
    for key, value in types.items():
        if type in value:
            gold_bags.add(key)
            gold_bags = gold_bags.union(p1_finder(types, key))
    return gold_bags


def p2(data):
    bag_types = {}
    for line in data:
        regex = re.compile('[^a-zA-Z1-9 ]')
        line = regex.sub('', line).replace(
            "contain", "").replace("no other", "").split("bag")
        line = list(map(clean, line))
        line.pop()
        main = line[0]
        if main in bag_types.keys():
            bag_types[main] = bag_types[main].union(set(line[1:]))
        else:
            bag_types[main] = set(line[1:])
    total_bags = p2_finder(bag_types, "shiny gold")
    return total_bags
    # return 1


def p2_finder(types, type):
    total = 0
    regex = re.compile('[^a-zA-Z ]')
    values = types[type]
    for bags in values:
        if bags != '':
            amt = [int(s) for s in bags.split() if s.isdigit()][0]
            clean = regex.sub("", bags).strip()
            inside_bags = p2_finder(types, clean)
            if inside_bags > 1:
                total += amt
            total += inside_bags * amt
    if total == 0:
        total = 1
    return total


data = open('data/day7.txt', 'r').read().replace("bags", "bag").split("\n")


print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
