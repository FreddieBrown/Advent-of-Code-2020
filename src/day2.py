def p1(word, letter):
    counter = 0
    for char in word:
        if char is letter:
            counter+=1
    return counter


def p2(word, letter, upper, lower):
    pos1 = word[lower-1] is letter
    pos2 = word[upper-1] is letter
    return (pos1 and not pos2) or (not pos1 and pos2)

part1 = 0
part2 = 0
with open('data/day2.txt') as f:
    for line in f:
        line = line.strip("\n")
        parts = line.split(" ")
        policy = parts[0].split("-")
        lower = int(policy[0])
        upper = int(policy[1])
        letter = parts[1].strip(":")
        password = list(parts[2])


        valid1 = p1(password, letter)
        if valid1 <= upper and valid1 >= lower:
            part1+=1
        if p2(password, letter, upper, lower):
            part2 += 1


print("Part 1: "+str(part1))
print("Part 2: "+str(part2))



