def calc(f):
    return f // 3 - 2

def part1(m):
    total = 0

    for f in m:
        total += calc(f)

    return total

def part2(m):
    total = 0

    for f in m:
        while calc(f) > 0:
            f = calc(f)
            total += f

    return total

with open('inputs.txt', 'r') as f:
    lines = f.readlines()
    modules = [int(f.strip()) for f in lines]

    print(part1(modules))
    print(part2(modules))
