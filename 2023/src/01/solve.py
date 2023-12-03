import re
import sys

number_table = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


class Solution:
    def part1(self, documents: list[str]) -> int:
        def calibrate(document: str) -> int:
            start: int = 0
            end: int = len(document) - 1

            firstDigit: str = document[start]
            lastDigit: str = document[end]

            while not firstDigit.isdigit():
                start += 1
                firstDigit = document[start]

            while not lastDigit.isdigit():
                end -= 1
                lastDigit = document[end]

            return int(firstDigit + lastDigit)

        return sum(map(calibrate, documents))

    def part2(self, documents: list[str]) -> int:
        def get_first_index(string: str, substring: str) -> int:
            match = re.search(substring, string)
            return match.start() if match else 999

        def get_last_index(string, substring) -> int:
            match = re.search(substring[::-1], string[::-1])
            return len(string) - match.start() if match else -1

        def calibrate(document: str) -> int:
            start = 0
            end = 0
            first_index = 999
            last_index = -1

            for k, v in number_table.items():
                curr_first_index = get_first_index(document, k)
                curr_last_index = get_last_index(document, k)

                if curr_first_index < first_index:
                    first_index = curr_first_index
                    start = v
                if curr_last_index > last_index:
                    last_index = curr_last_index
                    end = v

            return int(f"{start}{end}")

        return sum(map(calibrate, documents))


def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print(sol_1.part1(lines))
        print(sol_1.part2(lines))


if __name__ == "__main__":
    main(sys.argv[1])
