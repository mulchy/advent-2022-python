from utils.io import read

count_1 = 0
count_2 = 0
for line in read().splitlines():
    [[start_1, end_1], [start_2, end_2]] = [pair.split("-") for pair in line.split(",")]
    a = set(range(int(start_1), int(end_1) + 1))
    b = set(range(int(start_2), int(end_2) + 1))
    if a.issubset(b) or a.issuperset(b):
        count_1 += 1

    if not a.isdisjoint(b):
        count_2 += 1

print(count_1)
print(count_2)
