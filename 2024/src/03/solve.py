import sys

class Solution:
    def part1(self, line: str) -> int:
        stack = []
        inner = ""
        res = 0

        for index, char in enumerate(line):
            stack.append(char)

            if ''.join(stack) == "mul(" and (index + 1) < len(line) - 1:
                ahead = 1
                while line[index + ahead] != ")":
                    inner += line[index + ahead]
                    ahead += 1 

                nums = inner.split(",")

                if len(nums) == 2:
                    first = nums[0]
                    second = nums[1]

                    both_numeric = first.isnumeric() and second.isnumeric()
                    both_under_3 = len(first) <= 3 and len(second) <= 3

                    if both_numeric and both_under_3:
                        res += int(nums[0]) * int(nums[1])

                inner = ""

            if len(stack) > 3:
                stack.pop(0)

        return res

    def part2(self, line: str) -> int:
        stack = []
        inner = ""
        res = 0
        enabled = True

        for index, char in enumerate(line):
            stack.append(char)

            if "do()" in ''.join(stack):
                enabled = True
                stack = []
            elif "don't()" in ''.join(stack):
                enabled = False
                stack = []

            if enabled and "mul(" in ''.join(stack) and (index + 1) < len(line) - 1:
                ahead = 1
                while line[index + ahead] != ")":
                    inner += line[index + ahead]
                    ahead += 1 

                nums = inner.split(",")

                if len(nums) == 2:
                    first = nums[0]
                    second = nums[1]

                    both_numeric = first.isnumeric() and second.isnumeric()
                    both_under_3 = len(first) <= 3 and len(second) <= 3

                    if both_numeric and both_under_3:
                        res += int(nums[0]) * int(nums[1])

                inner = ""
                stack = []

            if len(stack) > 6:
                stack.pop(0)

        return res

def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol = Solution()

        print("Part 1:")
        print(sol.part1(''.join(lines)))
        print("Part 2:")
        print(sol.part2(''.join(lines)))

if __name__ == "__main__":
    main(sys.argv[1])
