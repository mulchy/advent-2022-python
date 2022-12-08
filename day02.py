shape_value = {"X": 1, "Y": 2, "Z": 3}

results = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

from utils.io import read

input = read()

score = 0
for game in input.splitlines():
    score += results[game] + shape_value[game[2]]

print(score)

my_choice = {
    "A X": "Z",
    "A Y": "X",
    "A Z": "Y",
    "B X": "X",
    "B Y": "Y",
    "B Z": "Z",
    "C X": "Y",
    "C Y": "Z",
    "C Z": "X",
}

score = 0
for game in input.splitlines():
    choice = my_choice[game]
    score += results[game[0:2] + choice] + shape_value[choice]

print(score)
