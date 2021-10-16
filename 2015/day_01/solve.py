# Count the number of parenthesis
def part1(line):
    floor = 0

    for char in line:
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

    return floor

# Find the position of the first character that causes the floor count to be negative.
def part2(line):
    floor = 0

    for index, char in enumerate(line):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1

        if floor < 0:
            return index + 1

    return len(line)

with open('input.txt', 'r') as f:
    line = f.readline()

    print(part1(line))
    print(part2(line))

