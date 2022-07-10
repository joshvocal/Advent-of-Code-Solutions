import sys

class Solution:
    def part1(self, lines):
        return

    def part2(self, lines):
        return

def main(textfile):
    with open(textfile, 'r') as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print(sol_1.part1(lines))
        print(sol_1.part2(lines))

if __name__ == "__main__":
    main(sys.argv[1])
