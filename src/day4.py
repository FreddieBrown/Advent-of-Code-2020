import re
categories_no_cid = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
])

categories = set([
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    "cid"
])


def validate(passport):
    count = 0
    keys = passport.keys()
    if 'byr' in keys:
        year = int(passport['byr'])
        if year >= 1920 and year <= 2002:
            count += 1
    else:
        return False
    if 'iyr' in keys:
        year = int(passport['iyr'])
        if year >= 2010 and year <= 2020:
            count += 1
    else:
        return False
    if 'eyr' in keys:
        year = int(passport['eyr'])
        if year >= 2020 and year <= 2030:
            count += 1
    else:
        return False
    if 'hgt' in keys:
        if "cm" in passport["hgt"]:
            hgt = passport["hgt"].strip("cm")
            hgt = int(hgt)
            if hgt >= 150 and hgt <= 193:
                count += 1
            else:
                return False
        elif "in" in passport["hgt"]:
            hgt = passport["hgt"].strip("in")
            hgt = int(hgt)
            if hgt >= 59 and hgt <= 76:
                count += 1
            else:
                return False
        else:
            return False
    else:
        return False
    if 'hcl' in keys:
        if len(passport['hcl']) == 7 and re.search('#[0-9a-f]+', passport['hcl']):
            count += 1
    else:
        return False
    if 'ecl' in keys:
        poss = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if passport['ecl'] in poss:
            count += 1
    else:
        return False
    if 'pid' in keys:
        if len(passport['pid']) == 9:
            count += 1
    else:
        return False
    if count == 7:
        return True
    return False


def p1(data):
    counter = 0
    for line in data:
        line = line.replace(" ", "\n").split("\n")
        passport = {}
        for entry in line:
            splitted = entry.split(":", 1)
            if len(splitted) > 1:
                passport[splitted[0]] = splitted[1]
        print(set(passport.keys()))
        if (set(passport.keys()) == categories_no_cid) or (set(passport.keys()) == categories):
            counter += 1
    return counter


def p2(data):
    counter = 0
    for line in data:
        line = line.replace(" ", "\n").split("\n")
        passport = {}
        for entry in line:
            splitted = entry.split(":", 1)
            if len(splitted) > 1:
                passport[splitted[0]] = splitted[1]
        if validate(passport):
            counter += 1

    return counter


data = open('data/day4.txt', 'r').read().split("\n\n")
print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
