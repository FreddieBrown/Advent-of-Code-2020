in_list = []
seen = set()

with open('../data/day1.txt') as f:
    for line in f:
        in_list.append(int(line))


print("Part 1")
for item in in_list:
    for elem in seen:
        if item + elem == 2020:
            print(str(item * elem))
    seen.add(item)

print("Part 2")
for item in in_list:
    for i in seen:
        for j in seen:
            if item + i + j == 2020: 
                print(str(item * i * j))
    seen.add(item)

