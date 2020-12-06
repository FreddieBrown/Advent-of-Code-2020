def p1(data):
    total = 0
    for group in data:
        group = group.replace("\n", "")
        letters = set(list(group))
        total += len(letters)
    return total


def p2(data):
    count = 0
    for group in data:
        group = group.split("\n")
        total = set(list("abcdefghijklmnopqrstuvwxyz"))
        for person in group:
            letters = set(list(person))
            total = total.intersection(letters)
        count += len(total)
    return count


data = open('data/day6.txt', 'r').read().split("\n\n")
print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
