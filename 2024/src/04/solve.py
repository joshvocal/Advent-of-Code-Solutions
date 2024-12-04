import sys

dirs = [
    # x, y
    (1, 0), # right
    (-1, 0), # left
    (0, 1), # up
    (0, -1), # down
    (1, 1), # up-right
    (1, -1), # down-right
    (-1, 1), # up-left
    (-1, -1), # down-left
]

def word_search(grid, x, y, dx, dy, rows, cols, target):
    word = ""

    for i in range(len(target)):
        if x < 0 or x >= rows or y < 0 or y >= cols:
            return False

        word += grid[x][y]
        x += dx
        y += dy

    return word == target

class Solution:

    def part1(self, lines: list[str]) -> int:
        grid = lines

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for y in range(rows):
            for x in range(cols):
                for dx, dy in dirs:
                    if word_search(grid, x, y, dx, dy, rows, cols, "XMAS"):
                        count += 1

        return count

    def part2(self, lines: list[str]) -> int:
        grid = lines

        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for y in range(rows - 2):
            for x in range(cols - 2):
                center = grid[x + 1][y + 1]
                top_left = grid[x][y]
                bottom_right = grid[x + 2][y + 2]
                top_right = grid[x + 2][y]
                bottom_left = grid[x][y + 2]

                '''
                 012
                0M.S
                1.A.
                2M.S
                '''

                is_center = center == "A"
                diag1 = (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M")
                diag2 = (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M")

                if is_center and diag1 and diag2:
                    count += 1

        return count

def main(textfile):
    with open(textfile, "r") as f:
        lines = f.read().splitlines()

        sol = Solution()

        print(sol.part1(lines))
        print(sol.part2(lines))

if __name__ == "__main__":
    main(sys.argv[1])
