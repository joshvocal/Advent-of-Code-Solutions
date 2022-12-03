import sys


class Game:
    def __init__(self, opponent_move, your_move):
        self.opponent_move = opponent_move
        self.your_move = your_move

        self.shape_score = {"A": 1, "X": 1, "B": 2, "Y": 2, "C": 3, "Z": 3}

        self.round_score = {
            "X": {
                "A": 3,
                "B": 0,
                "C": 6,
            },
            "Y": {
                "A": 6,
                "B": 3,
                "C": 0,
            },
            "Z": {
                "A": 0,
                "B": 6,
                "C": 3,
            },
        }

    def get_round_score(self):
        return self.round_score[self.your_move][self.opponent_move]

    def get_shape_score(self):
        return self.shape_score[self.your_move]

    def get_total_score(self):
        return self.shape_score[self.your_move] + self.get_round_score()


class Solution:
    def part1(self, lines):
        """
        A, X = Rock
        B, Y = Paper
        C, Z = Scissors

        # Shape Selected
        1 = Rock
        2 = Paper
        3 = Scissors

        # Outcome of Round
        0 = Loss
        3 = Draw
        6 = Win

        """
        score = 0

        for line in lines:
            opponent, yourself = line.split(" ")
            game = Game(opponent, yourself)
            score += game.get_total_score()

        return score

    def part2(self, lines):
        """
        X = Lose
        Y = Draw
        Z = Win
        """

        score = 0

        secret_strategy = {
            "A": {
                "X": "Z",
                "Y": "X",
                "Z": "Y",
            },
            "B": {
                "X": "X",
                "Y": "Y",
                "Z": "Z",
            },
            "C": {
                "X": "Y",
                "Y": "Z",
                "Z": "X",
            },
        }

        for line in lines:
            opponent, yourself = line.split(" ")
            yourself = secret_strategy[opponent][yourself]
            game = Game(opponent, yourself)
            score += game.get_total_score()

        return score


def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print(sol_1.part1(lines))
        print(sol_1.part2(lines))


if __name__ == "__main__":
    main(sys.argv[1])
