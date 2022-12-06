from re import match, split, MULTILINE
from utils.io import read

input = read()

colunn_label_regex = r"^(?:\s*(\d+)+\s*)+$"
movement_regex = r"move (?P<n>\d+) from (?P<source>\d+) to (?P<target>\d+)"

# [x] [x] [x] [x] [x] [x] [x] [x] [x]
# 0123456789
# fixed width, every fourth is contents

def initialize():
    initial_configuration, columns, instructions = split(colunn_label_regex, input, maxsplit=1, flags=MULTILINE)
    columns = int(columns)
    instructions = instructions.strip()

    stacks = [[] for _ in range(columns)]

    for line in initial_configuration.splitlines():
        contents = line[1::4]
        for i in range(columns):
            crate = contents[i].strip()
            if crate:
                stacks[i].append(crate)

    for stack in stacks:
        stack.reverse()

    return stacks, instructions

def solve(stacks, instructions, move_multiple=False):
    for line in instructions.splitlines():
        m = match(movement_regex, line)
        if m:
            n = int(m.group("n"))
            source = int(m.group("source")) - 1
            target = int(m.group("target")) - 1

            if move_multiple:
                stacks[target].extend(stacks[source][-n:])
                del stacks[source][-n:]
            else:
                for _ in range(n):
                    stacks[target].append(stacks[source].pop())

    answer = ""
    for stack in stacks:
        answer += stack.pop()

    return answer

stacks, instructions = initialize()
print(solve(stacks, instructions))

stacks, instructions = initialize()
print(solve(stacks, instructions, True))
