from enum import Enum
import sys

class Solution:
    class Direction(Enum):
        NORTH = (0, 1)
        EAST = (1, 0)
        SOUTH = (0, -1)
        WEST = (-1, 0)

    DIRECTIONS = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]

    def manhattan_sum(self, a, b):
        return tuple(map(sum, zip(a, b)))

    def manhattan_blocks_away(self, coordinate):
        return sum(map(abs, coordinate))

    def scale_coordaintes(self, direction, scaler):
        return tuple(map(lambda axis: axis * scaler, direction))

    def part1(self, instructions):
        direction = 0
        current_coordinates = (0, 0)

        for instruction in instructions:
            turn, steps = instruction

            if turn == 'R':
                direction = (direction + 1) % len(self.DIRECTIONS)
            elif turn == 'L':
                direction = (direction - 1) % len(self.DIRECTIONS)

            coordinates_walked = self.scale_coordaintes(self.DIRECTIONS[direction].value, steps)
            current_coordinates = self.manhattan_sum(coordinates_walked, current_coordinates)

        return self.manhattan_blocks_away(current_coordinates)

    def part2(self, instructions):
        direction = 0
        position = (0, 0)
        visited = set(position)

        for instruction in instructions:
            turn, steps = instruction

            if turn == 'R':
                direction = (direction + 1) % len(self.DIRECTIONS)
            elif turn == 'L':
                direction = (direction - 1) % len(self.DIRECTIONS)

            for _ in range(steps):
                position = self.manhattan_sum(position, self.DIRECTIONS[direction].value)
                if position in visited:
                    return self.manhattan_blocks_away(position)
                visited.add(position)

        return self.manhattan_blocks_away(position)

def main(textfile):
    with open(textfile, 'r') as f:
        instructions = f.readline().split(', ')

        instructions = [(instruction[0], int(instruction[1:])) for instruction in instructions]

        sol_1 = Solution()

        print(sol_1.part1(instructions))
        print(sol_1.part2(instructions))

if __name__ == "__main__":
    main(sys.argv[1])
