import sys
import heapq


class Solution:
    def part1(self, calories):
        return None
        
    def part2(self, calories):
        return None

def main(textfile):
    with open(textfile, 'r') as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print(sol_1.part1(lines))
        print(sol_1.part2(lines))

if __name__ == "__main__":
    main(sys.argv[1])