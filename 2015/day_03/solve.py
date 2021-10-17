def part1(line):
    seen_houses = set()
    x = 0
    y = 0

    seen_houses.add((x, y))

    for char in line:
        if char == '^':
            y += 1
        elif char == 'v':
            y -= 1
        elif char == '>':
            x += 1
        elif char == '<':
            x -= 1

        seen_houses.add((x, y))

    return len(seen_houses)

def part2(line):
    santa_houses = set()
    robot_houses = set()

    s_x = 0
    s_y = 0
    r_x = 0
    r_y = 0

    santa_houses.add((0, 0))
    robot_houses.add((0, 0))

    for index, char in enumerate(line):
        if index % 2 == 0:
            if char == '^':
                s_y += 1
            elif char == 'v':
                s_y -= 1
            elif char == '>':
                s_x += 1
            elif char == '<':
                s_x -= 1

            santa_houses.add((s_x, s_y))
        else:
            if char == '^':
                r_y += 1
            elif char == 'v':
                r_y -= 1
            elif char == '>':
                r_x += 1
            elif char == '<':
                r_x -= 1

            robot_houses.add((r_x, r_y))

    return len(robot_houses.union(santa_houses))

with open('input.txt', 'r') as f:
    line = f.readline()

    print(part1(line))
    print(part2(line))
