from utils.io import read

elves = read().split('\n\n')

calories = []
for elf in elves:
    items = elf.splitlines()
    total = 0
    for item in items:
        total += int(item)
    calories.append(total)

top_3 = sorted(calories)[-3:]

print(top_3[-1])
print(sum(top_3))