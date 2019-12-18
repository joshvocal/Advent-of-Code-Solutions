def part1(x):

    for i in range(0, len(x), 4):
        cmd = x[i]
        a = x[i + 1]
        b = x[i + 2]
        p = x[i + 3]


        if cmd == 1:
            x[p] = x[a] + x[b]
        elif cmd == 2:
            x[p] = x[a] * x[b]
        elif cmd == 99:
            return x

    return x

for line in open('inputs.txt', 'r'):
    x = []
    for line in line.strip().split(','):
        x.append(int(line))

    print(part1(x))
