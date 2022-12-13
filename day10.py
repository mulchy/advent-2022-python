from time import sleep


with open("input/day10.txt") as f:
    input = f.readlines()


def run(input):
    state = {"x": 1, "count": 1}

    cycles_we_care_about = [20, 60, 100, 140, 180, 220]
    signal_strengths = []

    display = ["." for _ in range(240)]

    def cycle(n):
        for _ in range(n):
            # part 1
            if state["count"] in cycles_we_care_about:
                signal_strengths.append(state["count"] * state["x"])

            # part 2
            sprite = [state["x"] + i for i in range(-1, 2)]

            if (state["count"] - 1) % 40 in sprite:
                display[state["count"] - 1] = "#"

            # render(display)
            state["count"] += 1

    for line in input:
        match line.split():
            case ["addx", n]:
                cycle(2)
                state["x"] += int(n)
            case ["noop"]:
                cycle(1)
            case _:
                print("failed to parse command")

    print(sum(signal_strengths))
    render(display)


def render(display):
    # print("\033[2J\033[H", end=None)
    print("".join(f"\n{c}" if i % 40 == 0 and i != 0 else c for i, c in enumerate(display)))
    # sleep(0.01)


run(input)
