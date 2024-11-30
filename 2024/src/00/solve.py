import sys

class Solution:
    def part1(self, lines: list[str]) -> int:
        return 1

    def part2(self, lines: list[str]) -> int:
        return 2

def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol = Solution()

        print(sol.part1(lines))
        print(sol.part2(lines))

if __name__ == "__main__":
    main(sys.argv[1])
