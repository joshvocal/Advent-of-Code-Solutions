from enum import Enum
import sys

class Solution:
    class Direction(Enum):
        NORTH = (0, 1)
        EAST = (1, 0)
        SOUTH = (0, -1)
        WEST = (-1, 0)

    COORDINATES = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]

    def part1(self, instructions):
        direction = 0
        current_coordinates = (0, 0)

        for instruction in instructions:
            turn, steps = instruction

            if turn == 'R':
                direction = (direction + 1) % len(self.COORDINATES)
            elif turn == 'L':
                direction = (direction - 1) % len(self.COORDINATES)

            new_coordinates = tuple([axis * steps for axis in self.COORDINATES[direction].value])
            current_coordinates = tuple(map(sum, zip(new_coordinates, current_coordinates)))

        return sum(map(abs, current_coordinates))

    def part2(self, instructions):
        direction = 0
        position = (0, 0)
        visited = set(position)

        for instruction in instructions:
            turn, steps = instruction

            if turn == 'R':
                direction = (direction + 1) % len(self.COORDINATES)
            elif turn == 'L':
                direction = (direction - 1) % len(self.COORDINATES)

            for _ in range(steps):
                position = tuple(map(sum, zip(position, self.COORDINATES[direction].value)))
                if position in visited:
                    return sum(map(abs, position))
                visited.add(position)

        return sum(map(abs, position))

def main(textfile):
    with open(textfile, 'r') as f:
        instructions = f.readline().split(', ')

        instructions = [(instruction[0], int(instruction[1:])) for instruction in instructions]

        sol_1 = Solution()

        print(sol_1.part1(instructions))
        print(sol_1.part2(instructions))

if __name__ == "__main__":
    main(sys.argv[1])
