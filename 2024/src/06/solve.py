import sys

dirs = [
    (0, 1),   # right
    (0, -1),  # left
    (1, 0),   # down
    (-1, 0)   # up
]

def next_direction(dir):
    match dir:
        case (0, 1):   # right
            return (1, 0)  # down
        case (1, 0):   # down
            return (0, -1) # left
        case (0, -1):  # left
            return (-1, 0) # up
        case (-1, 0):  # up
            return (0, 1)  # right

def direction_word(dir):
    match dir:
        case (0, 1):   # right
            return "right"
        case (1, 0):   # down
            return "down"
        case (0, -1):  # left
            return "left"
        case (-1, 0):  # up
            return "up"

def get_guard_direction(char):
    match char:
        case "^":
            return (-1, 0)  # up
        case ">":
            return (0, 1)   # right
        case "v":
            return (1, 0)   # down
        case "<":
            return (0, -1)  # left

def walk(guard_coord, guard_direction, grid, visited):
    def is_valid(guard_coord, guard_direction):
        row = guard_coord[0] + guard_direction[0]
        col = guard_coord[1] + guard_direction[1]
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])

    while is_valid(guard_coord, guard_direction):
        print(guard_coord)
        print(direction_word(guard_direction))
        visited.add(guard_coord)

        if grid[guard_coord[0] + guard_direction[0]][guard_coord[1] + guard_direction[1]] == "#":
            guard_direction = next_direction(guard_direction)

        guard_coord = (guard_coord[0] + guard_direction[0], guard_coord[1] + guard_direction[1])

    visited.add(guard_coord)

class Solution:
    def part1(self, grid) -> int:
        guard_direction = (0, 0)
        guard_coord = (0, 0)

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] in ["^", ">", "v", "<"]:
                    guard = grid[row][col]
                    guard_direction = get_guard_direction(guard)
                    guard_coord = (row, col)
                    break

        walk(guard_coord, guard_direction, grid, visited)

        return len(visited)

    def part2(self, lines: list[str]) -> int:
        return 2

def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        grid = lines

        sol = Solution()

        print(sol.part1(grid))
        print(sol.part2(grid))

if __name__ == "__main__":
    main(sys.argv[1])
