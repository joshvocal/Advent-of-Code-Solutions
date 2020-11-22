def part1(x, noun = 12, verb = 2):

    x[1] = noun
    x[2] = verb

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
            return x[0]

    return x[0]

def part2(x):
    for noun in range(100):
        for verb in range(100):
            temp = list(x)
            temp[1] = noun 
            temp[2] = verb

            out = part1(temp, noun, verb)

            if out == 19690720: 
                return noun, verb

    return -1, -1

for line in open('inputs.txt', 'r'):
    x = []
    for line in line.strip().split(','):
        x.append(int(line))

    print(part1(list(x)))
    noun, verb = part2(list(x))
    print(100 * noun + verb)
