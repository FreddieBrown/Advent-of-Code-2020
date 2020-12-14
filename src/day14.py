def p1(data):
    mem = dict()
    mask = list("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for line in data:
        kvp = line.split(" = ")
        if kvp[0] == "mask":
            mask = list(kvp[1])
        else:
            kvp[1] = int(kvp[1])
            kvp[0] = int(kvp[0].replace("mem", "").replace(
                "[", "").replace("]", ""))
            binary = list('{0:036b}'.format(kvp[1]))
            for i in range(0, 36):
                if mask[i] == 'X':
                    continue
                binary[i] = mask[i]
            mem[kvp[0]] = int("".join(binary), 2)
    return sum(mem.values())


def p2(data):
    mem = dict()
    mask = list("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    for line in data:
        kvp = line.split(" = ")
        if kvp[0] == "mask":
            mask = list(kvp[1])
        else:
            kvp[1] = int(kvp[1])
            kvp[0] = int(kvp[0].replace("mem", "").replace(
                "[", "").replace("]", ""))
            binary = list('{0:036b}'.format(kvp[0]))
            for i in range(0, 36):
                if mask[i] != "0":
                    binary[i] = mask[i]
            address_list = list_mask(binary)
            for address in address_list:
                address = int("".join(address), 2)
                mem[address] = kvp[1]
    return sum(mem.values())


def list_mask(mask):
    mask_copy0 = [x for x in mask]
    mask_copy1 = [x for x in mask]
    for i in range(0, len(mask)):
        if mask[i] == 'X':
            mask_copy0[i] = "0"
            mask_copy1[i] = "1"
            list0 = list_mask(mask_copy0)
            list1 = list_mask(mask_copy1)
            return list0 + list1
    return [mask]


data = open('data/day14.txt', 'r').read().split("\n")

print("Part 1: "+str(p1(data)))
print("Part 2: "+str(p2(data)))
