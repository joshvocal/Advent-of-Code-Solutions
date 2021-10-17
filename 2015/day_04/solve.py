from hashlib import md5

def part1(key, leading_string):
    secret_key_digit = 0

    while True:
        secret_key_string = key + str(secret_key_digit)
        md5_hash = md5(secret_key_string.encode()).hexdigest()

        if md5_hash[:len(leading_string)] == leading_string:
            break
        else:
            secret_key_digit += 1

    return secret_key_digit

with open('input.txt', 'r') as f:
    line = f.readline().strip()

    print(part1(line, '00000'))
    print(part1(line, '000000'))
