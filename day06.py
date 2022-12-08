from utils.io import read

input = read()


def find_first_unique_sequence(input, length=4):
    i = length
    while i < len(input):
        if len(set(input[i - length : i])) == length:
            return i
        i += 1


assert find_first_unique_sequence("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
assert find_first_unique_sequence("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
assert find_first_unique_sequence("nppdvjthqldpwncqszvftbrmjlhg") == 6
assert find_first_unique_sequence("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
assert find_first_unique_sequence("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

print(find_first_unique_sequence(input))
print(find_first_unique_sequence(input, 14))
