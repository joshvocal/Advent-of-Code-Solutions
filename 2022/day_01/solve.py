import sys
import heapq


class Solution:
    def part1(self, calories):
        max_calories = float("-inf")
        calorie_sum = 0

        for calorie in calories:
            if calorie == "":
                calorie_sum = 0
            else:
                calorie_sum += int(calorie)
                max_calories = max(max_calories, calorie_sum)

        return max_calories

    def part2(self, calories):
        elves = []
        calorie_sum = 0

        for calorie in calories:
            if calorie == "":
                elves.append(-int(calorie_sum))
                calorie_sum = 0
            else:
                calorie_sum += int(calorie)

        if calorie_sum != 0:
            elves.append(-int(calorie_sum))
            calorie_sum = 0

        result = 0
        heapq.heapify(elves)

        for i in range(3):
            elf = heapq.heappop(elves)
            result += elf

        return abs(result)


def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print(sol_1.part1(lines))
        print(sol_1.part2(lines))


if __name__ == "__main__":
    main(sys.argv[1])
