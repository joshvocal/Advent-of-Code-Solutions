from enum import Enum

class Direction(Enum):
    NORTH = (0, 1)
    EAST = (1, 0)
    SOUTH = (0, -1)
    WEST = (-1, 0)

COORDINATES = [Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST]

def part1(instructions):
    direction = 0
    current_coordinates = (0, 0)

    for instruction in instructions:
        turn, steps = instruction

        if turn == 'R':
            direction = (direction + 1) % len(COORDINATES)
        elif turn == 'L':
            direction = (direction - 1) % len(COORDINATES)

        new_coordinates = tuple([axis * steps for axis in COORDINATES[direction].value])
        current_coordinates = tuple(map(sum, zip(new_coordinates, current_coordinates)))

    return sum(map(abs, current_coordinates))

def part2(lines):
    return

with open('input.txt', 'r') as f:
    instructions = f.readline().split(', ')

    instructions = [(instruction[0], int(instruction[1:])) for instruction in instructions]

    print(part1(instructions))
    print(part2(instructions))
