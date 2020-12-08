def p1(data):
    counter = 0
    executed = set()
    i = 0
    while i < len(data):
        if i in executed:
            return counter
        executed.add(i)
        line = data[i].split(" ")
        val = int(line[1])
        instr = line[0]

        if instr == "acc":
            counter += val
            i += 1
        elif instr == "jmp":
            i += val
        else:
            i += 1
    return counter


def p2(data):
    counter = 0
    executed = set()
    i = 0
    while i < len(data):
        if i in executed:
            print("fail in p2: "+str(i))
            return counter
        executed.add(i)
        line = data[i].split(" ")
        val = int(line[1])
        instr = line[0]
        if instr == "acc":
            counter += val
            i += 1
        elif instr == "jmp":
            try_run = p2_fuel(data, "nop", i)
            if try_run != 0:
                return try_run
            i += val
        else:
            try_run = p2_fuel(data, "jmp", i)
            if try_run != 0:
                return try_run
            i += 1
    return counter


def p2_fuel(data, c_instr, line):
    counter = 0
    executed = set()
    i = 0
    while i < len(data):
        if i in executed:
            return 0
        executed.add(i)
        code = data[i].split(" ")
        val = int(code[1])
        instr = code[0]
        if i == line:
            instr = c_instr
        if instr == "acc":
            counter += val
            i += 1
        elif instr == "jmp":
            i += val
        else:
            i += 1
    return counter


data = open('data/day8.txt', 'r').read().replace("+", "").split("\n")


print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
