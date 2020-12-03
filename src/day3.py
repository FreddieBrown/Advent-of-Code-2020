def p1(grid, x_step, y_step):
    x = 0
    y = 0
    max_x = len(grid[0])
    max_y = len(grid)
    trees = 0
    while y < max_y:
        if x >= max_x:
            x = x - max_x
        space = grid[y][x]
        if space == '#':
            trees += 1
        x += x_step
        y += y_step

    return trees


def p2(grid):
    r1 = p1(grid, 1, 1)
    r2 = p1(grid, 3, 1)
    r3 = p1(grid, 5, 1)
    r4 = p1(grid, 7, 1)
    r5 = p1(grid, 1, 2)
    return r1 * r2 * r3 * r4 * r5


def print_grid(grid):
    for y in grid:
        for x in y:
            print(x, end = '')
        print("")

grid = []
with open('data/day3.txt') as f:
    for line in f:
        line = list(line.strip("\n"))
        grid.append(line)

print("Part 1: "+str(p1(grid, 3, 1)))
print("Part 2: "+str(p2(grid)))
