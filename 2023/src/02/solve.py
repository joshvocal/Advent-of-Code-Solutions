import re
import sys

color_patterns = {
    "red": r"(\d+) red",
    "blue": r"(\d+) blue",
    "green": r"(\d+) green",
}

max_red = 12
max_green = 13
max_blue = 14


class Solution:
    def part1(self, lines: list[str]) -> int:
        game_id_sum = 0

        for line in lines:
            game_id_str, sub_games = [x.strip() for x in line.split(":")]
            match = re.search(r"\d+", game_id_str)
            game_id: int | None = int(match.group()) if match else None
            games = [x.strip() for x in sub_games.split(";")]

            numbers = {}
            is_possible = True

            for game in games:
                # Use regex to find all the color names and the number count associated with them
                for color, pattern in color_patterns.items():
                    matches = re.findall(pattern, game)
                    numbers[color] = sum([int(match) for match in matches])

                if (
                    numbers["red"] > max_red
                    or numbers["green"] > max_green
                    or numbers["blue"] > max_blue
                ):
                    is_possible = False

                numbers = {}

            if game_id and is_possible:
                game_id_sum += game_id

        return game_id_sum

    def part2(self, lines: list[str]) -> int:
        return 0


def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print(sol_1.part1(lines))
        print(sol_1.part2(lines))


if __name__ == "__main__":
    main(sys.argv[1])
