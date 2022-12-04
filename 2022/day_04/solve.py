import sys


class Solution:
    def part1(self, lines):
        pairs = 0

        for line in lines:
            left, right = line.split(",")
            left_start, left_end = left.split("-")
            right_start, right_end = right.split("-")

            x = range(int(left_start), int(left_end) + 1)
            y = range(int(right_start), int(right_end) + 1)

            z = list(set(x) & set(y))

            if len(z) == len(x) or len(z) == len(y):
                pairs += 1

        return pairs

    def part2(self, lines):
        pairs = 0

        for line in lines:
            left, right = line.split(",")
            left_start, left_end = left.split("-")
            right_start, right_end = right.split("-")

            x = range(int(left_start), int(left_end) + 1)
            y = range(int(right_start), int(right_end) + 1)

            z = list(set(x) & set(y))

            if len(z) > 0:
                pairs += 1

        return pairs


def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print("Part 1: ", sol_1.part1(lines))
        print("Part 2: ", sol_1.part2(lines))


if __name__ == "__main__":
    main(sys.argv[1])
