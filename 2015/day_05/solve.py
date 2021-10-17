
def part1(lines):
    def filter_vowels(letters):
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0

        for char in letters:
            if char in vowels:
                count += 1

        return count >= 3

    def filter_substring(letters):
        banned = ["ab", "cd", "pq", "xy"]

        for banned_str in banned:
            if banned_str in letters:
                return False

        return True

    def filter_repeated_char(letters):
        repeated = [i + j for i, j in zip(letters, letters[1:]) if i == j]

        if len(repeated) > 0:
            return True

        return False

    nice_string_count = 0

    for line in lines:
        filtered_vowels = filter_vowels(line)
        filtered_substring = filter_substring(line)
        filtered_repeated = filter_repeated_char(line)

        if filtered_vowels and filtered_substring and filtered_repeated:
            nice_string_count += 1

    return nice_string_count

def part2(lines):
    return

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    print(part1(lines))
