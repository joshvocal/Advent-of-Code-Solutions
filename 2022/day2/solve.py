import sys
import heapq

class Game:
    def __init__(self, opponent_move, your_move):
        self.opponent_move = opponent_move
        self.your_move = your_move

    def get_round_score(self):
        score = 0

        if self.your_move == "X" or self.your_move == "A":
            if self.opponent_move == "X" or self.opponent_move == "A":
                score = 3
            elif self.opponent_move == "B" or self.opponent_move == "Y":
                score = 0
            elif self.opponent_move == "C" or self.opponent_move == "Z":
                score = 6
        elif self.your_move == "B" or self.your_move == "Y":
            if self.opponent_move == "A" or self.opponent_move == "X":
                score = 6
            elif self.opponent_move == "B" or self.opponent_move == "Y":
                score = 3
            elif self.opponent_move == "C" or self.opponent_move == "Z":
                score = 0
        elif self.your_move == "C" or self.your_move == "Z":
            if self.opponent_move == "A" or self.opponent_move == "X":
                score = 0
            elif self.opponent_move == "B" or self.opponent_move == "Y":
                score = 6
            elif self.opponent_move == "C" or self.opponent_move == "Z":
                score = 3

        return score

    def get_total_score(self):
        score = 0

        shape_score = {
            'A' : 1,
            'X' : 1,
            'B' : 2,
            'Y' : 2,
            'C' : 3,
            'Z' : 3
        }

        return shape_score[self.your_move] + self.get_round_score()

class Solution:
    def part1(self, lines):
        '''
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

        '''
        score = 0

        for line in lines:
            opponent, yourself = line.split(' ')
            game = Game(opponent, yourself)
            score += game.get_total_score()

        return score
        
    def part2(self, lines):
        return None

def main(textfile):
    with open(textfile, 'r') as f:
        lines = f.read().splitlines()

        sol_1 = Solution()

        print(sol_1.part1(lines))
        print(sol_1.part2(lines))

if __name__ == "__main__":
    main(sys.argv[1])