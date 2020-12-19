import re


def build_rules(raw):
    regex = re.compile(r'^[0-9 ]+$')
    rules = {}
    raw = raw.split("\n")
    for rule in raw:
        rule = rule.replace('"', "").split(": ")
        rule[0] = int(rule[0])
        if " | " in rule[1]:
            rule[1] = rule[1].split(" | ")
            for r in rule[1]:
                r = r.split(" ")
                r = [int(x) for x in r]
                if rule[0] not in rules:
                    rules[rule[0]] = [r]
                else:
                    rules[rule[0]].append(r)
        elif regex.match(rule[1]):
            rule[1] = rule[1].split(" ")
            rule[1] = [int(x) for x in rule[1]]
            if rule[0] not in rules:
                rules[rule[0]] = [rule[1]]
            else:
                rules[rule[0]].append(rule[1])
        else:
            rules[rule[0]] = rule[1]
    biggest_key = max(rules.keys())
    for i in range(0, biggest_key+1):
        if i not in rules.keys() or type(rules[i]) is not list:
            continue
        for j in range(0, len(rules[i])):
            while len(rules[i][j]) > 2:
                # create new rule with first 2 elems in supersized rule
                biggest_key += 1
                rules[biggest_key] = [rules[i][j][:2]]
                rules[i][j] = [biggest_key]+rules[i][j][2:]

    return rules


def cyk(data):
    counter = 0
    regex = re.compile(r'^[a-zA-Z]+$')
    rules = build_rules(data[0])
    for input in data[1].split("\n"):
        input = list(input)
        n = len(input)
        r = max(rules.keys())+1
        parse_table = {}

        for i in range(0, n):
            for j in range(0, n):
                for k in range(0, r):
                    parse_table[i, j, k] = False

        for s in range(0, n):
            for key, value in rules.items():
                if type(value) is not list:
                    if value == input[s]:
                        parse_table[0, s, key] = True

        for l in range(1, n):
            for s in range(n - l):
                for p in range(l):
                    for key, value in rules.items():
                        if type(value) is list:
                            for rule in value:
                                if parse_table[p, s, rule[0]] and parse_table[l-p-1, s+p+1, rule[1]]:
                                    parse_table[l, s, key] = True
        if parse_table[n-1, 0, 0]:
            counter += 1

    return counter


print("Part 1: "+str(cyk(open('data/day191.txt', 'r').read().split("\n\n"))))
print("Part 2: "+str(cyk(open('data/day192.txt', 'r').read().split("\n\n"))))
