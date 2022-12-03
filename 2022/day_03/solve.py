import sys


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

        return priority_sum

    def part2(self, lines):
        freq = {}
        priority_sum = 0

        for group in zip(lines, lines, lines):
            for rucksack in group:
                for char in set(rucksack):
                    freq[char] = freq.get(char, 0) + 1

                    if freq[char] == 3:
                        if char.isupper():
                            priority_sum += ord(char) - ord('A') + 27
                        else:
                            priority_sum += ord(char) - ord('a') + 1
            freq = {}

        return priority_sum


def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()
        iter_lines = iter(lines)

        sol_1 = Solution()

        print("Part 1: ", sol_1.part1(lines))
        print("Part 2: ", sol_1.part2(iter_lines))


if __name__ == "__main__":
    main(sys.argv[1])
