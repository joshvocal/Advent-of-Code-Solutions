import sys


class Solution:
    def part1(self, lines):
        return None

    def part2(self, lines):
        return None


def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print("Part 1: ", sol_1.part1(lines))
        print("Part 2: ", sol_1.part2(lines))


if __name__ == "__main__":
    main(sys.argv[1])
