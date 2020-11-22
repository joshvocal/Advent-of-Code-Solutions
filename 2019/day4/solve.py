def part1(lo, hi):
    l = []

    for i in range(int(lo), int(hi) + 1):
        a = True
        b = False
        for j in range(1, 6):
            if str(i)[j - 1] > str(i)[j]:
                a = False
            if str(i)[j - 1] == str(i)[j] and not b:
                b = True

        if a and b:
            l.append(i)

    return len(l)


def part2(lo, hi):
    return 2

with open('inputs.txt', 'r') as f:
    lines = f.readlines()
    l = lines[0].strip()
    s = l.split('-')
    lo = s[0]
    hi = s[1]

    print(part1(lo, hi))
