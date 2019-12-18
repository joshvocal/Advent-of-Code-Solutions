def part1(w1, w2):

    def helper(ww):
        x = 0
        y = 0
        s = set()

        for w in ww:
            a = w[0]
            b = int(w[1:])

            if a == 'U':
                for i in range(b):
                    y += 1
                    s.add((x, y))
            elif a == 'D':
                for i in range(b):
                    y -= 1
                    s.add((x, y))
            elif a == 'L':
                for i in range(b):
                    x -= 1
                    s.add((x, y))
            elif a == 'R':
                for i in range(b):
                    x += 1
                    s.add((x, y))

        return s

    s1 = helper(w1)
    s2 = helper(w2)
    j = [i for i in s1 if i in s2]

    l = []
    for i in j:
        a = abs(i[0])
        b = abs(i[1])
        l.append(a + b)

    return min(l)

with open('inputs.txt', 'r') as f:
    lines = f.readlines()
    w1 = lines[0].strip().split(',')
    w2 = lines[1].strip().split(',')

    print(part1(w1, w2))

