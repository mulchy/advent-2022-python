from math import floor
from utils.io import read

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
priorities = { k: v for (v, k) in enumerate(alphabet, 1)}

input = read()

total = 0
for line in input.splitlines():
    mid = floor(len(line)/2)
    first_half = set(line[:mid])
    second_half = set(line[mid:])

    dupe = list(first_half.intersection(second_half))[0] # assume only one dupe
    total += priorities[dupe]

print(total)

total = 0
lines = input.splitlines()

i = 2
while i < len(lines):
    dupe = list(
            set(lines[i-2])
                .intersection(set(lines[i-1]))
                .intersection(set(lines[i]))
    )[0]
    total += priorities[dupe]
    i += 3

print(total)