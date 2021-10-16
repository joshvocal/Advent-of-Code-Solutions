def part1(lines):
    total_wrapping_paper = 0

    for line in lines:
        dimensions = [int(i) for i in line.split('x')]

        length = dimensions[0]
        width = dimensions[1]
        height = dimensions[2]

        side_1 = length*width
        side_2 = width*height
        side_3 = height*length

        surface_area = 2 * (side_1 + side_2 + side_3)
        smallest_side = min(side_1, side_2, side_3)

        total_wrapping_paper += (surface_area + smallest_side)

    return total_wrapping_paper

def part2(lines):
    total_ribbon_len = 0

    for line in lines:
        dimensions = [int(i) for i in line.split('x')]

        length = dimensions[0]
        width = dimensions[1]
        height = dimensions[2]

        sorted_dimensions = sorted(dimensions)

        wrapped_ribbon = 2 * (sorted_dimensions[0] + sorted_dimensions[1])
        bow_ribbon = length * width * height

        total_ribbon_len += wrapped_ribbon + bow_ribbon

    return total_ribbon_len

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    print(part1(lines))
    print(part2(lines))
