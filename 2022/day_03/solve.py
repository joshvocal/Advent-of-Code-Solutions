import sys
from itertools import islice


class Solution:
    def part1(self, lines):
        priority_sum = 0

        for line in lines:

            size = len(line)
            first, second = set(line[:size//2]), set(line[size//2:])

            for char in first:
                if char in second:
                    if char.isupper():
                        priority_sum += ord(char) - ord('A') + 27
                    else:
                        priority_sum += ord(char) - ord('a') + 1

                    second.remove(char)

        return priority_sum

    def part2(self, lines):
        return None


def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()
        aa = [line for line in f][:3]

        print(aa)

        sol_1 = Solution()

        print("Part 1: ", sol_1.part1(lines))
        print("Part 2: ", sol_1.part2(lines))


if __name__ == "__main__":
    main(sys.argv[1])
