import sys

class Solution:
    def part1(self, lines: list[str]) -> int:
        first = []
        second = []
        distances = 0

        for line in lines:
            digits = [int(s) for s in line.split() if s.isdigit()]
            first.append(digits[0])
            second.append(digits[1])

        first.sort()
        second.sort()

        for one, two in zip(first, second):
            distances += abs(one - two)

        return distances

    def part2(self, lines: list[str]) -> int:
        first = []
        second = []
        similarity = 0

        for line in lines:
            digits = [int(s) for s in line.split() if s.isdigit()]
            first.append(digits[0])
            second.append(digits[1])

        freq = {key: 0 for key in second}

        for num in second:
            freq[num] += 1

        for num in first:
            if num in freq:
                similarity += (num * freq[num])

        return similarity

def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol = Solution()

        print(sol.part1(lines))
        print(sol.part2(lines))

if __name__ == "__main__":
    main(sys.argv[1])
