def part1(lines):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]

    for line in lines:
        instruction, from_coords, _, dest_coords = line.strip().rsplit(' ', 3)
        from_coords = [int(coord) for coord in from_coords.split(',')]
        dest_coords = [int(coord) for coord in dest_coords.split(',')]

        for x_coord in range(from_coords[0], dest_coords[0] + 1):
            for y_coord in range(from_coords[1], dest_coords[1] + 1):
                light = grid[x_coord][y_coord]

                if instruction == "turn on":
                    if not light:
                        grid[x_coord][y_coord] = 1
                elif instruction == "turn off":
                    if light:
                        grid[x_coord][y_coord] = 0
                else:
                    if light:
                        grid[x_coord][y_coord] = 0
                    else:
                        grid[x_coord][y_coord] = 1

    num_lights = 0

    for row in grid:
        for col in row:
            if col == 1:
                num_lights += 1

    return num_lights

def part2(lines):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    brightness = 0

    for line in lines:
        instruction, from_coords, _, dest_coords = line.strip().rsplit(' ', 3)
        from_coords = [int(coord) for coord in from_coords.split(',')]
        dest_coords = [int(coord) for coord in dest_coords.split(',')]

        for x_coord in range(from_coords[0], dest_coords[0] + 1):
                for y_coord in range(from_coords[1], dest_coords[1] + 1):
                    if instruction == "turn on":
                        grid[x_coord][y_coord] += 1
                    elif instruction == "turn off":
                        if grid[x_coord][y_coord] > 0:
                            grid[x_coord][y_coord] -= 1
                    else:
                        grid[x_coord][y_coord] += 2

    for row in grid:
        for col in row:
            brightness += col

    return brightness

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    print(part1(lines))
    print(part2(lines))